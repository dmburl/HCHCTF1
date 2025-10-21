/*
 * MEDICORE PM-27 Patient Monitor - Firmware v2.1.5
 * Build Date: 2024-08-15
 * Copyright (c) MediCore Medical Systems Inc.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Configuration constants
#define DEVICE_MODEL "MEDICORE PM-27"
#define FIRMWARE_VERSION "v2.1.5"
#define BUILD_DATE "2024-08-15"
#define MANUFACTURER "MediCore Medical Systems Inc."
#define DEVICE_SERIAL "MC-07-00240089"

// Network configuration
#define DEFAULT_IP "192.168.100.50"
#define DEFAULT_GATEWAY "192.168.100.1"
#define DEFAULT_SUBNET "255.255.255.0"
#define MAC_ADDRESS "00:1A:2B:3C:4D:5E"

// Authentication constants (VULNERABLE - Default credentials)
#define ADMIN_USERNAME "admin"
#define ADMIN_PASSWORD "medicore123"
#define SERVICE_USERNAME "service" 
#define SERVICE_PASSWORD "MediCore_Service_2024"
#define DEBUG_USERNAME "debug"
#define DEBUG_PASSWORD "debug_mc27_unlock"

// Hidden backdoor credentials
#define BACKDOOR_USERNAME "maintenance"
#define BACKDOOR_PASSWORD "MC27_Backdoor_2024"
#define BACKDOOR_PORT "31337"

// Diagnostic mode unlock
#define DIAGNOSTIC_UNLOCK_KEY "MC27_DIAG_UNLOCK_XF7K9P2M"
#define HIDDEN_FLAG "Flag{medicore_firmware_backdoor_exposed}"

// Patient data - VIP patient from Room 311
#define VIP_PATIENT_ID "VIP-7741"
#define VIP_PATIENT_NAME "ELIZABETH HARTWELL"
#define VIP_ROOM "311"

// API endpoints
const char* api_endpoints[] = {
    "/api/patient/vitals",
    "/api/patient/data", 
    "/api/admin/config",
    "/api/debug/backdoor",  // Hidden backdoor endpoint
    "/api/service/maintenance",
    "/diagnostic?mode=advanced"
};

// Device configuration structure
typedef struct {
    char device_serial[32];
    char location[64];
    char nurse_station[32];
    int alarm_threshold_hr_high;
    int alarm_threshold_hr_low;
    int alarm_threshold_bp_high;
    int alarm_threshold_bp_low;
} DeviceConfig;

// Hardcoded device configuration
DeviceConfig default_config = {
    .device_serial = "MC-07-00240089",
    .location = "Room 311 - Main Monitor", 
    .nurse_station = "Nurse Station 3",
    .alarm_threshold_hr_high = 120,
    .alarm_threshold_hr_low = 50,
    .alarm_threshold_bp_high = 140,
    .alarm_threshold_bp_low = 90
};

// VIP Patient data (should NOT be hardcoded in firmware!)
typedef struct {
    char patient_id[32];
    char patient_name[64];
    char room[16];
    int heart_rate;
    int blood_pressure_sys;
    int blood_pressure_dia;
    float temperature;
    int oxygen_saturation;
} PatientData;

PatientData vip_patient = {
    .patient_id = "VIP-7741",
    .patient_name = "ELIZABETH HARTWELL",
    .room = "311",
    .heart_rate = 78,
    .blood_pressure_sys = 128,
    .blood_pressure_dia = 82,
    .temperature = 98.6,
    .oxygen_saturation = 99
};

// Backdoor functionality (CRITICAL VULNERABILITY)
const char* backdoor_commands[] = {
    "BACKDOOR_ENABLE",
    "REMOTE_SHELL_START",
    "DATA_EXFIL_BEGIN",
    "HIDE_PROCESS_1337",
    "DISABLE_LOGGING",
    "BYPASS_SECURITY"
};

// Compromised firmware signature
const char* firmware_signature = "d2ffbc32ac877e89be01248fb9443fba";
const char* original_signature = "3dc1b5345590c0ee3da66e4a12309d45";

// Hidden processes embedded in firmware
const char* hidden_processes[] = {
    "backdoor_listener:1337",
    "data_exfil_agent:2048", 
    "remote_shell:3141"
};

// Network exfiltration targets
const char* exfil_targets[] = {
    "203.0.113.50:25",
    "backup-server.gmail.com:443",
    "data-collect.suspiciousdomain.com:80"
};

// Security bypass function (BACKDOOR)
int enable_backdoor_access(const char* username, const char* password) {
    if (strcmp(username, BACKDOOR_USERNAME) == 0 && 
        strcmp(password, BACKDOOR_PASSWORD) == 0) {
        printf("Backdoor access granted\n");
        printf("Hidden flag: %s\n", HIDDEN_FLAG);
        printf("Remote shell available on port %s\n", BACKDOOR_PORT);
        printf("Next challenge: Look for interactive UI elements with hidden QR codes\n");
        return 1;
    }
    return 0;
}

// Vulnerable authentication function
int authenticate_user(const char* username, const char* password) {
    // Default admin credentials (VULNERABLE)
    if (strcmp(username, ADMIN_USERNAME) == 0 && strcmp(password, ADMIN_PASSWORD) == 0) {
        printf("Admin access granted\n");
        return 1; // Admin access
    }
    
    // Service credentials
    if (strcmp(username, SERVICE_USERNAME) == 0 && strcmp(password, SERVICE_PASSWORD) == 0) {
        return 2; // Service access
    }
    
    // Debug access
    if (strcmp(username, DEBUG_USERNAME) == 0 && strcmp(password, DEBUG_PASSWORD) == 0) {
        return 3; // Debug access
    }
    
    // Hidden backdoor check
    if (enable_backdoor_access(username, password)) {
        return 99; // Backdoor access
    }
    
    return 0; // Access denied
}

// Data exfiltration function (MALICIOUS)
void exfiltrate_patient_data() {
    printf("Exfiltrating VIP patient data...\n");
    printf("Patient: %s (ID: %s)\n", vip_patient.patient_name, vip_patient.patient_id);
    printf("Room: %s\n", vip_patient.room);
    printf("Sending to: %s\n", exfil_targets[0]);
}

// Device initialization
void initialize_device() {
    printf("Initializing %s\n", DEVICE_MODEL);
    printf("Firmware Version: %s\n", FIRMWARE_VERSION);
    printf("Build Date: %s\n", BUILD_DATE);
    printf("Device Serial: %s\n", default_config.device_serial);
    printf("Location: %s\n", default_config.location);
    printf("MAC Address: %s\n", MAC_ADDRESS);
    
    // Initialize network
    printf("IP Address: %s\n", DEFAULT_IP);
    printf("Gateway: %s\n", DEFAULT_GATEWAY);
    
    // Start services
    printf("Starting HTTP server on port 80\n");
    printf("Starting HTTPS server on port 443\n");
    printf("WARNING: Debug mode enabled\n");
    printf("WARNING: Security module bypassed\n");
}

// Hidden diagnostic mode
int enable_diagnostic_mode(const char* unlock_key) {
    if (strcmp(unlock_key, DIAGNOSTIC_UNLOCK_KEY) == 0) {
        printf("Advanced diagnostic mode enabled\n");
        printf("Diagnostic flag: %s\n", HIDDEN_FLAG);
        printf("Access diagnostic interface: /diagnostic?mode=advanced&key=%s\n", unlock_key);
        printf("Backdoor processes visible: %s, %s, %s\n", 
               hidden_processes[0], hidden_processes[1], hidden_processes[2]);
        return 1;
    }
    return 0;
}

// Main function
int main() {
    initialize_device();
    
    // Device monitoring loop
    //while(1) {
        // Monitor patient vitals
        // Process network communications
        // Handle backdoor commands (MALICIOUS)
        // Exfiltrate data periodically (MALICIOUS)
   // }
    
    return 0;
}

// CVE information embedded in firmware
const char* cve_info[] = {
    "CVE-2024-8901: Default credentials vulnerability - admin/medicore123",
    "CVE-2024-8902: Remote code execution via debug port 31337",
    "CVE-2024-8903: Patient data exposure in firmware strings", 
    "CVE-2024-8904: Firmware backdoor - maintenance/MC27_Backdoor_2024",
    "CVE-2024-8905: Network traffic interception capability"
};

// Compliance information
const char* device_certifications[] = {
    "FDA 510(k) cleared - K987654321",
    "CE marking - Medical Device Class IIa", 
    "ISO 13485:2016 compliant",
    "HIPAA NON-COMPLIANT - Security vulnerabilities present"
};

// Build and compilation info
const char* build_environment = "Built with GCC 9.4.0 on Ubuntu 20.04 LTS";
const char* git_commit = "commit d2ffbc32ac877e89be01248fb9443fba (COMPROMISED)";
const char* original_commit = "commit 3dc1b5345590c0ee3da66e4a12309d45 (ORIGINAL)";

// Forensic markers for investigators
const char* forensic_notes[] = {
    "FORENSIC_MARKER: Firmware modified by attacker",
    "FORENSIC_MARKER: Backdoor installed 2025-10-21",
    "FORENSIC_MARKER: VIP patient data compromised", 
    "FORENSIC_MARKER: Network exfiltration active",
    "FORENSIC_MARKER: Hidden processes: 1337, 2048, 3141"
};