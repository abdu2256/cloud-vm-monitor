import psutil
import datetime
import time

log_file = "monitor.log"

while True:
    current_time = datetime.datetime.now()

    cpu = psutil.cpu_percent(interval=2)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu < 70 and memory < 70 and disk < 80:
        status = "HEALTHY"
    else:
        status = "WARNING"

    # Console output
    print("Time:", current_time)
    print("CPU Usage:", cpu, "%")
    print("Memory Usage:", memory, "%")
    print("Disk Usage:", disk, "%")
    print("System Status:", status)
    print("-----------------------------")

    # Log file write
    with open(log_file, "a") as file:
        file.write(
            f"{current_time} | CPU: {cpu}% | RAM: {memory}% | Disk: {disk}% | Status: {status}\n"
        )

    time.sleep(5)
