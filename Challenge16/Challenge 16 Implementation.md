# Challenge 16: THE HL7 EXPLOIT

## Setup
Following the DICOM investigation, you've discovered that the attacker is
manipulating HL7 messages related to Elizabeth Hartwell (MRN: VIP-7741, Room 311).

The hospital's HL7 message handler has been compromised and is accepting
malformed messages. These weaponized healthcare protocol messages are allowing
the attacker to spread through interconnected systems.

## OBJECTIVE
Exploit the vulnerable HL7 message handler to extract the flag and understand
the attack vector being used.

## TARGET
- HL7 Handler IP: 172.184.215.224
- Port: 2575 (standard HL7 port)
- Patient of Interest: Elizabeth Hartwell (VIP-7741)

## TOOLS PROVIDED
- sample_hl7_message.txt (valid message format for reference)
- hl7_exploit_template.py (starter code)

# HINTS
1. HL7 uses pipe (|) delimiters between fields
2. The PV1 segment contains room/location information
3. Look for unsafe evaluation or execution in the handler
4. The system processes messages related to Room 311
5. Python's eval() function is dangerous when handling untrusted input

SUBMIT: The flag in format FLAG{...}

# **For this challenge to be successfult the participant must:**

1. Download the template (has room "999")
2. Run it and see it returns "999"
3. Read the hints about eval() and FLAG
4. Realize they need to inject code
5. Change 999 to ' or FLAG or '
6. Run it again and get the flag!