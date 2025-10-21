# Challenge 4: The Urgent Announcement
## Implementation Instructions
### Audio Creation Steps
1.	Text-to-Speech Generation
* use Azure Text to Speach tool to create voice using this as a base [Code Blue Alert](<Plain Text Scripts/Code Blue alert.txt>) this as a SSML configured peach file [Code Blue Alert SSML File](<Speech Synthesis Markup Language (SSML) Scripts/Code Blue alert.txt>)
2.	Audio Distortion Layers
Introduce Hospital noise using this file: <audio controls src="Audio File Scripts/stconHospital Code Blue -Ambiant track.mp3" title="Title"></audio>
* Add pink noise overlay at 0.3 intensity
* Export file as MP3

## Key Information Hidden in Audio
Apparent Content:
* Emergency Code Blue in Room 311
* Medical device maintenance request
* Specific device types mentioned

## Hidden Content (requires audio cleanup):
* Station code "Alpha-Seven-Delta-Four-Two-Nine" converts to "A7D429"
* UMDNS codes: 12647, 14355, 13215
* Device types: Philips IntelliVue, GE Carescape, Alaris pumps
* Flag: STCON-UMDNS-12647-14355-13215
## Code Analysis & Meaning
### UMDNS Codes (Flag Components)
1. These are real Universal Medical Device Nomenclature System codes from the ECRI Institute:
* 12647: Physiologic Monitoring Systems, Acute Care (Philips IntelliVue monitors)
* 14355: Ventilators, Other (GE Carescape ventilators)
* 13215: Infusion Pumps, General-Purpose (Alaris infusion delivery systems)
* Story Context: Specific device categories confirmed as compromised
