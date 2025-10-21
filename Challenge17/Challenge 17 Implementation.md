# Challenge 17: The Telemetry Leak
## Technical Architecture & Solution Guide

---

## 🏗️ How This Challenge Is Built

### Infrastructure Overview

This challenge simulates a real-world medical IoT vulnerability using the MQTT (Message Queuing Telemetry Transport) protocol, commonly used in healthcare environments for patient monitoring devices.

### Architecture Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Azure Ubuntu Server                       │
│                   (172.184.215.224)                          │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │         Mosquitto MQTT Broker                       │    │
│  │  - Port 1883: Standard MQTT protocol                │    │
│  │  - Port 9001: WebSocket support                     │    │
│  │  - Anonymous access enabled (intentional vuln)      │    │
│  │  - No TLS/SSL encryption (intentional vuln)         │    │
│  └────────────────────────────────────────────────────┘    │
│                           ↓                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │    Telemetry Publisher (Python Script)              │    │
│  │  - Simulates patient monitor in Room 311            │    │
│  │  - Publishes every 5 seconds                        │    │
│  │  - Multiple MQTT topics with different data         │    │
│  │  - Flag hidden in debug messages                    │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                           ↓
              Published MQTT Topics:
   ┌─────────────────────────────────────────────┐
   │ hospital/telemetry/room311/vitals           │ → Heart rate, BP, O2, temp
   │ hospital/telemetry/room311/device_status    │ → Device info, model, firmware
   │ hospital/telemetry/room311/demographics     │ → Patient PII (HIPAA violation!)
   │ hospital/telemetry/room311/alerts          │ → System alerts & DEBUG messages
   │ hospital/telemetry/room311/logs            │ → Device logs with auth tokens
   └─────────────────────────────────────────────┘
                           ↓
                   Participants Subscribe
              (from anywhere on the internet)
```

### MQTT Protocol Basics

**MQTT** is a lightweight publish-subscribe messaging protocol designed for IoT devices:
- **Broker:** Central server that routes messages (Mosquitto in this case)
- **Publisher:** Device/application that sends messages (our telemetry script)
- **Subscriber:** Client that receives messages (participants)
- **Topics:** Hierarchical paths like file systems (`hospital/telemetry/room311/vitals`)
- **QoS:** Quality of Service levels (0, 1, or 2) - we use 0 (fire and forget)

### Security Vulnerabilities (By Design)

This challenge intentionally implements several security flaws found in real medical devices:

1. **No Authentication**
   - `allow_anonymous true` in Mosquitto config
   - Anyone can connect without credentials
   - Real-world example: 2019 study found 83% of medical IoT devices had this flaw

2. **No Encryption**
   - Uses port 1883 (unencrypted) instead of 8883 (TLS/SSL)
   - All patient data transmitted in plaintext
   - HIPAA violation - PHI must be encrypted in transit

3. **Debug Info in Production**
   - Authentication tokens exposed in log messages
   - System debug information leaking sensitive data
   - Common developer mistake: leaving debug code in production

4. **Excessive Data Broadcast**
   - Patient demographics published unnecessarily
   - More data exposed than needed for monitoring
   - Violates principle of least privilege

5. **No Access Control**
   - No topic-level permissions (ACLs)
   - Anyone can subscribe to any topic
   - Should restrict which devices can access which topics

### Data Flow

```
Every 5 seconds, the publisher script:
1. Generates random vital signs (realistic ranges)
2. Creates JSON payloads for each topic
3. Publishes to 5 different MQTT topics
4. Randomly selects an alert message (including flag)
5. Includes auth token in logs (contains flag)
```

**Example Vital Signs Generation:**
```python
{
    "heart_rate": random.randint(75, 95),          # Normal: 60-100 bpm
    "blood_pressure_systolic": random.randint(145, 165),   # Elevated!
    "blood_pressure_diastolic": random.randint(85, 95),    # Elevated!
    "oxygen_saturation": random.randint(94, 98),   # Normal: 95-100%
    "respiratory_rate": random.randint(16, 20),    # Normal: 12-20/min
    "temperature": round(random.uniform(98.2, 99.1), 1)   # Normal: 97-99°F
}
```

**Flag Placement Strategy:**
The flag appears in TWO locations to give participants multiple paths to success:

1. **Primary Location (Alerts Topic):**
   ```json
   {
       "message": "SYSTEM_DEBUG: device_auth_token=CTF{M3D1C4L_T3L3M3TRY_1S_N0T_S3CUR3}"
   }
   ```
   - Appears randomly (1 in 6 chance each cycle)
   - Simulates debug logging accidentally left in production

2. **Secondary Location (Logs Topic):**
   ```json
   {
       "auth_token": "CTF{M3D1C4L_T3L3M3TRY_1S_N0T_S3CUR3}"
   }
   ```
   - Appears in EVERY log message
   - Simulates hardcoded credentials in telemetry

---

## 🎯 How Participants Solve This Challenge

### Phase 1: Understanding the Challenge (2-5 minutes)

Participants read the challenge description and learn:
- Target: Elizabeth Hartwell in Room 311
- Protocol: MQTT (they may need to research this)
- Connection info: Server IP and port
- Goal: Find flag in telemetry stream

**Key realization:** This is a network reconnaissance challenge requiring MQTT knowledge.

### Phase 2: Tool Selection (5-10 minutes)

Participants choose their approach:

**Option A: Command Line (Fastest for experienced users)**
```bash
# Install mosquitto client
sudo apt-get install mosquitto-clients  # Linux
brew install mosquitto                   # macOS

