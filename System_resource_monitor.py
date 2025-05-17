import psutil

cpu_usage = print(psutil.cpu_percent(interval=10))
print(cpu_usage)

ram_usage = print(psutil.virtual_memory())
print(ram_usage)

disk_usage = print(psutil.disk_usage('/'))
print(disk_usage)


# system_monitor.py from chatgpt

import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Get RAM usage
ram = psutil.virtual_memory()
print(f"RAM Usage: {ram.percent}% (Used: {ram.used / (1024 ** 3):.2f} GB / Total: {ram.total / (1024 ** 3):.2f} GB)")

# Get Disk usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}% (Used: {disk.used / (1024 ** 3):.2f} GB / Total: {disk.total / (1024 ** 3):.2f} GB)")
