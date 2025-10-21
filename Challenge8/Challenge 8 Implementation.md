# Challenge 8: The Network Traffic Analysis
## Setup
Use this python script [python script](challenge8_createPCAP.py) to created the PCAP file using 

## Scenario
From the previous Challenge 7 the participant can download the [PCAP File](hospital_network_traffic.pcap) for this challenge.

This file also points to Challenge 9's URL and Username and password.

## Challenge
1. Download the [PCAP File](hospital_network_traffic.pcap)
2. Open it in Wireshark or similar network analysis tool
3. Look for suspicious outbound traffic
4. Identify protocols being used for data exfiltration
5. Extract the hidden flag that represents the stolen patient data

**Hints**:
- Look for unusual outbound connections
- Check common protocols: HTTP, SMTP, FTP, DNS
- Patient data might be encoded (Base64, hex, etc.)
- Pay attention to traffic to external IP addresses
- The flag format is: FLAG{...}

**Tools Recommended**:
- Wireshark
- tshark (command line)
- NetworkMiner
- tcpdump

## Story Context
The PCAP file has leaked data for Elizabeth Hartwell. 

## Flag Location
There are three locations where the FLAG can be found in the PCAP file. All three locations have the same flag. Finding one will fulfill the challenge.