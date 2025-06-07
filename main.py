from model import predictor

def main():
    print("🔧 Nhập thông tin tác vụ:")
    task_type = input("Loại tác vụ (CPU-bound / IO-bound / ...): ").strip()
    cpu = float(input("CPU usage (%): "))
    mem = float(input("Memory usage (%): "))
    io = float(input("I/O usage (%): "))
    duration = float(input("Duration (s): "))
    priority = input("Priority (low / medium / high): ").strip()

    result = predictor.predict(task_type, cpu, mem, io, duration, priority)
    print(f"\n📊 Dự đoán phân bổ tài nguyên: {result.upper()}")

if __name__ == "__main__":
    main()
