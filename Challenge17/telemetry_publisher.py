#!/usr/bin/env python3
"""
Patient Telemetry Publisher for Challenge 17
Simulates medical device telemetry for Elizabeth Hartwell
The flag is hidden in the telemetry stream
"""

import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

# MQTT Configuration
BROKER_HOST = "localhost"  # Change to your Azure server IP
BROKER_PORT = 1883

# Patient Information (from previous challenges)
PATIENT_INFO = {
   "name": "ELIZABETH HARTWELL",
    "dob": "03/15/1962",
    "mrn": "VIP-7741",
    "room": "311",
    "admission": "10/21/2025"
}

# Flag hidden in telemetry data
FLAG = "FLAG{Medical_Telemetry_is_not_secure}"

def generate_vital_signs():
    """Generate realistic but slightly concerning vital signs"""
    return {
        "heart_rate": random.randint(75, 95),
        "blood_pressure_systolic": random.randint(145, 165),
        "blood_pressure_diastolic": random.randint(85, 95),
        "oxygen_saturation": random.randint(94, 98),
        "respiratory_rate": random.randint(16, 20),
        "temperature": round(random.uniform(98.2, 99.1), 1)
    }

def generate_device_info():
    """Generate medical device information"""
    return {
        "device_id": "BEDMON-311-A",
        "device_type": "Patient Monitor",
        "manufacturer": "MediTech Solutions",
        "model": "VitalStream 3000",
        "firmware": "v2.4.1",
        "last_calibration": "2025-10-15"
    }

def publish_telemetry(client):
    """Publish various telemetry topics"""
    
    # Topic 1: Basic vitals (most obvious)
    vitals = generate_vital_signs()
    vitals_payload = {
        "timestamp": datetime.now().isoformat(),
        "room": PATIENT_INFO["room"],
        "patient_id": PATIENT_INFO["mrn"],
        "vitals": vitals
    }
    client.publish("hospital/telemetry/room304/vitals", json.dumps(vitals_payload))
    
    # Topic 2: Device status
    device_status = {
        "timestamp": datetime.now().isoformat(),
        "device": generate_device_info(),
        "status": "OPERATIONAL",
        "alerts": []
    }
    client.publish("hospital/telemetry/room311/device_status", json.dumps(device_status))
    
    # Topic 3: Patient demographics (contains PII - security flaw)
    demographics = {
        "timestamp": datetime.now().isoformat(),
        "patient": PATIENT_INFO,
        "attending_physician": "Dr. Sarah Mitchell",
        "diagnosis": "Hypertension, Type 2 Diabetes",
        "allergies": ["Penicillin", "Latex"]
    }
    client.publish("hospital/telemetry/room311/demographics", json.dumps(demographics))
    
    # Topic 4: Alert stream (where flag is hidden)
    # The flag appears in alert messages periodically
    alert_messages = [
        "Blood pressure elevated - monitoring",
        "Patient vitals stable",
        "Medication due in 30 minutes",
        f"SYSTEM_DEBUG: device_auth_token={FLAG}",  # Flag hidden as debug message
        "Nurse call button test successful",
        "IV pump flow rate normal"
    ]
    
    alert = {
        "timestamp": datetime.now().isoformat(),
        "room": PATIENT_INFO["room"],
        "alert_type": "INFO",
        "message": random.choice(alert_messages)
    }
    client.publish("hospital/telemetry/room311/alerts", json.dumps(alert))
    
    # Topic 5: Equipment logs (alternative flag location)
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "device_id": "BEDMON-311-A",
        "log_level": "DEBUG",
        "message": f"Telemetry stream active for patient {PATIENT_INFO['mrn']}",
        "auth_token": FLAG  # Flag also hidden here
    }
    client.publish("hospital/telemetry/room311/logs", json.dumps(log_entry))

#def on_connect(client, userdata, flags, rc):
def on_connect(client, userdata, flags, rc, properties=None):
    """Callback when connected to broker"""
    if rc == 0:
        print("✓ Connected to MQTT broker")
        print(f"✓ Publishing telemetry for {PATIENT_INFO['name']}")
        print(f"✓ Room: {PATIENT_INFO['room']}")
        print("\nAvailable topics:")
        print("  - hospital/telemetry/room311/vitals")
        print("  - hospital/telemetry/room311/device_status")
        print("  - hospital/telemetry/room311/demographics")
        print("  - hospital/telemetry/room311/alerts")
        print("  - hospital/telemetry/room311/logs")
        print("\nTelemetry stream active. Press Ctrl+C to stop.")
    else:
        print(f"✗ Connection failed with code {rc}")

def main():
    """Main publisher loop"""
    client = mqtt.Client(client_id="PatientMonitor_Room311", callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
#    client = mqtt.Client("PatientMonitor_Room311")
    client.on_connect = on_connect
    
    try:
        print(f"Connecting to MQTT broker at {BROKER_HOST}:{BROKER_PORT}...")
        client.connect(BROKER_HOST, BROKER_PORT, 60)
        client.loop_start()
        
        # Publish telemetry every 5 seconds
        while True:
            publish_telemetry(client)
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n\nShutting down telemetry publisher...")
        client.loop_stop()
        client.disconnect()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
