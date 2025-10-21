# Challenge 19: The Insecure Chat
## Objective
Hospital staff have been using "SecureHealthChat™" to discuss patient care during the security incident. Your job is to analyze screenshots of their conversation and identify security vulnerabilities that expose sensitive information.
## What You're Given

- Screenshots of a chat conversation between Dr. Sarah Chen and Marcus Webb
- The chat app claims to be "secure" with end-to-end encryption
- Conversation took place at 2:47 AM (the same time as the security breach)

## How to Solve
### Step 1: Visual Inspection
Carefully examine the screenshots for obvious security flaws:
- Look for debug information, development warnings, or error messages
- Check for any overlays, banners, or indicators that shouldn't be visible in production
- Notice any suspicious timing or correlations with previous challenges

### Step 2: Metadata Analysis
 - Extract and analyze metadata from the screenshot images:

    * exiftool screenshot.jpg
    * exiftool screenshot.png

Look for:

- GPS coordinates embedded in the image
- Author/creator information
- Timestamps and device information
- Hidden comments or tags

### Step 3: Technical Analysis
If the screenshots show a web-based interface:

- Check the URL bar - is it HTTP or HTTPS?
- Look for "Not Secure" warnings
- Examine any visible API endpoints or connection strings
- Check for exposed debug consoles or developer tools

### Step 4: Source Code Inspection (Advanced)
If provided with the HTML file or able to access the page:

- View page source (right-click → View Page Source)
- Check browser console (F12 → Console tab)
- Look in CSS comments
- Examine JavaScript variables and functions

### Step 5: Content Analysis
Read the conversation carefully:

- What sensitive information is being discussed?
- Are there any references to credentials or system access?
- Does the conversation reveal information about the breach?
- Note any mentions of fake clinics, unauthorized access, or compromised accounts

### What to Submit

- The flag found through one or more of the methods above
- The security vulnerability you identified (e.g., "Debug mode enabled in production")
- Why this is dangerous in a healthcare setting

### Hints

- Apps claiming to be "secure" aren't always what they seem
- Development builds should never be used for sensitive communications
- Sometimes the biggest security flaws are hiding in plain sight
- Pay attention to what's visible at the bottom of the screen