# Connect and subscribe
mosquitto_sub -h 172.184.215.224 -t 'hospital/telemetry/room311/#' -v
```

**Option B: Python Script (Most flexible)**
```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")
    # Can add filtering logic here

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.on_connect = lambda c, u, f, r, p: c.subscribe("hospital/telemetry/room311/#")
client.connect("172.184.215.224", 1883, 60)
client.loop_forever()
```

**Option C: GUI Tool (Best for beginners)**
- Download MQTT Explorer: http://mqtt-explorer.com/
- Connect to 172.184.215.224:1883
- Browse topic tree visually
- See all messages in organized view

**Option D: Web Browser (No installation needed)**
- Go to HiveMQ WebSocket Client: http://www.hivemq.com/demos/websocket-client/
- Host: `172.184.215.224`
- Port: `9001` (WebSocket port)
- Subscribe to: `hospital/telemetry/room311/#`

### Phase 3: Initial Reconnaissance (5-10 minutes)

Once connected, participants see data streaming:

```
hospital/telemetry/room311/vitals {"timestamp":"2025-10-20T...", "vitals":{...}}
hospital/telemetry/room311/device_status {"device":{"device_id":"BEDMON-311-A"...}}
hospital/telemetry/room311/demographics {"patient":{"name":"ELIZABETH HARTWELL"...}}
hospital/telemetry/room311/alerts {"message":"Blood pressure elevated - monitoring"}
hospital/telemetry/room311/logs {"device_id":"BEDMON-311-A", "auth_token":"CTF{...}"}
```

**Observations they should make:**
1. Multiple topics with different data types
2. Some topics contain PHI (Protected Health Information)
3. Demographics topic shows full patient details (HIPAA violation!)
4. Alerts and logs topics contain system information
5. Data updates every 5 seconds

### Phase 4: Pattern Recognition (5-15 minutes)

**Less Experienced Participants:**
- May watch vitals data initially (wrong focus)
- Might need Hint 1 to look beyond medical data
- Eventually notice alerts with "SYSTEM_DEBUG" messages
- Realize debug info shouldn't be in production

**More Experienced Participants:**
- Immediately focus on alerts and logs topics
- Recognize debug messages as suspicious
- Use grep/filtering to isolate interesting messages:
  ```bash
  mosquitto_sub -h 172.184.215.224 -t 'hospital/telemetry/room311/#' -v | grep -i "debug\|token\|ctf"
  ```

### Phase 5: Flag Discovery (Immediate to 60 seconds)

**Path A: Alerts Topic (Random)**
Participants must wait for the debug message to appear:
```json
{
  "timestamp": "2025-10-20T14:23:45",
  "room": "311",
  "alert_type": "INFO",
  "message": "SYSTEM_DEBUG: device_auth_token=FLAG{Medical_Telemetry_is_not_secure}"
}
```
- Appears randomly (~16% chance per cycle)
- Average wait time: 30 seconds
- Teaches patience and observation

**Path B: Logs Topic (Always Present)**
Flag appears in EVERY log message:
```json
{
  "timestamp": "2025-10-20T14:23:50",
  "device_id": "BEDMON-311-A",
  "log_level": "DEBUG",
  "message": "Telemetry stream active for patient VIP-7741",
  "auth_token": "FLAG{Medical_Telemetry_is_not_secure}"
}
```
- Visible immediately if checking logs topic
- More reliable discovery method
- Represents hardcoded credentials

### Phase 6: Flag Submission (1 minute)

Participants submit: `FLAG{Medical_Telemetry_is_not_secure}`

