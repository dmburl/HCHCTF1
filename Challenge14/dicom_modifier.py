#!/usr/bin/env python3
"""
DICOM Challenge File Modifier for Hospital CTF
Challenge 14: The DICOM Manipulation

This script takes an existing DICOM file and modifies it with tampered metadata.
The flag is hidden in the original metadata that the attacker "forgot" to remove.

Requirements: pip install pydicom
"""

import pydicom
from pydicom.uid import generate_uid
from datetime import datetime
import os
import sys
import shutil

def modify_existing_dicom(input_filename='Anonymized_20251011.dcm', 
                          output_filename='hospital_xray_20241015.dcm',
                          backup=True):
    """
    Modifies an existing DICOM file with tampered metadata for the CTF challenge
    
    Args:
        input_filename: Path to the existing DICOM file
        output_filename: Path for the modified challenge file
        backup: If True, creates a backup of the original file
    """
    
    # Check if input file exists
    if not os.path.exists(input_filename):
        print(f"❌ Error: Input file '{input_filename}' not found!")
        print(f"   Please ensure the file exists in the current directory.")
        return False
    
    # Create backup if requested
    if backup:
        backup_filename = input_filename + '.backup'
        shutil.copy2(input_filename, backup_filename)
        print(f"✓ Backup created: {backup_filename}")
    
    try:
        # Read the existing DICOM file
        print(f"\n📂 Reading existing DICOM file: {input_filename}")
        ds = pydicom.dcmread(input_filename)
        
        # Store original values before modification (for the hidden metadata)
        original_patient_name = str(ds.PatientName) if 'PatientName' in ds else 'UNKNOWN'
        original_patient_id = str(ds.PatientID) if 'PatientID' in ds else 'UNKNOWN'
        
        print(f"   Original Patient Name: {original_patient_name}")
        print(f"   Original Patient ID: {original_patient_id}")
        
        # Update file meta information
        dt = datetime.now()
        ds.ContentDate = dt.strftime('%Y%m%d')
        ds.ContentTime = dt.strftime('%H%M%S.%f')
        
        # SPOOFED METADATA (What the attacker changed)
        print(f"\n🎭 Applying spoofed metadata...")
        ds.PatientName = "SMITH^JOHN^M"
        ds.PatientID = "PT987654"
        ds.PatientBirthDate = "19650823"
        ds.PatientSex = "M"
        
        # Study Information (Spoofed)
        ds.StudyDate = "20241015"
        ds.StudyTime = "143022"
        ds.StudyDescription = "CHEST PA AND LATERAL"
        
        # Generate new UIDs for the spoofed study
        ds.StudyInstanceUID = generate_uid()
        ds.AccessionNumber = "ACC20241015789"
        
        # Series Information
        ds.SeriesDate = "20241015"
        ds.SeriesTime = "143525"
        ds.SeriesDescription = "CHEST XRAY 2 VIEWS"
        ds.SeriesInstanceUID = generate_uid()
        ds.SeriesNumber = "1"
        
        # Image Information
        ds.InstanceNumber = "1"
        if hasattr(ds, 'file_meta'):
            ds.SOPInstanceUID = generate_uid()
        
        # Equipment/Institution
        ds.InstitutionName = "SaintCon Hospital"
        ds.Manufacturer = "CTF Medical Systems"
        ds.ManufacturerModelName = "X-RAY-2000"
        ds.StationName = "XRAY_ROOM_3"
        
        # HIDDEN ORIGINAL METADATA (The flag location)
        print(f"🔒 Embedding hidden original metadata...")
        
        # Private Creator tag - this is where smart attackers would look
        ds.add_new([0x0009, 0x0010], 'LO', 'ORIGINAL_PATIENT_DATA')
        ds.add_new([0x0009, 0x1001], 'PN', 'HARTWELL^ELIZABETH^R')  # Original patient name
        ds.add_new([0x0009, 0x1002], 'LO', 'VIP-7741')  # Original patient ID
        ds.add_new([0x0009, 0x1003], 'LO', 'ROOM_311_VIP_CARDIAC_MONITOR')
        
        # Another private tag with more info
        ds.add_new([0x0011, 0x0010], 'LO', 'BACKUP_METADATA')
        ds.add_new([0x0011, 0x1010], 'LO', 'Original_Acc:VIP20251021311')
        
        # Store the ACTUAL original patient data in a hidden tag for forensics realism
        ds.add_new([0x0013, 0x0010], 'LO', 'FORENSIC_BACKUP')
        ds.add_new([0x0013, 0x1001], 'LO', f'REAL_ORIGINAL_NAME:{original_patient_name}')
        ds.add_new([0x0013, 0x1002], 'LO', f'REAL_ORIGINAL_ID:{original_patient_id}')
        
        # Image Comments - often overlooked field with flag
        ds.ImageComments = "ORIGINAL_PT_ID:VIP-7741|BACKUP_STUDY:CARDIAC_CATH|FLAG{VIP_PATIENT_ELIZABETH_HARTWELL_311_COMPROMISED}"
        
        # Operator name might contain original info
        ds.OperatorsName = "TECH_MARTINEZ_J"
        
        # Referring Physician - another place for hidden data
        ds.ReferringPhysicianName = "CARDIOLOGY^DEPT"
        
        # Some metadata inconsistencies that hint at tampering
        ds.PerformingPhysicianName = "DR_CHEN_CARDIO"  # Cardio specialist for a "routine" chest x-ray?
        
        # Ensure proper DICOM format settings
        ds.is_little_endian = True
        ds.is_implicit_VR = False
        
        # Save the modified file
        print(f"\n💾 Saving modified DICOM file: {output_filename}")
        ds.save_as(output_filename, write_like_original=False)
        
        file_size = os.path.getsize(output_filename)
        print(f"✓ DICOM challenge file created successfully!")
        print(f"  File size: {file_size:,} bytes ({file_size/1024:.2f} KB)")
        
        print(f"\n{'='*60}")
        print("CHALLENGE FILE SUMMARY")
        print(f"{'='*60}")
        print(f"Spoofed Patient: SMITH^JOHN^M (PT987654)")
        print(f"Challenge Patient: HARTWELL^ELIZABETH^R (VIP-7741)")
        print(f"Actual Original: {original_patient_name} ({original_patient_id})")
        print(f"Flag location: ImageComments tag (0020,4000)")
        print(f"\nHint for participants: 'Not all metadata is visible in standard viewers...'")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error modifying DICOM file: {e}")
        import traceback
        traceback.print_exc()
        return False

