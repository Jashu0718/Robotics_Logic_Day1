import numpy as np
import matplotlib.pyplot as plt
import time

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.prev_error = 0
        self.integral = 0

    def update(self, setpoint, measured_value, dt):
        error = setpoint - measured_value
        
        # Proportional
        P = self.kp * error
        
        # Integral (with windup protection)
        self.integral += error * dt
        I = self.ki * self.integral
        
        # Derivative
        derivative = (error - self.prev_error) / dt
        D = self.kd * derivative
        
        self.prev_error = error
        return P + I + D

# --- Simulation: Testing our Controller ---
def simulate_control(kp, ki, kd):
    pid = PIDController(kp, ki, kd)
    pos = 0.0
    target = 10.0
    dt = 0.1
    history = []

    for _ in range(100):
        force = pid.update(target, pos, dt)
        pos += force * dt  # Simplified physics
        history.append(pos)
    
    return history

# Compare Tuning
plt.figure(figsize=(10, 5))
plt.plot(simulate_control(0.5, 0.0, 0.0), label="P-Only (Slow/Steady)")
plt.plot(simulate_control(2.0, 0.0, 0.2), label="PD (Fast/Aggressive)")
# 1. UNDERDAMPED (The "Aggressive" Robot)
# It gets there fast, but it "hunts" for the target.
plt.plot(simulate_control(kp=1.5, ki=0.0, kd=0.1), label="Underdamped")

# 2. OVERDAMPED (The "Lazy" Robot)
# It's safe, but it's too slow for a high-performance environment.
plt.plot(simulate_control(kp=0.2, ki=0.0, kd=0.0), label="Overdamped")

# 3. CRITICALLY DAMPED (The "25 LPA" Pro Robot)
# This is what you're aiming for: Fast but perfectly stable.
plt.plot(simulate_control(kp=0.6, ki=0.0, kd=0.3), label="Critically Damped")
plt.axhline(y=10, color='r', linestyle='--', label="Target")
plt.title("PID Tuning Comparison")
plt.legend()
plt.savefig("pid_test.png")
