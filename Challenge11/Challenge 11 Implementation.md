# Challenge 11: The Device Firmware
## Setup
The website for Challenge 9 at https://dmburl.github.io/HCHCTF1/Challenge9/challenge9.html has a link in a hidden non-obvious place. (Upper right corner)
Using this [c script](medicalFirmware.c) to create this [medicore firmware](medicoreFirmware) file.

## Scenario
From the previous Challenge 9, the participant identifies the hidden link and clicks on it. From this link the participant downloads the medicoreFirmware.bin for this challenge.
Run the appropriate commands to extract the flags.

## Challenge
1. Find the hiden link
2. Download the medicoreFirmware.bin
3. Extract all readable strings usinf this command strings medicoreFirmware.bin
4. Search for the flag
5. Find other secrets

**Hints**:
- The website from Challenge 9 is used for this Challenge.
- The flag is in the mmedicoreFirmware.bin that is under a hidden link

## Story Context
The medicoreFirmware.bin holds the flag. 