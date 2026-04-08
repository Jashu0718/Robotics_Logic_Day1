import datetime # Let's add timestamps like a pro

class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.log_file = f"{self.name}_log.txt"

    # THE POWER MOVE: A method that writes its own logs
    def log_action(self, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {self.name} ({self.model}): {action}\n"
        
        with open(self.log_file, "a") as f:
            f.write(log_entry)
        print(f"Log Updated: {action}")

    def perform_task(self, task):
        print(f"{self.name} is starting task: {task}")
        # Automatically record this to the file!
        self.log_action(f"Started {task}")

# --- Test the Integration ---
factory_bot = Robot("Jash-Arm-01", "Fanuc-Industrial")

factory_bot.perform_task("Welding Chassis")
factory_bot.perform_task("Quality Inspection")