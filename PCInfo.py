import psutil
import platform
import os

os.system("cls")

print("System Info Viewer v3.7")
print("")
print("-"*40, "System Info", "-"*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"PC Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

print("-"*40, "CPU Info", "-"*40)
print("Actual Cores:", psutil.cpu_count(logical=False))
print("Logical Cores:", psutil.cpu_count(logical=True))
print(f"Max Frequency: {psutil.cpu_freq().max:.1f}Mhz")
print(f"Current Frequency: {psutil.cpu_freq().current:.1f}Mhz")
print(f"CPU Usage: {psutil.cpu_percent()}%")
print("CPU Usage/Core:")
for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {perc}%")

def adjust_size(size):
    factor = 1024
    for i in [" B", " KB", " MB", " GB", " TB"]:
        if size > factor:
            size = size / factor
        else:
            return f"{size:.3f}{i}"

print("-"*40, "RAM Info", "-"*40)
vm = psutil.virtual_memory()
print(f"Total: {adjust_size(vm.total)}")
print(f"Available: {adjust_size(vm.available)}")
print(f"Used: {adjust_size(vm.used)}")
print(f"Percentage: {vm.percent}")
print("-"*40, "SWAP", "-"*40)
sp = psutil.swap_memory()
print(f"Total: {adjust_size(sp.total)}")
print(f"Free: {adjust_size(sp.free)}")
print(f"Used: {adjust_size(sp.used)}")
print(f"Percentage: {sp.percent}")

print("-"*40, "Disk Info", "-"*40)
par = psutil.disk_partitions()
for p in par:
    print(f"Device: {p.device}")
    print(f"\tMountpoint: {p.mountpoint}")
    print(f"\tFile System Type: {p.fstype}")
    try:
        paru = psutil.disk_usage(p.mountpoint)
    except PermissionError:
        continue
    print(f"\t  Total Size: {adjust_size(paru.total)}")
    print(f"\t  Used: {adjust_size(paru.used)}")
    print(f"\t  Free: {adjust_size(paru.free)}")
    print(f"\t  Percentage: {adjust_size(paru.percent)}%")
diskio = psutil.disk_io_counters()
print(f"Read since boot: {adjust_size(diskio.read_bytes)}")
print(f"Written since boot: {adjust_size(diskio.write_bytes)}")

print("")    
input("Press Enter to close")