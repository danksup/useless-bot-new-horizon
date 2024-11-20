import psutil
import platform
import cpuinfo
import subprocess
import re

async def get_bot_info() -> str:
    bot_name = "multilinear"
    bot_id = "727842349094535248"
    bot_version = "sus"
    bot_author = "multilinear"

    cpu_info = cpuinfo.get_cpu_info()
    cpu_name = cpu_info['brand_raw']
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_temp = None

    battery_info = {}

    if platform.system() == "Darwin":
        try:
            output = subprocess.check_output(["ioreg", "-r", "-k", "Temperature", "StateOfCharge", "CurrentCapacity", "IsCharging", "CycleCount", "DesignCapacity"]).decode("utf-8")

            temp_matches = re.findall(r'"Temperature" = (\d+)', output)
            if temp_matches:
                cpu_temp = f"{float(temp_matches[0]) / 100:.1f} °C"

            state_of_charge_matches = re.findall(r'"StateOfCharge" = (\d+)', output)
            current_capacity_matches = re.findall(r'"CurrentCapacity" = (\d+)', output)
            is_charging_matches = re.findall(r'"IsCharging" = (Yes|No)', output)
            cycle_count_matches = re.findall(r'"CycleCount" = (\d+)', output)
            design_capacity_matches = re.findall(r'"DesignCapacity" = (\d+)', output)

            battery_info['StateOfCharge'] = state_of_charge_matches[0] if state_of_charge_matches else "N/A"
            battery_info['CurrentCapacity'] = current_capacity_matches[0] if current_capacity_matches else "N/A"
            battery_info['IsCharging'] = is_charging_matches[0] if is_charging_matches else "N/A"
            battery_info['CycleCount'] = cycle_count_matches[0] if cycle_count_matches else "N/A"
            battery_info['DesignCapacity'] = design_capacity_matches[0] if design_capacity_matches else "N/A"

        except Exception as e:
            cpu_temp = "Could not retrieve temperature"
            battery_info = "Could not retrieve battery information"

    virtual_memory = psutil.virtual_memory()
    memory_total = virtual_memory.total / (1024 ** 3)
    memory_available = virtual_memory.available / (1024 ** 3)
    memory_used = virtual_memory.used / (1024 ** 3)
    memory_percentage = virtual_memory.percent

    disk_usage = psutil.disk_usage('/')
    disk_total = disk_usage.total / (1024 ** 3)
    disk_used = disk_usage.used / (1024 ** 3)
    disk_free = disk_usage.free / (1024 ** 3)
    disk_percentage = disk_usage.percent

    os_info = platform.platform()

    response = (
        f"**Bot Information**\n"
        f"Name: {bot_name}\n"
        f"ID: {bot_id}\n"
        f"Version: {bot_version}\n"
        f"Author: {bot_author}\n\n"
        f"**OS Information**\n"
        f"{os_info}\n\n"
        f"**CPU Information**\n"
        f"Name: {cpu_name}\n"
        f"Cores: {cpu_cores}\n"
        f"Threads: {cpu_threads}\n"
        f"Usage: {cpu_usage}%\n"
        f"Temperature: {cpu_temp if cpu_temp else 'N/A'}\n\n"
        f"**Memory Information**\n"
        f"Total: {memory_total:.2f} GB\n"
        f"Used: {memory_used:.2f} GB\n"
        f"Available: {memory_available:.2f} GB\n"
        f"Usage: {memory_percentage}%\n\n"
        f"**Disk Information**\n"
        f"Total: {disk_total:.2f} GB\n"
        f"Used: {disk_used:.2f} GB\n"
        f"Free: {disk_free:.2f} GB\n"
        f"Usage: {disk_percentage}%\n\n"
        f"**Battery Information**\n"
        f"Current Capacity: {battery_info.get('CurrentCapacity', 'N/A')} %\n"
        f"Is Charging: {battery_info.get('IsCharging', 'N/A')}\n"
        f"Cycle Count: {battery_info.get('CycleCount', 'N/A')}\n"
        f"Design Capacity: {battery_info.get('DesignCapacity', 'N/A')} mAh\n"
    )

    return response
