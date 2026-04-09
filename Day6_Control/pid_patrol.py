import numpy as np
import matplotlib.pyplot as plt

class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, current_value, dt):
        error = setpoint - current_value
        self.integral += error * dt
        # Derivative: rate of change of error
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

# 1. Setup Environment
# Tweak these: higher mass = rounder corners | higher kd = sharper corners
mass = 1.0 
dt = 0.1
# Pro-tuning: Lower Kp and higher Kd creates smoother, curved motion

pid_x = PID(kp=0.3, ki=0.0, kd=1.2) # Lower Kp, much higher Kd
pid_y = PID(kp=0.3, ki=0.0, kd=1.2)

pos = np.array([0.0, 0.0])
velocity = np.array([0.0, 0.0])
waypoints = [[10, 0], [10, 10], [0, 10], [0, 0]]
history = [pos.copy()]

# 2. Execute Patrol
for target in waypoints:
    print(f"Navigating to {target}...")
    
    # Give the robot enough time (max steps) to reach each corner
    for step in range(400):
        dist_to_goal = np.linalg.norm(target - pos)
        
        # Stop condition: Close to target AND moving slowly
        if dist_to_goal < 0.2 and np.linalg.norm(velocity) < 0.1:
            break
            
        # PID calculates 'Force'
        fx = pid_x.compute(target[0], pos[0], dt)
        fy = pid_y.compute(target[1], pos[1], dt)
        force = np.array([fx, fy])

        # Physics: F = ma -> a = F/m
        acceleration = force / mass
        
        # Integration: Force -> Velocity -> Position
        velocity += acceleration * dt
        pos += velocity * dt
        
        history.append(pos.copy())

# 3. Visualization
path = np.array(history)
plt.figure(figsize=(10, 10))

# Plot the smooth path
plt.plot(path[:, 0], path[:, 1], 'b-', linewidth=2, label="PID Trajectory (with Inertia)")

# Plot Waypoints as Red Squares
for i, w in enumerate(waypoints):
    plt.plot(w[0], w[1], 'rs', markersize=8)
    plt.text(w[0]+0.2, w[1]+0.2, f"WP {i+1}", fontsize=12)

plt.title("Advanced Autonomous Patrol: Realistic Physics & PID Control")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal') # Keeps the square shape from looking like a rectangle

plt.savefig("pid_patrol_result.png")
print("Success! Check 'pid_patrol_result.png' in VS Code.")