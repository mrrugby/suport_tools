import psutil
import time

#threshold limit for warmings

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print("WARNING: High CPU usage detected!")
        
def check_memory():
    memory_info = psutil.virtual_memory()
    print(f"Memory usage : {memory_info.percent}%")
    if memory_info.percent > MEMORY_THRESHOLD:
        print("WARNING: Hight memory usage detected!")
        
def check_disk():
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")
    if disk_usage.percent > DISK_THRESHOLD:
        print("Warning: Low disk space detected!")
        
def check_network():
    net_io = psutil.net_io_counters()
    print(f"Network - Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB, Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

def system_health_check():
    print("\n--- System Health Check ---")
    check_cpu()
    check_memory()
    check_disk()
    check_network()
    print("--------------------------\n")
    
while True:
    system_health_check()
    time.sleep(10)