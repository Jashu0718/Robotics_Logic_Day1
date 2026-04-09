import numpy as np
import time

robot_pos = np.array([0.0, 0.0])
target_pos = np.array([10.0, 10.0])
step_size = 1.0  # Smaller steps are more stable
tolerance = 0.5  # Stop when within 50cm

print("Mission Started...")

for i in range(100): # Hard limit of 100 steps
    dist_to_goal = np.linalg.norm(target_pos - robot_pos)
    
    if dist_to_goal < tolerance:
        print(f"Goal Reached in {i} steps!")
        break
        
    # Move
    direction = (target_pos - robot_pos) / dist_to_goal # Normalizing
    robot_pos += direction * step_size
    
    print(f"Step {i}: Pos={robot_pos.round(2)} | Dist={dist_to_goal:.2f}")
    time.sleep(0.1)