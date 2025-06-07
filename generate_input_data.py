import psutil
import csv
import os
import time

# --- Cấu hình ngưỡng phân loại ---
THRESHOLDS = {
    "cpu_high": 60,
    "mem_high": 60,
    "io_high": 40,
    "net_high": 50,         # KB/s
    "gpu_all_high": 60,      # CPU, MEM, IO >= 40
}

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
    return "high" if get_priority(proc) == "high" else "medium"

def classify_task_type(cpu, mem, io, net):
    # Network-bound
    if net >= THRESHOLDS["net_high"]:
        return "Network-bound"
    # GPU-bound (deep learning, xử lý song song)
    if cpu >= THRESHOLDS["gpu_all_high"] and mem >= THRESHOLDS["gpu_all_high"] and io >= THRESHOLDS["gpu_all_high"]:
        return "GPU-bound"
    # CPU-bound
    if cpu >= THRESHOLDS["cpu_high"] and mem < 50 and io < 30:
        return "CPU-bound"
    # I/O-bound
    if io >= THRESHOLDS["io_high"] and cpu < 50:
        return "I/O-bound"
    # Memory-bound
    if mem >= THRESHOLDS["mem_high"] and cpu < 50:
        return "Memory-bound"
    return "Unknown"

if __name__ == "__main__":
    output = "data/train_data.csv"
    file_exists = os.path.isfile(output)

    # --- Thu thập tài nguyên mạng toàn hệ thống ---
    net_start = psutil.net_io_counters()
    time.sleep(1)  # để đo tốc độ mạng trong khoảng 1 giây
    net_end = psutil.net_io_counters()
    net_bytes = (net_end.bytes_sent + net_end.bytes_recv) - (net_start.bytes_sent + net_start.bytes_recv)
    net_usage = int(net_bytes / 1024)  # KB/s

    with open(output, mode="a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow([
                "task_type", "cpu_usage", "mem_usage", "io_usage",
                "net_usage", "duration", "priority", "resource_allocated"
            ])

        for proc in psutil.process_iter(["name", "cpu_percent", "memory_percent", "io_counters", "create_time", "nice"]):
            try:
                name = proc.info["name"] or "unknown"
                cpu = proc.cpu_percent(interval=0.1)
                mem = proc.memory_percent()
                io_bytes = proc.info["io_counters"].read_bytes + proc.info["io_counters"].write_bytes if proc.info["io_counters"] else 0
                io_usage = min(int(io_bytes / (1024 * 1024)), 100)  # MB
                duration = int(time.time() - proc.info["create_time"]) if proc.info["create_time"] else 0
                priority = get_priority(proc)
                resource_allocated = get_resource_allocated(proc)

                # Phân loại dựa trên thông tin và net_usage toàn hệ thống
                task_type = classify_task_type(cpu, mem, io_usage, net_usage)

                writer.writerow([
                    task_type, int(cpu), int(mem), io_usage,
                    duration, priority, resource_allocated
                ])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    print(f"Process metrics appended to {output}")
