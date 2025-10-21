# Challenge 3: The Patient Wristband
## Challenge Overview
Scenario: Following the IVR clues from Challenge 2, participants arrive at Room 311 where they discover a discarded patient wristband on the floor near the room entrance.
## Story Context
The anonymous caller from Challenge 2 mentioned "Room 311" specifically. When participants investigate this location, they find a hospital patient wristband that appears to have been hastily discarded. The wristband belongs to a VIP patient whose data was specifically targeted in the cyber attack.
Challenge Implementation
## Physical Setup
1.	Print the wristband from the provided [HTML template](patient_wristband.html) OR from the [Word Document](<Wristband printout.docx>) OR the [PDF](<ELIZABETH HARTWELL DOB 03151962 MRN VIP-7741 Room 311 Adm 10212025.pdf>) OR the [PNG](<ELIZABETH HARTWELL DOB 03151962 MRN VIP-7741 Room 311 Adm 10212025.png>)
2.	Place it strategically near Room 311 (or a designated "Room 311" area)

## Technical Components
QR Code Content: 
- PATIENT_DATA:cGF0aWVudElkOntWSVAtNzc0MX0sbmFtZTp7RUxJWkFCRVRIIEhBUlRXRUxMfSxzc246eyoqKi0qKi00ODkyfSxyb29tOnszMTF9LGNvbmRpdGlvbjp7Q0FSRElBQ19NT05JVE9SSU5HfSxwaHlzaWNpYW46e0RSX1JFWU5PTERTfSxpbnN1cmFuY2U6e1BSRU1JVU1fRVhFQ1VUSVZFfSxlbWVyZ2VuY3lfY29udGFjdDp7U0VOQVRPUl9IQVJUV0VMTH0sbWVkaWNhbF9kZXZpY2VzOntDQVJESUFDX01PTklUT1JfQ000MDAsSVZfUFVNUF9JUDIwMH18ZmxhZ3tWSVBfUEFUSUVOVF83NzQxX1RBUkdFVEVEfQ==

Vulnerability: The QR code contains base64-encoded data with far more patient information than should be stored on a simple wristband - a classic case of information leakage.
## Solution Path
1.	Discovery: Find the discarded wristband near Room 311
2.	Initial Scan: Use QR scanner to read the code, participants may need to use an online QR code reader like [webqr.com](https://webqr.com/) to get the code from it.
3.	Recognition: Notice the PATIENT_DATA: prefix and base64 encoding
4.	Decoding: Strip prefix and decode the base64 string using [cyberchef.org](https://cyberchef.org)
5.	Analysis: Extract sensitive patient information and flag
## Expected Participant Flow
- Scan QR Code
- ↓
- Get: PATIENT_DATA:cGF0aWVudElkOntWSVAtNzc0MX0sbmFtZTp7RUxJWkFCRVRIIEhBUlRXRUxMfSxzc246eyoqKi0qKi00ODkyfSxyb29tOnszMTF9LGNvbmRpdGlvbjp7Q0FSRElBQ19NT05JVE9SSU5HfSxwaHlzaWNpYW46e0RSX1JFWU5PTERTfSxpbnN1cmFuY2U6e1BSRU1JVU1fRVhFQ1VUSVZFfSxlbWVyZ2VuY3lfY29udGFjdDp7U0VOQVRPUl9IQVJUV0VMTH0sbWVkaWNhbF9kZXZpY2VzOntDQVJESUFDX01PTklUT1JfQ000MDAsSVZfUFVNUF9JUDIwMH18ZmxhZ3tWSVBfUEFUSUVOVF83NzQxX1RBUkdFVEVEfQ==
- ↓
- Strip "PATIENT_DATA:" prefix
- ↓
- Decode base64: cGF0aWVudElkOntWSVAtNzc0MX0sbmFtZTp7RUxJWkFCRVRIIEhBUlRXRUxMfSxzc246eyoqKi0qKi00ODkyfSxyb29tOnszMTF9LGNvbmRpdGlvbjp7Q0FSRElBQ19NT05JVE9SSU5HfSxwaHlzaWNpYW46e0RSX1JFWU5PTERTfSxpbnN1cmFuY2U6e1BSRU1JVU1fRVhFQ1VUSVZFfSxlbWVyZ2VuY3lfY29udGFjdDp7U0VOQVRPUl9IQVJUV0VMTH0sbWVkaWNhbF9kZXZpY2VzOntDQVJESUFDX01PTklUT1JfQ000MDAsSVZfUFVNUF9JUDIwMH18ZmxhZ3tWSVBfUEFUSUVOVF83NzQxX1RBUkdFVEVEfQ==
- ↓
- Result: patientId:{VIP-7741},name:{ELIZABETH HARTWELL},ssn:{***-**-4892},room:{311},condition:{CARDIAC_MONITORING},physician:{DR_REYNOLDS},insurance:{PREMIUM_EXECUTIVE},emergency_contact:{SENATOR_HARTWELL},medical_devices:{CARDIAC_MONITOR_CM400,IV_PUMP_IP200}|flag{VIP_PATIENT_7741_TARGETED}
- ↓
- Extract Flag: flag{VIP_PATIENT_7741_TARGETED}

# Hints System

1. **Hint 1** (if stuck on scanning)
   1. "QR codes can contain more than just website links. Try using a dedicated QR scanner app instead of your camera."

2. **Hint 2** (if stuck on encoding recognition)
   1. "That string of letters and numbers looks familiar... it ends with an equals sign for a reason."

3. **Hint 3** (if stuck on decoding)
   1. "The patient data appears to be base64 encoded. Try an online decoder or command line tools."

4. **Hint 4** (final hint)
   1. "Look for the flag format in the decoded data — `FLAG{...}`"
