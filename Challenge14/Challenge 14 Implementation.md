# Challenge 14: The DICOM Manipulation
## Complete Setup Guide
Run this command to modify an existing DCOM file: [dicom_modifier.py](dicom_modifier.py) 
This is an existing anonymized chest x-ray [Anonymized.dcm](Anonymized_20251021.dcm) file.
This will generate this file [Hospital_xray.dcm](hospital_xray_20251021.dcm) that the participant will use to finish the challenge.


## Challenge Brief (Give to Participants)

### Scenario
Following your analysis of the EHR audit logs, you've discovered that someone accessed medical imaging files for the VIP patient in Room 304. The investigation has led you to a suspicious chest X-ray file that was modified on October 21, 2025.

The file appears to be a routine chest X-ray for a patient named "John Smith," but something doesn't add up. The EHR audit logs show this file was accessed and modified during the time window of the attack, yet it seems completely ordinary.

**Your Mission:** Analyze the DICOM medical image file to uncover what the attacker tried to hide. The flag is hidden in the original metadata that wasn't properly sanitized.

### What You Receive
- File: `hospital_xray_20251021.dcm`

### Success Criteria
Extract the flag in the format: `FLAG{...}`

**Recommended Participant Tools:**
- Python with pydicom library
- DCMTK toolkit (dcmdump)
- ExifTool
- Online DICOM viewers (e.g., https://www.dicomlibrary.com)

## Hints System
