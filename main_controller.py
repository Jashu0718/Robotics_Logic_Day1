import robot_actions as action

print("--- Jash-Botics Secure Controller ---")

while True:
    user_input = input("\nEnter Vibration Level (or 'exit'): ")
    
    if user_input.lower() == 'exit':
        break

    # The Safety Net
    try:
        vibe_val = int(user_input)
        status = action.check_vibration(vibe_val)
        print(f"REPORT: {status}")
        # Inside your 'try' block:
        action.save_log(f"Vibration checked: {vibe_val} - Result: {status}")
    except ValueError:
        print("ERROR: Invalid input! Please enter a numerical value for vibration.")