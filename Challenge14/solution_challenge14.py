#!/usr/bin/env python3
"""
Solution script for Challenge 14: DICOM Manipulation
"""

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
        print("\n[VISIBLE PATIENT DATA - SPOOFED]")
        print(f"Patient Name: {ds.PatientName}")
        print(f"Patient ID: {ds.PatientID}")
        print(f"Study Description: {ds.StudyDescription}")
        
        # Show hidden original data
        print("\n[HIDDEN ORIGINAL DATA - CHALLENGE]")
        if (0x0009, 0x1001) in ds:
            print(f"Challenge Patient Name: {ds[0x0009, 0x1001].value}")
        if (0x0009, 0x1002) in ds:
            print(f"Challenge Patient ID: {ds[0x0009, 0x1002].value}")
        if (0x0009, 0x1003) in ds:
            print(f"Original Study Info: {ds[0x0009, 0x1003].value}")
        
        # Show actual original data (forensic backup)
        print("\n[FORENSIC BACKUP - REAL ORIGINAL DATA]")
        if (0x0013, 0x1001) in ds:
            print(f"Real Original Name: {ds[0x0013, 0x1001].value}")
        if (0x0013, 0x1002) in ds:
            print(f"Real Original ID: {ds[0x0013, 0x1002].value}")
        
        # Extract the flag
        print("\n[FLAG EXTRACTION]")
        if 'ImageComments' in ds:
            comments = ds.ImageComments
            print(f"Image Comments: {comments}")
            
            if 'FLAG{' in comments:
                flag_start = comments.index('FLAG{')
                flag_end = comments.index('}', flag_start) + 1
                flag = comments[flag_start:flag_end]
                print(f"\n{'='*60}")
                print(f"🚩 FLAG FOUND: {flag}")
                print(f"{'='*60}")
                return flag
        
        print("\n⚠️  Flag not found in expected location")
        return None
        
    except Exception as e:
        print(f"Error analyzing DICOM file: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution_challenge14.py <dicom_file>")
        sys.exit(1)
    
    solve_dicom_challenge(sys.argv[1])
