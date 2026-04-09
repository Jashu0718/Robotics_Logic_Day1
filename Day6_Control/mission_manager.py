import numpy as np
import matplotlib.pyplot as plt
import os

class RobotDriver:
    """The 'Muscles' - Handles PID and Physics"""
    def __init__(self, kp, kd, mass):
        self.kp = kp
        self.kd = kd
        self.mass = mass
        self.pos = np.array([0.0, 0.0])
        self.vel = np.array([0.0, 0.0])
        self.prev_error = np.array([0.0, 0.0])
        self.dt = 0.1

    def move_step(self, target):
        error = target - self.pos
        
        # Derivative (Change in error)
        derivative = (error - self.prev_error) / self.dt
        
        # PD Control Output (Force)
        force = (self.kp * error) + (self.kd * derivative)
        
        # Physics: a = F/m
        accel = force / self.mass
        self.vel += accel * self.dt
        self.pos += self.vel * self.dt
        
        self.prev_error = error
        return self.pos.copy()

class MissionControl:
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.history = []

    def run_mission(self, driver):
        for target in self.waypoints:
            target = np.array(target)
            print(f"Mission: Targeting Waypoint {target}")
            
            for step in range(600): # Increased steps for smoother arrival
                new_pos = driver.move_step(target)
                self.history.append(new_pos)
                
                # --- SAFETY GUARDRAIL ---
                # If robot goes more than 0.5m past any boundary, Kill Task
                if new_pos[0] > 10.5 or new_pos[1] > 10.5 or new_pos[0] < -0.5 or new_pos[1] < -0.5:
                    print("⚠️ EMERGENCY STOP: OVERSHOOT DETECTED!")
                    return # Exit the entire mission

                # Arrival Logic: Must be close AND almost stopped
                dist = np.linalg.norm(target - new_pos)
                speed = np.linalg.norm(driver.vel)
                
                if dist < 0.1 and speed < 0.05:
                    print(f"Waypoint {target} secured.")
                    # Reset internal error to prevent "Integral Windup"
                    driver.prev_error = np.array([0.0, 0.0])
                    break

# --- Execution ---
wps = [[10, 0], [10, 10], [0, 10], [0, 0]]
my_driver = RobotDriver(kp=0.2, kd=2.5, mass=1.0) # Using your tuned values
mission = MissionControl(wps)

mission.run_mission(my_driver)

# --- Visualization ---
data = np.array(mission.history)
plt.figure(figsize=(8,8))
plt.plot(data[:,0], data[:,1], 'g-', label="Managed Trajectory")
plt.scatter([w[0] for w in wps], [w[1] for w in wps], c='red')
plt.title("Modular Mission Management System")
plt.grid(True)
plt.savefig("managed_mission.png")
print("Mission Complete. Visual saved.")