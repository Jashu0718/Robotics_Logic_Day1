# 🤖 Jash-Botics: Autonomous State Monitor (Day 1)

## 📌 Project Overview
This project is the foundation of a modular control system for autonomous robotics. It is designed to monitor mechanical health (vibration and battery levels) using a decoupled architecture, ensuring scalability and ease of maintenance in production environments.

### 🛠️ Tech Stack
- **OS:** Ubuntu 24.04 (WSL2)
- **Language:** Python 3.10+
- **Environment:** VS Code (Remote-WSL)
- **Version Control:** Git/GitHub

## 🚀 Key Features
* **Modular Architecture:** Separates hardware logic (`robot_actions.py`) from the execution hub (`main_controller.py`).
* **Real-time Telemetry Logging:** Implements a persistent "Black Box" recorder (`telemetry.log`) for post-operation analysis.
* **Fault Tolerance:** Uses robust error handling to prevent system crashes during invalid sensor inputs.
* **Memory Management:** Utilizes FIFO buffers to track historical sensor trends.

## 📁 File Structure
- `main_controller.py`: The central nervous system that processes user/sensor input.
- `robot_actions.py`: The utility library containing safety thresholds and battery calculations.
- `telemetry.log`: A persistent record of all system events.

## 🔧 How to Run (Linux/Ubuntu)
1. Clone the repo: `git clone [YOUR_URL]`
2. Navigate to directory: `cd Robotics_Logic_Day1`
3. Run the controller: `python3 main_controller.py`
4. Monitor logs live: `tail -f telemetry.log`

## Day 2: Industrial Data Reliability & Scaling
Focused on making the robot logic "Indestructible" and preparing for fleet-level monitoring.

### Key Milestones:
- **Error Handling:** Implemented `try/except` blocks to catch invalid sensor inputs, preventing system crashes during runtime.
- **Data Structures:** Utilized **Dictionaries** to manage complex robot states (ID, Battery, Temperature, Vibration).
- **Fleet Management:** Developed a "Fleet Manager" using **Lists of Dictionaries** to monitor multiple robots simultaneously.
- **Automated Alert System:** Created a logic gate that triggers an alert and logs data to `fleet_alerts.txt` when a robot's temperature exceeds 100°C.

### Skills Gained:
- Version Control (Resolving Git Pull/Push conflicts).
- File I/O (Persistent logging for telemetry).
- State Management (Using dictionaries to track machine health).
## Day 3: Object-Oriented Robotics & System Architecture
Today’s focus was transitioning from procedural scripting to Object-Oriented Programming (OOP), mimicking how production-level robotics software (like ROS) is structured.

### Key Milestones
Class Architecture: Designed a master Robot blueprint to manage state (battery, status, model) and behavior through encapsulated methods.

Inheritance & Polymorphism: Developed a specialized Drone subclass that inherits core telemetry logic from the base Robot class while implementing unique aerial behaviors (fly method).

Integrated Telemetry (The "Black Box"): * Wired a persistent logging system directly into the Class methods.

Every robot action (tasks, movement, errors) is automatically timestamped and recorded to individual .txt telemetry files.

Industrial Safety Logic: Implemented a global emergency_shutdown protocol to safely terminate processes across different robot types.

Timezone Synchronization: Resolved Linux/Python system discrepancies by implementing a manual IST (India Standard Time) offset for accurate data auditing.

### Technical Stack
Language: Python 3.10+

OOP Concepts: Classes, Objects, __init__, self, Inheritance, Method Overriding.

Modules: datetime (for temporal data tracking), os (for file management).

Environment: Ubuntu (WSL/Linux) & Git Version Control.

### Project Structure
Day3_OOP/
├── robot_class.py        # Core OOP fundamentals and methods
├── fleet_ops.py          # Polymorphism and multi-robot management
└── integrated_fleet.py    # Production-grade logging and error handling
# Robotics Software Engineering Journey 🤖

This repository tracks my transition from Mechanical Engineering to Robotics Software Development. It documents my daily progress in Python, C++, and Autonomous Systems.

## 🚀 Progress Log

### **Day 4: Mathematical Foundations & Navigation**
* **Vector Mathematics:** Implemented distance calculation and vector normalization using NumPy.
* **Coordinate Geometry:** Mastered rotation matrices and heading calculations using `atan2`.
* **Linear Controller:** Built a script to move a robot from Point A to Point B with overshoot prevention.

### **Day 5: Telemetry, Noise, and Waypoint Navigation**
* **Sensor Simulation:** Implemented Gaussian (White) Noise to simulate real-world sensor inaccuracies.
* **Data Visualization:** Integrated `Matplotlib` to plot planned vs. actual robot trajectories.
* **Waypoint Mission:** Developed a "Square Patrol" algorithm allowing the robot to visit a sequence of coordinates autonomously.
* **Telemetry Logging:** Created a system to record and analyze "Mission Data" (total distance, mean error, and path efficiency).

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** NumPy (Math), Matplotlib (Visualization)
* **Environment:** Ubuntu (WSL2), VS Code, Git
* **Hardware Context:** Insights applied from experience with Hyundai CAS Design and FANUC Robot Programming.

## 📈 Next Milestones
- [ ] **Day 6:** PID Control (Proportional-Integral-Derivative) for smooth acceleration.
- [ ] **Day 7:** Introduction to ROS2 (Robot Operating System) nodes.