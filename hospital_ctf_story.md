# Hospital CTF: "Code Red at Mercy General"
## Overarching Story

A cybersecurity incident has occurred at Mercy General Hospital. Patient data has been compromised, medical devices are malfunctioning, and there's evidence of an insider threat. As a digital forensics investigator, you must uncover the attack chain, identify the perpetrator, and secure the hospital's systems before more damage occurs.

## Challenge Flow & Story Progression

### Phase 1: Discovery & Initial Investigation

**Challenge 1: The Whistleblower's Evidence**
- **Scenario**: A concerned employee left a USB drive in the hospital parking lot for investigators to find
- **Challenge**: Analyze the contents of a simulated found USB from a hospital parking lot
- **Story Context**: The USB contains initial evidence pointing to suspicious activity but is encrypted/obfuscated
- **Flag Location**: Hidden in a file on the USB that reveals the first clue about compromised systems

**Challenge 2: The Anonymous Tip**
- **Scenario**: Following the USB evidence, you receive a phone call with additional information
- **Challenge**: Call a number, listen to an IVR system with audio clues, and gather data to answer a quiz
- **Story Context**: The caller provides details about which hospital systems are compromised and mentions a specific patient room
- **Flag Location**: Obtained by correctly answering questions based on the IVR audio clues

### Phase 2: Physical Investigation

**Challenge 3: The Patient Wristband**
- **Scenario**: The IVR mentioned Room 304. You find a discarded patient wristband near that room
- **Challenge**: Have a printed patient wristband with a QR code. Participant attempts to decode it and identify suspicious or vulnerable encoding
- **Story Context**: The wristband belongs to a VIP patient whose data was specifically targeted
- **Flag Location**: Hidden in the QR code data, reveals the patient ID being targeted

**Challenge 4: The Urgent Announcement**
- **Scenario**: As you investigate, an emergency announcement plays over the PA system
- **Challenge**: Play a distorted or noisy hospital PA announcement (e.g., "Code Blue, Room 304"). Participants clean up or interpret the audio using tools like Audacity
- **Story Context**: The announcement contains coded information about which medical devices are compromised
- **Flag Location**: Hidden in the cleaned audio, reveals specific device types under attack

### Phase 3: Digital Forensics

**Challenge 5: The Hospital Documentation**
- **Scenario**: You need to examine hospital documentation for metadata clues
- **Challenge**: Provide a "hospital brochure" PDF or JPEG. Participants use metadata tools to extract author info or embedded location tags
- **Story Context**: The metadata reveals the attacker's identity or connection to the hospital
- **Flag Location**: Hidden in GPS coordinates or author information pointing to the next location

**Challenge 6: The Insider's Trail**
- **Scenario**: Following the metadata clues, you discover evidence of an insider threat
- **Challenge**: Plant a "volunteer" with an exposed Post-it note on their laptop or "forgotten" USB drive. Participants recognize the social engineering flaw and submit the hidden flag
- **Story Context**: A hospital employee has been careless with sensitive information, revealing login credentials
- **Flag Location**: On the Post-it note or USB drive, providing access credentials for the next phase

### Phase 4: Network Investigation

**Challenge 7: The Rogue Network**
- **Scenario**: Using the discovered credentials, you investigate the hospital's wireless infrastructure
- **Challenge**: Create a fake "HospitalGuest" AP and have participants capture traffic or credentials. Participants identify credentials passed in plaintext or intercept a sensitive file
- **Story Context**: The attacker has set up a rogue access point to steal credentials from staff
- **Flag Location**: In the intercepted traffic or captured file

**Challenge 8: The Network Traffic Analysis**
- **Scenario**: With network access, you can now analyze broader hospital communications
- **Challenge**: Analyze a PCAP from hospital traffic to find the leaked patient file
- **Story Context**: The captured traffic reveals how patient data was exfiltrated
- **Flag Location**: Hidden in the PCAP data showing the stolen patient information

### Phase 5: Medical Device Investigation

**Challenge 9: The Vulnerable Device**
- **Scenario**: The PCAP analysis reveals compromised medical devices on the network
- **Challenge**: Simulate a vulnerable embedded medical device (e.g., insulin pump, heart rate monitor), using a Raspberry PI with a web dashboard. Participants identify and exploit a simple vulnerability
- **Story Context**: Critical patient care devices have been compromised and could cause harm
- **Flag Location**: Found by exploiting the device vulnerability (default creds, debug port, etc.)

**Challenge 10: The Hidden Interface**
- **Scenario**: The compromised device leads you to discover a hidden diagnostic interface
- **Challenge**: A demo medical device contains a QR code or file hidden in a non-obvious place (inside UI logs, behind a panel). Participants extract or locate the flag
- **Story Context**: Manufacturers hide diagnostic tools that attackers can abuse
- **Flag Location**: In the hidden QR code or diagnostic file

