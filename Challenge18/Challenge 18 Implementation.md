# Challenge 18: The Web Interface Injection - Setup Guide
## Challenge Overview
Participants must exploit a SQL injection vulnerability in the patient monitoring web interface to retrieve the flag from a hidden administrative record.
##Vulnerability Details
- Type: SQL Injection
- Location: Patient search functionality
- Weakness: Unsanitized user input directly concatenated into database query

## Solution Approaches
- Method 1: Classic SQL Injection
- Search for: ' OR '1'='1
- Method 2: Admin Keyword
- Search for: admin
- Method 3: Always-True Condition
- Search for: ' OR 1=1 --
- Method 4: Union-based (conceptual)
- Search for: ' UNION SELECT * FROM patients WHERE id='ADMIN
- Expected Flag
- FLAG{SQL_Injection_via_patient_query}
## Hints for Participants

- Press 'H' key three times in the interface for console hints
- Try searching for Room 304 first (legitimate query)
- Notice the help text mentions specific search terms
- Check the browser console for debugging information
- Think about how the query might be constructed on the backend

## Story Connection
This challenge reveals how the attacker has been accessing patient data through the vulnerable web interface, specifically targeting VIP patient data from Room 304 (connecting back to earlier challenges about the patient wristband and PA announcement).
