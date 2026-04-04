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