**Challenge 11: The Device Firmware**
- **Scenario**: You need to examine the device's firmware for hardcoded vulnerabilities
- **Challenge**: Download and extract strings from a sample firmware binary to find the flag
- **Story Context**: The firmware contains hardcoded credentials or backdoors
- **Flag Location**: Hidden in the firmware strings

**Challenge 12: The Interactive Exploit**
- **Scenario**: Some devices have hidden interfaces that only appear under specific conditions
- **Challenge**: A simulated device UI has a hidden QR code only visible under certain interaction
- **Story Context**: Advanced persistent threats use sophisticated hiding techniques
- **Flag Location**: QR code revealed through specific UI interactions

### Phase 6: Electronic Health Records Investigation

**Challenge 13: The Audit Trail**
- **Scenario**: You need to examine who has been accessing patient records inappropriately
- **Challenge**: Analyze a redacted EHR audit log and answer who accessed a file and when
- **Story Context**: The audit logs reveal the insider threat's access patterns
- **Flag Location**: Found by correctly identifying the unauthorized access

**Challenge 14: The DICOM Manipulation**
- **Scenario**: Medical imaging data has been tampered with to hide evidence
- **Challenge**: Modify DICOM metadata to spoof patient data (e.g., name or study description) and extract the flag
- **Story Context**: The attacker modified medical images to cover their tracks
- **Flag Location**: Hidden in the original DICOM metadata before tampering

**Challenge 15: The Encrypted Notes**
- **Scenario**: A nurse's physical notes contain additional clues
- **Challenge**: A nurse's clipboard has notes encrypted with a Caesar cipher or base64
- **Story Context**: Staff were documenting suspicious activities in code
- **Flag Location**: Decrypted message reveals the next piece of the puzzle

### Phase 7: System Integration Attacks

**Challenge 16: The HL7 Exploit**
- **Scenario**: Hospital systems communicate using HL7 messages, which have been weaponized
- **Challenge**: Exploit a basic HL7 message handler with malformed input
- **Story Context**: The attacker is using healthcare communication protocols to spread through systems
- **Flag Location**: Obtained by successfully exploiting the HL7 handler

**Challenge 17: The Telemetry Leak**
- **Scenario**: Patient monitoring devices are leaking data through IoT protocols
- **Challenge**: Subscribe to a demo MQTT topic leaking patient telemetry and find the flag
- **Story Context**: Real-time patient data is being broadcast insecurely
- **Flag Location**: Hidden in the MQTT telemetry stream

**Challenge 18: The Web Interface Injection**
- **Scenario**: Patient monitoring web interfaces are vulnerable to injection attacks
- **Challenge**: Find the injection point in a web UI meant to mimic a patient monitor
- **Story Context**: The attacker is using web vulnerabilities to access patient data
- **Flag Location**: Retrieved through successful web application exploitation

### Phase 8: Communication Security

**Challenge 19: The Insecure Chat**
- **Scenario**: Hospital staff use a "secure" chat application that isn't actually secure
- **Challenge**: Analyze screenshots from a "secure" hospital chat app to find the flaw
- **Story Context**: Confidential communications about the incident have been compromised
- **Flag Location**: Visible in the chat app screenshots showing the security flaw

### Phase 9: Threat Intelligence & Resolution

**Challenge 20: The Vulnerability Research**
- **Scenario**: You need to identify the specific vulnerability being exploited
- **Challenge**: Based on a known vulnerability, name the CVE and the patch date
- **Story Context**: Understanding the exact vulnerability helps prevent future attacks
- **Flag Location**: Correct CVE number and patch date

**Challenge 21: The OSINT Investigation**
- **Scenario**: The attacker has created fake medical facilities as part of their operation
- **Challenge**: Given a list of clinics, identify which one is fake using OSINT
- **Story Context**: The fake clinic is part of a larger healthcare fraud scheme
- **Flag Location**: Correct identification of the fake clinic

## Final Resolution

After completing all challenges, participants will have uncovered:
- The insider threat's identity
- How the attack was carried out
- Which systems were compromised
- What patient data was stolen
- How to prevent similar attacks

The final flag combines elements from multiple challenges to create a master key that "secures" the hospital and completes the investigation.

## Implementation Notes

- Each challenge builds upon information discovered in previous challenges
- Physical items (USB drives, wristbands, clipboards) create tangible investigation elements
- Multiple technical domains (network, firmware, medical protocols) provide diverse skill challenges
- The hospital setting makes the scenario relatable and highlights real-world healthcare security concerns
- Progressive difficulty from basic forensics to advanced exploitation techniques