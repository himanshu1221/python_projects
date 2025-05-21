import psutil

cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}% (Used: {memory.used / (1024 ** 3):.2f} GB / Total: {memory.total / (1024 ** 3):.2f} GB)")


for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
    print(f"Process ID: {proc.info['pid']}, Name: {proc.info['name']}, CPU Usage: {proc.info['cpu_percent']}%, Memory Usage: {proc.info['memory_info'].rss / (1024 ** 2):.2f} MB")