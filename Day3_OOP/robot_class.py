# Jash-Botics Class Architecture v2.0

class Robot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery = battery_level
        self.status = "Idle"

    def report_status(self):
        print(f"--- [{self.name}] Report ---")
        print(f"Status: {self.status} | Battery: {self.battery}%")

    def move(self, distance):
        if self.battery > 10:
            self.status = "Moving"
            drain = distance * 0.5
            self.battery -= drain
            print(f"{self.name} moved {distance}m (Drained {drain}% battery).")
        else:
            self.status = "Power Critical"
            print(f"!!! {self.name}: LOW BATTERY ({self.battery}%) - Movement Blocked !!!")

    # --- YOUR NEW METHOD ---
    def charge(self):
        print(f"\n[SYSTEM] Connecting {self.name} to Power Station...")
        self.battery = 100
        self.status = "Fully Charged"
        print(f"[SYSTEM] {self.name} is now at {self.battery}%. Ready for mission.")

# --- Testing the Logic ---
print("SCENARIO: Deploying Low-Power Robot")
bot2 = Robot("Heavy-Lifter", 15)

# 1. Try to move with low battery
bot2.move(20)
bot2.report_status()

# 2. Fix the issue using the new method
bot2.charge()

# 3. Try to move again
bot2.move(20)
bot2.report_status()
# Drone inherits from Robot
class Drone(Robot):
    def __init__(self, name, battery_level):
        # 'super' pulls in the name and battery logic from the parent Robot class
        super().__init__(name, battery_level)
        self.altitude = 0

    def fly(self, target_alt):
        if self.battery > 20:
            self.altitude = target_alt
            self.status = f"Flying at {self.altitude}m"
            print(f"{self.name} is airborne! Altitude: {self.altitude}m")
        else:
            print(f"{self.name} battery too low for takeoff!")

# Test the Drone
my_drone = Drone("Sky-Scanner", 50)
my_drone.fly(100)
my_drone.report_status() # This still works because it was inherited!