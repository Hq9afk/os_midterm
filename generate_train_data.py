import psutil
import csv
import os
import time


def get_priority(proc):
    try:
        nice = proc.nice()
        if nice < 0:
            return "high"
        elif nice == 0:
            return "medium"
        else:
            return "low"
    except Exception:
        return "unknown"


def get_resource_allocated(proc):
    # Placeholder: you can customize this based on your needs
    return "high" if get_priority(proc) == "high" else "medium"


if __name__ == "__main__":
    output = "data/train_data.csv"
    file_exists = os.path.isfile(output)
    with open(output, mode="a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(["task_type", "cpu_usage", "mem_usage", "io_usage", "duration", "priority", "resource_allocated"])
        for proc in psutil.process_iter(["name", "cpu_percent", "memory_percent", "io_counters", "create_time", "nice"]):
            try:
                name = proc.info["name"] or "unknown"
                cpu = proc.cpu_percent(interval=0.1)
                mem = proc.memory_percent()
                io = proc.info["io_counters"].read_bytes + proc.info["io_counters"].write_bytes if proc.info["io_counters"] else 0
                # Normalize IO usage to a percentage (example, you can adjust)
                io_usage = min(int(io / (1024 * 1024)), 100)
                duration = int(time.time() - proc.info["create_time"]) if proc.info["create_time"] else 0
                priority = get_priority(proc)
                resource_allocated = get_resource_allocated(proc)
                writer.writerow([name, int(cpu), int(mem), io_usage, duration, priority, resource_allocated])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
    print(f"Process metrics appended to {output}")
