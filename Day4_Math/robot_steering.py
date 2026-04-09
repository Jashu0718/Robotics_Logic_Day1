import numpy as np

def get_target_angle(current_pos, target_pos):
    # Calculate the difference
    diff = target_pos - current_pos
    
    # math.atan2(y, x) gives the angle in RADIANS
    radians = np.arctan2(diff[1], diff[0])
    
    # Convert to Degrees because humans think in degrees
    degrees = np.degrees(radians)
    return degrees

# Test Case
my_pos = np.array([0, 0])
goal_pos = np.array([-10, 0]) # Target is straight ahead on the Y-axis

heading = get_target_angle(my_pos, goal_pos)

print(f"Current Position: {my_pos}")
print(f"Target Position:  {goal_pos}")
print(f"Robot must turn to: {heading:.2f} degrees")