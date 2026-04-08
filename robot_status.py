# Jash-Botics Advanced Status Monitor

# 1. Initialize the Robot State Dictionary
robot = {
    "id": "JB-001",
    "battery": 100,
    "vibration": 0.0,
    "temperature": 25.0,
    "status": "Stationary"
}

print(f"--- System Online: {robot['id']} ---")

while True:
    print(f"\n[LIVE TELEMETRY]: {robot}")
    
    cmd = input("Enter 'u' to update sensors or 'exit' to quit: ").lower()
    
    if cmd == 'exit':
        break
    elif cmd == 'u':
        try:
            # 2. Get Input for multiple sensors
            new_vibe = float(input("Enter Vibration (Hz): "))
            new_temp = float(input("Enter Temperature (C): "))

            # 3. Update the Dictionary
            robot["vibration"] = new_vibe
            robot["temperature"] = new_temp

            # 4. Professional Logic: Overheating Check First
            if robot["temperature"] > 100:
                robot["status"] = "OVERHEATING - EMERGENCY SHUTDOWN"
            elif robot["vibration"] > 0.5:
                robot["status"] = "Moving/Active"
            else:
                robot["status"] = "Stationary"

            print(">> Dictionary Updated Successfully.")

        except ValueError:
            # This prevents the crash if user types letters
            print("!! ERROR: Invalid Input. Please use numbers for sensors. !!")
    else:
        print("Unknown command. Press 'u' or 'exit'.")

print("--- System Offline ---")