def create_challenge_hints():
    """Generate hint files for CTF organizers"""
    
    hints = """
# Challenge 14: DICOM Manipulation - Hints

## Hint 1 (Easy - 10 points penalty)
"DICOM files can contain private tags that aren't displayed by standard viewers. Try using command-line tools to see ALL metadata."

## Hint 2 (Medium - 20 points penalty)
"Look for tags in the 0x0009 and 0x0011 ranges. Also check the ImageComments field - it's often overlooked."

## Hint 3 (Hard - 30 points penalty)
"Use dcmdump or pydicom to examine every single tag. The attacker only modified standard patient identification fields."

## Solution Commands:

### Using dcmdump (DCMTK):
```bash
dcmdump hospital_xray_20241015.dcm | grep -i "comment\\|private\\|original"
```

### Using pydicom (Python):
```python
import pydicom
ds = pydicom.dcmread('hospital_xray_20241015.dcm')
print(ds.ImageComments)
print(ds[0x0009, 0x1001].value)  # Original patient name
print(ds[0x0009, 0x1002].value)  # Original patient ID
```

### Using exiftool:
```bash
exiftool -a -G1 hospital_xray_20241015.dcm | grep -i comment
```

## Flag Format:
FLAG{VIP_PATIENT_ELIZABETH_HARTWELL_311_COMPROMISED}

## Story Connection:
- Elizabeth Hartwell is the VIP patient from Room 311 (Challenge 2 IVR, Challenge 3 Wristband)
- This proves her cardiac imaging data was specifically targeted
- The attacker tried to hide the evidence by spoofing the patient name
"""
    
    with open('challenge14_hints.txt', 'w') as f:
        f.write(hints)
    print("\n✓ Hint file created: challenge14_hints.txt")

