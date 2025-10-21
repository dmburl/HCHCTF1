# Challenge 2: The Anonymous Tip

## Implementation Notes
Below are the audio scripts, the SSML markup scripts and the outputted audio files. 

Add these files to a IVR system, I used voip.ms, to create the pathway for answering the questions. I would love to have a diagram for this, but I don't.

## Audio Scripts
### Used in this order:
- [SC-Main Menu](<Script Files/SC-Main Menu.txt>) 
- [SC-Access Code Check](<Script Files/SC-Access Code Check.txt>)
- [SC-Invalide Code](<Script Files/SC-Invalid Code.txt>) 
- [SC-Briefing Heading](<Script Files/SC-Briefing Heading.txt>)
- [SC-Briefing](<Script Files/SC-Briefing.txt>)
- [SC-Question 1](<Script Files/SC-Question 1.txt>)
- [SC-Question 2](<Script Files/SC-Question 2.txt>) 
- [SC-Question 3](<Script Files/SC-Question 3.txt>) 
- [SC-Verification End](<Script Files/SC-Verification End.txt>)
- Not used [SC-Correct. Next Question](<Script Files/SC-Correct. Next Question.txt>)
- Not used [SC-Incorect](<Script Files/SC-Incorrect.txt>)

## Speech Synthesis Markup Language (SSML) Scripts
- [SC-Main Menu](<Speech Synthesis Markup Language (SSML) Scripts/SC-Main Menu.txt>) 
- [SC-Access Code Check](<Speech Synthesis Markup Language (SSML) Scripts/SC-Access Code Check.txt>) 
- [SC-Invalid Code](<Speech Synthesis Markup Language (SSML) Scripts/SC-Invalid Code.txt>) 
- [SC-Briefing Heading](<Speech Synthesis Markup Language (SSML) Scripts/SC-Briefing Heading.txt>) 
- [SC-Briefing](<Speech Synthesis Markup Language (SSML) Scripts/SC-Briefing.txt>) 
- [SC-Question 1](<Speech Synthesis Markup Language (SSML) Scripts/SC-Question 1.txt>) 
- [SC-Question 2](<Speech Synthesis Markup Language (SSML) Scripts/SC-Question 2.txt>) 
- [SC-Question 3](<Speech Synthesis Markup Language (SSML) Scripts/SC-Question 3.txt>) 
- [SC-Verification End](<Speech Synthesis Markup Language (SSML) Scripts/SC-Verification End.txt>)
- Not used [SC-Correct. Next Question](<Speech Synthesis Markup Language (SSML) Scripts/SC-Correct. Next Question.txt>) 
- Not used [SC-Incorrect](<Speech Synthesis Markup Language (SSML) Scripts/SC-Incorrect.txt>) 



## Audio Recordings
|Name                         | Audio File                                   | 
|-----------------------------|----------------------------------------------|
|- SC-Main Menu | <audio controls src="Audio Files/SC-Main Menu.mp3" title="SC-Main Menu"></audio> |
|- SC-Access Code Check | <audio controls src="Audio Files/SC-Access Code Check.mp3" title="SC-Access Code Check"></audio> | 
|- SC-Invalid Code | <audio controls src="Audio Files/SC-Invalid Code.mp3" title="SC-Invalid Code"></audio> |
|- SC-Briefing Heading | <audio controls src="Audio Files/SC-Briefing Heading.mp3" title="SC-Briefing Heading"></audio> |
|- SC-Briefing | <audio controls src="Audio Files/SC-Briefing.mp3" title="SC-Briefing"></audio> |
|- SC-Question 1 | <audio controls src="Audio Files/SC-Question 1.mp3" title="SC-Question 1"></audio> |
|- SC-Question 2 | <audio controls src="Audio Files/SC-Question 2.mp3" title="SC-Question 2"></audio> |
|- SC-Question 3 | <audio controls src="Audio Files/SC-Question 3.mp3" title="SC-Question 3"></audio> |
|- SC-Verification End | <audio controls src="Audio Files/SC-Verification End.mp3" title="SC-Verification End"></audio> |
|- Not used SC-Correct. Next Question | <audio controls src="Audio Files/SC-Correct. Next Question.mp3" title="SC-Correct. Next Question"></audio> |
|- Not used SC-Incorrect | <audio controls src="Audio Files/SC-Incorrect.mp3" title="SC-Incorrect"></audio> |


## Technical Notes for VoIP.ms Setup
- File Format: MP3
- Maximum Tries: 3 attempts before hangup
- Expected Access Code: STCON (78266)
- Expected Quiz Answers: 1, 3, 304

