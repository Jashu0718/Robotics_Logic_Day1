# robot_actions.py - The Utility Module

def check_vibration(val):
    if val > 90:
        return "CRITICAL: Shutting down motors!"
    elif val > 75:
        return "WARNING: Reducing speed."
    return "SAFE: Operating at full capacity."

def calculate_battery(voltage):
    # Simple robotics math: percentage based on 12V system
    percentage = (voltage / 12) * 100
    return round(percentage, 2)
def save_log(msg):
    with open("telemetry.log", "a") as f:
        f.write(f"LOG: {msg}\n")