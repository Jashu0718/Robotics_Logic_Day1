# Jash-Botics Memory System v1.0

# This is an empty List to store sensor data
vibration_history = []

print("--- Memory System Online ---")

while True:
    data = input("Enter vibration reading (or 'history' / 'exit'): ").lower()

    if data == 'exit':
        break
    
    elif data == 'history':
        print(f"Complete Log: {vibration_history}")
        if len(vibration_history) > 0:
            avg = sum(vibration_history) / len(vibration_history)
            print(f"Average Vibration: {avg:.2f}")
    
    else:
        # Convert to number and add to our List
        val = int(data)
        vibration_history.append(val)
        print(f"Recorded: {val}")

        # Robotics Logic: If we have more than 5 records, remove the oldest one
        if len(vibration_history) > 5:
            removed = vibration_history.pop(0)
            print(f"Memory full. Removing oldest record: {removed}")