# Jash-Botics Fleet Operations Control

class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
    
    def get_info(self):
        return f"Robot: {self.name} | Power: {self.battery}%"

class Drone(Robot):
    def fly(self):
        return f"{self.name} is now scanning from the air."

class GroundBot(Robot):
    def drive(self):
        return f"{self.name} is moving on tracks."

# --- The Fleet Manager (Using OOP Objects in a List) ---
my_fleet = [
    Drone("Sky-1", 80),
    GroundBot("Rover-1", 45),
    Drone("Sky-2", 15)
]

print("--- DAILY FLEET REPORT ---")
for bot in my_fleet:
    print(bot.get_info()) # Every bot has this from the parent
    
    # Specific actions based on type
    if isinstance(bot, Drone):
        print(bot.fly())
    elif isinstance(bot, GroundBot):
        print(bot.drive())
    print("-" * 20)