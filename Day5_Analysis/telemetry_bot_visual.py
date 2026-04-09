import numpy as np
import matplotlib.pyplot as plt # The new tool

class TelemetryBot:
    def __init__(self, start_pos):
        self.pos = np.array(start_pos, dtype=float)
        self.history = [self.pos.copy()] 
        
    def move(self, target):
        target = np.array(target, dtype=float)
        while np.linalg.norm(target - self.pos) > 0.1:
            dist = np.linalg.norm(target - self.pos)
            # Take a 1m step, but don't overshoot
            step_size = min(1.0, dist)
            step = (target - self.pos) / dist * step_size
            
            self.pos += step
            self.history.append(self.pos.copy())

# 1. Run the Mission
bot = TelemetryBot([0, 0])
bot.move([8, 15]) # Moving to a diagonal target

# 2. Convert history to a NumPy array for easy plotting
path = np.array(bot.history)

# 3. MATPLOTLIB CODE: Create the Graph
plt.figure(figsize=(8, 6))

# Plot the path (X is path[:, 0], Y is path[:, 1])
plt.plot(path[:, 0], path[:, 1], marker='o', color='blue', label='Robot Path')

# Mark the Start and Goal
plt.plot(0, 0, 'gs', label='Start') # Green Square
plt.plot(8, 15, 'rx', label='Goal') # Red X

# Labels and Styling
plt.title("Robot Trajectory Telemetry")
plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")
plt.legend()
plt.grid(True)

# Save the file
plt.savefig("mission_map.png")
print("Mission complete. Graph saved as 'mission_map.png'")