import numpy as np
import time

class SmartRobot:
    def __init__(self, name, start_pos):
        self.name = name
        self.pos = np.array(start_pos, dtype=float)
        self.heading = 0.0  # Degrees
        
    def navigate_to(self, target):
        target = np.array(target, dtype=float)
        
        # 1. CALCULATE STEERING
        diff = target - self.pos
        target_angle = np.degrees(np.arctan2(diff[1], diff[0]))
        
        print(f"[{self.name}] Target detected at {target_angle:.2f}°")
        print(f"[{self.name}] Rotating from {self.heading}° to {target_angle:.2f}°...")
        
        self.heading = target_angle # In a real robot, this would take time
        
        # 2. MOVE TO TARGET
        print(f"[{self.name}] Commencing movement...")
        while True:
            dist = np.linalg.norm(target - self.pos)
            
            # 1. Check if we arrived
            if dist <= 0.5:
                self.pos = target # Snap to exact target
                print(f"[{self.name}] Final Position: {self.pos} - MISSION COMPLETE.")
                break
            
            # 2. Prevent overshooting: 
            # If the next step is bigger than the distance, just move the remaining distance
            current_step = min(1.5, dist) 
            
            direction = (target - self.pos) / dist
            self.pos += direction * current_step
            
            print(f"  > Position: {self.pos.round(2)} | Dist: {dist:.2f}m")
            time.sleep(0.1)

# Run the Simulation
bot = SmartRobot("Jash-Bot", [0, 0])
bot.navigate_to([10, 5])