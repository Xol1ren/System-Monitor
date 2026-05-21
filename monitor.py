import os 

pids = []
for pid in os.listdir('/proc'):
    if pid.isdigit():
        try:
            with open(f'/proc/{pid}/comm', 'r') as f:
                name = f.read().strip()
            with open(f'/proc/{pid}/statm', 'r') as f:
                vm_size_pages = int(f.read().split()[0])
            mem_mb = (vm_size_pages * 4096 ) / (1024 * 1024)
            print(f"PID: {pid} | Name: {name} | Memory: {mem_mb:.2f} MB")
        except (FileNotFoundError, PermissionError):
            continue
