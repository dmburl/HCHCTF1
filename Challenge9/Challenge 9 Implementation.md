# Challenge 9: The Vulnerable Device
## Setup
The PCAP file from Challenge 8 holds the answer to the URL and the username and password for Challenge 9.
Challenge 9 is at https://dmburl.github.io/HCHCTF1/Challenge9/challenge9.html

## Scenario
From the previous Challenge 8 the participant look through the PCAP file for information related to Challenge 9.
They are looking for:
The URL: https://dmburl.github.io/HCHCTF1/Challenge9/challenge9.html
The username/passowrd: admin/MediCore PM-2024

## Challenge
1. Look through the PCAP file to find the URL and credentials
2. Go to the URL and neter the credentials
3. Look for the flag on the page "FLAG{default_creds_medicore_compromised}"
4. This page will be usd for Challenge 10 and Challenge 11

**Hints**:
- The URL for Challenge 9 is inthe PCAP file from Challenge 8
- The flag is in the middle lower block of data

**Tools Recommended**:
- Wireshark
- tshark (command line)
- NetworkMiner
- tcpdump

## Story Context
The PCAP file has defaiult crdentials from a medicore device. 