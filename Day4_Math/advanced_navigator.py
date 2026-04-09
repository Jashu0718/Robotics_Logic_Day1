import numpy as np

class AutonomousBot:
    def __init__(self, start_pos):
        self.pos = np.array(start_pos, dtype=float)
        self.boundary_x = 8.0 # Robot cannot pass X = 8.0
        
    def move_with_safety(self, target):
        # Calculate movement vector
        direction = target - self.pos
        step = direction / np.linalg.norm(direction) * 1.5 # 1.5m step
        
        # Add 'Sensor Noise' (Standard deviation of 0.05)
        noise = np.random.normal(0, 0.05, size=2)
        next_step = self.pos + step + noise
        
        # Safety Check: Geofencing
        if next_step[0] > self.boundary_x:
            print(f"⚠️ SAFETY ALERT: Boundary at {self.boundary_x} reached! Stopping.")
            return False
        
        self.pos = next_step
        print(f"Robot moved to: {self.pos.round(2)}")
        return True

# Simulation
my_bot = AutonomousBot([0, 0])
goal = np.array([10, 0])

for i in range(10):
    if not my_bot.move_with_safety(goal):
        break