# Jash-Botics Safe Input System

while True:
    user_input = input("Enter Sensor Value (or 'exit'): ")
    
    if user_input.lower() == 'exit':
        break

    try:
        # We TRY to convert to an integer
        val = int(user_input)
        print(f"Sensor Reading: {val} - System Stable.")
    except ValueError:
        # If the user typed text instead of a number, we catch the error!
        print("!!! ERROR: Invalid Input. Please enter a NUMBER only !!!")