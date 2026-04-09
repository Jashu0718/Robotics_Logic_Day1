import numpy as np
import matplotlib.pyplot as plt

class PatrolBot:
    def __init__(self, start_pos):
        self.pos = np.array(start_pos, dtype=float)
        self.history = [self.pos.copy()]
        
    def move_to_waypoint(self, target):
        target = np.array(target, dtype=float)
        while np.linalg.norm(target - self.pos) > 0.3:
            dist = np.linalg.norm(target - self.pos)
            step_size = min(1.0, dist)
            direction = (target - self.pos) / dist
            
            # Add a small amount of realism (noise)
            noise = np.random.normal(0, 0.1, size=2)
            
            self.pos += (direction * step_size) + noise
            self.history.append(self.pos.copy())

# 1. Define the Square Waypoints
# (0,0) -> (10,0) -> (10,10) -> (0,10) -> (0,0)
waypoints = [
    [10, 0],   # Corner 1
    [10, 10],  # Corner 2
    [0, 10],   # Corner 3
    [0, 0]     # Back Home
]

bot = PatrolBot([0, 0])

# 2. Execute the Patrol
print("Starting Square Patrol...")
for point in waypoints:
    print(f"Navigating to Waypoint: {point}")
    bot.move_to_waypoint(point)

# 3. Plot the Result
path = np.array(bot.history)
plt.figure(figsize=(8, 8))
plt.plot(path[:, 0], path[:, 1], 'b-o', markersize=3, label='Patrol Path')

# Mark the waypoints for clarity
for point in waypoints:
    plt.plot(point[0], point[1], 'rs') # Red squares at corners

plt.title("Autonomous Square Patrol Simulation")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid(True)
plt.legend()

plt.savefig("square_patrol.png")
print("\nPatrol Complete. Open 'square_patrol.png' to see the track.")