def create_solution_script():
    """Create a solution script for verification"""
    
    solution = """#!/usr/bin/env python3
\"\"\"
Solution script for Challenge 14: DICOM Manipulation
\"\"\"

import pydicom
import sys

def solve_dicom_challenge(filename):
    try:
        # Read the DICOM file
        ds = pydicom.dcmread(filename)
        
        print("="*60)
        print("DICOM METADATA ANALYSIS")
        print("="*60)
        
        # Show spoofed data
        print("\\n[VISIBLE PATIENT DATA - SPOOFED]")
        print(f"Patient Name: {ds.PatientName}")
        print(f"Patient ID: {ds.PatientID}")
        print(f"Study Description: {ds.StudyDescription}")
        
        # Show hidden original data
        print("\\n[HIDDEN ORIGINAL DATA - CHALLENGE]")
        if (0x0009, 0x1001) in ds:
            print(f"Challenge Patient Name: {ds[0x0009, 0x1001].value}")
        if (0x0009, 0x1002) in ds:
            print(f"Challenge Patient ID: {ds[0x0009, 0x1002].value}")
        if (0x0009, 0x1003) in ds:
            print(f"Original Study Info: {ds[0x0009, 0x1003].value}")
        
        # Show actual original data (forensic backup)
        print("\\n[FORENSIC BACKUP - REAL ORIGINAL DATA]")
        if (0x0013, 0x1001) in ds:
            print(f"Real Original Name: {ds[0x0013, 0x1001].value}")
        if (0x0013, 0x1002) in ds:
            print(f"Real Original ID: {ds[0x0013, 0x1002].value}")
        
        # Extract the flag
        print("\\n[FLAG EXTRACTION]")
        if 'ImageComments' in ds:
            comments = ds.ImageComments
            print(f"Image Comments: {comments}")
            
            if 'FLAG{' in comments:
                flag_start = comments.index('FLAG{')
                flag_end = comments.index('}', flag_start) + 1
                flag = comments[flag_start:flag_end]
                print(f"\\n{'='*60}")
                print(f"🚩 FLAG FOUND: {flag}")
                print(f"{'='*60}")
                return flag
        
        print("\\n⚠️  Flag not found in expected location")
        return None
        
    except Exception as e:
        print(f"Error analyzing DICOM file: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution_challenge14.py <dicom_file>")
        sys.exit(1)
    
    solve_dicom_challenge(sys.argv[1])
"""
    
    with open('solution_challenge14.py', 'w') as f:
        f.write(solution)
    print("✓ Solution script created: solution_challenge14.py")

def print_usage():
    """Print usage information"""
    print("\nUsage:")
    print("  python dicom_modifier.py [input_file] [output_file]")
    print("\nExamples:")
    print("  python dicom_modifier.py")
    print("  python dicom_modifier.py Anonymized_20251021.dcm")
    print("  python dicom_modifier.py Anonymized_20251021.dcm challenge_file.dcm")
    print("\nDefault behavior:")
    print("  Input:  Anonymized_20251021.dcm")
    print("  Output: hospital_xray_20251021.dcm")
    print("  A backup file will be created automatically")

if __name__ == "__main__":
    print("="*60)
    print("HOSPITAL CTF - Challenge 14: DICOM Manipulation")
    print("DICOM File Modifier (Uses Existing DICOM File)")
    print("="*60)
    print()
    
    # Parse command line arguments
    input_file = 'Anonymized_20251021.dcm'
    output_file = 'hospital_xray_20251021.dcm'
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    # Check if help is requested
    if '--help' in sys.argv or '-h' in sys.argv:
        print_usage()
        sys.exit(0)
    
    print(f"Input DICOM file:  {input_file}")
    print(f"Output DICOM file: {output_file}")
    print()
    
    # Modify the DICOM file
    success = modify_existing_dicom(input_file, output_file, backup=True)
    
    if success:
        # Create supporting materials
        create_challenge_hints()
        create_solution_script()
        
        print("\n" + "="*60)
        print("✓ All files created successfully!")
        print("="*60)
        print("\nFiles created:")
        print(f"  1. {output_file} - The challenge DICOM file")
        print(f"  2. {input_file}.backup - Backup of original file")
        print("  3. challenge14_hints.txt - Hints for participants")
        print("  4. solution_challenge14.py - Solution verification script")
        print("\nTo test:")
        print(f"  python solution_challenge14.py {output_file}")
        print("\nTo view metadata:")
        print(f"  dcmdump {output_file} | grep -i 'comment\\|original'")
        print(f"  dcmdump {output_file} | grep '(0009'")
        print(f"  dcmdump {output_file} | grep '(0011'")
        print(f"  dcmdump {output_file} | grep '(0013'")
    else:
        print("\n" + "="*60)
        print("❌ File creation failed!")
        print("="*60)
        print("\nPlease check:")
        print(f"  1. Does '{input_file}' exist in the current directory?")
        print("  2. Is pydicom installed? (pip install pydicom)")
        print("  3. Is the file a valid DICOM file?")
        print("\nFor help, run: python dicom_modifier.py --help")
        sys.exit(1)
