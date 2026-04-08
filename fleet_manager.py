# Jash-Botics Fleet Manager v2.0 (with Persistent Logging)

# 1. A List of Dictionaries (Your Robot Fleet)
fleet = [
    {"id": "Bot-01", "temp": 25},
    {"id": "Bot-02", "temp": 110}, # Overheating!
    {"id": "Bot-03", "temp": 30},
    {"id": "Bot-04", "temp": 150}  # Another one!
]

print("--- Scanning Fleet and Writing to Log ---")

# 2. Open the file in 'a' (append) mode
# This ensures we don't delete previous alerts
with open("fleet_alerts.txt", "a") as f:
    for bot in fleet:
        if bot["temp"] > 100:
            alert_msg = f"!!! ALERT: {bot['id']} CRITICAL (Temp: {bot['temp']}C)\n"
            
            # Print to screen for the operator
            print(alert_msg.strip())
            
            # Write to the permanent log file
            f.write(alert_msg)
        else:
            print(f"Status OK: {bot['id']} is stable.")

print("\nScan Complete. Check 'fleet_alerts.txt' for historical data.")