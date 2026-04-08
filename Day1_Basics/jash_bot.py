# Jash-Botics Autonomous Monitor v2.0

print("--- System Online: Monitoring Started ---")

while True:
    # 1. Get user input
    command = input("\nEnter Vibration Level (or 'status' / 'exit'): ").lower()

    # 2. Check for exit command
    if command == "exit":
        print("Shutting down... System Offline.")
        break
    
    # 3. Check for status report
    elif command == "status":
        print("SYSTEM CHECK: CPU i7-1165G7 | OS: Ubuntu 24.04 | Connection: STABLE")
        continue # Skips the rest and starts the loop over

    # 4. Process sensor data (Numbers)
    else:
        vibration = int(command)
        if vibration > 90:
            print("!!! CRITICAL: High Vibration. Emergency Brake Engaged !!!")
        elif vibration > 70:
            print("WARNING: Vibration high. Reducing motor speed.")
        else:
            print("OK: Vibration within normal limits.")