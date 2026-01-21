# Cloud VM Health Monitoring System (Python)

This project is a beginner-to-intermediate level cloud monitoring simulation
developed using Python. It is designed to demonstrate basic cloud VM health
monitoring concepts such as resource usage tracking and system status evaluation.

---

## 🔹 Project Overview
The script continuously monitors:
- CPU usage
- Memory (RAM) usage
- Disk usage

Based on defined thresholds, it determines whether the system is in a
**HEALTHY** or **WARNING** state. All monitoring data is logged with timestamps.

---

## 🔹 Features
- Real-time CPU, RAM, and Disk monitoring
- Threshold-based health status detection
- Timestamped logging to a file
- Continuous monitoring with auto-refresh

---

## 🔹 Technologies Used
- Python 3
- psutil library
- Basic Linux/OS resource concepts

---

## 🔹 How to Run
1. Install Python 3
2. Install dependencies:
   ```bash
   pip install psutil
# Run the script
python monitor.py
