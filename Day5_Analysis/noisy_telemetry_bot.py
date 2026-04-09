import numpy as np
import matplotlib.pyplot as plt

class StressTestBot:
    def __init__(self, start_pos):
        self.pos = np.array(start_pos, dtype=float)
        self.history = [self.pos.copy()]
        
    def move(self, target, noise_level):
        target = np.array(target, dtype=float)
        print(f"Moving toward {target} with Noise Level: {noise_level}")
        
        # Hard limit of 100 steps to prevent infinite loops in high noise
        steps = 0
        while np.linalg.norm(target - self.pos) > 0.5 and steps < 100:
            dist = np.linalg.norm(target - self.pos)
            step_size = min(1.0, dist)
            direction = (target - self.pos) / dist
            
            # 1. Ideal movement
            ideal_step = direction * step_size
            
            # 2. Add Extreme Noise (Standard Deviation = 1.0)
            noise = np.random.normal(0, noise_level, size=2)
            
            self.pos += ideal_step + noise
            self.history.append(self.pos.copy())
            steps += 1

# 1. Initialize
bot = StressTestBot([0, 0])

# 2. Outbound Journey (High Noise)
bot.move([10, 10], noise_level=0.6) 

# 3. Return to Base (Lower Noise)
print("\nGoal reached. Returning to Base...")
bot.move([0, 0], noise_level=0.1)

# 4. Visualization
path = np.array(bot.history)
plt.figure(figsize=(10, 10))

# Plot the whole trajectory
plt.plot(path[:, 0], path[:, 1], 'b-o', markersize=3, alpha=0.6, label='Robot Trajectory')

# Mark key locations
plt.plot(0, 0, 'gs', markersize=10, label='Base (Home)')
plt.plot(10, 10, 'rx', markersize=10, label='Target Goal')

plt.title("Full Mission: Outbound (Extreme Noise) vs. Return (Low Noise)")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)

plt.savefig("stress_test_mission.png")
print("\nMission Map Saved as 'stress_test_mission.png'")