# AI Task Resource Allocator

Hệ thống dựa trên mô hình học máy (Decision Tree) để dự đoán mức tài nguyên cần thiết (thấp / trung bình / cao) cho từng tác vụ AI, giúp phân bổ tài nguyên hiệu quả trong môi trường hệ điều hành hoặc cloud system.

---

## 📁 Cấu trúc dự án

```
ai_task_allocator/
├── data/
│   ├── raw_data.csv             # Dữ liệu huấn luyện
│   └── test_tasks.csv           # Dữ liệu test (tùy chọn)
├── model/
│   ├── train_model.py           # Huấn luyện mô hình
│   ├── predictor.py             # Dự đoán đơn lẻ và CSV
│   └── model.pkl                # Mô hình đã lưu
├── utils/
│   └── preprocessing.py         # Hàm xử lý dữ liệu
├── test/
│   └── test_prediction.py       # Kiểm thử nhanh
├── main.py                      # Chạy chương trình CLI
└── README.md                    # Hướng dẫn chạy
```

---

## ⚙️ Yêu cầu môi trường

- Python 3.8+
- Các thư viện:
  ```bash
  pip install pandas scikit-learn joblib
  ```

---

## 🚀 Hướng dẫn chạy chương trình

### 🔹 Bước 1: Huấn luyện mô hình

```bash
python model/train_model.py
```

- Đọc dữ liệu từ `data/raw_data.csv`
- Lưu mô hình vào `model/model.pkl`

---

### 🔹 Bước 2: Dự đoán đơn lẻ (CLI)

```bash
python main.py
```

- Nhập thông tin về task:
  ```
  Loại tác vụ: data_analysis
  CPU usage (%): 50
  Memory usage (%): 40
  I/O usage (%): 30
  Duration (s): 60
  Priority: medium
  ```
- Kết quả:
  ```
  📊 Dự đoán phân bổ tài nguyên: MEDIUM
  ```

---

### 🔹 Bước 3: Dự đoán hàng loạt từ file CSV

```bash
python -c "from model import predictor; predictor.predict_from_csv('data/test_data.csv', 'data/output.csv')"
```

- In kết quả ra terminal
- Ghi vào file `data/output.csv` nếu chỉ định

---

### 🔹 Bước 4: Chạy kiểm thử nhanh

```bash
python test/test_prediction.py
```

- Chạy một ví dụ mẫu để kiểm tra hệ thống
- Kết quả in ra màn hình

---

## 🧪 Dữ liệu mẫu (`raw_data.csv`)

```csv
task_type,cpu_usage,mem_usage,io_usage,duration,priority,resource_allocated
image_processing,70,60,30,45,high,high
data_analysis,40,20,10,60,medium,medium
network_request,50,50,60,30,low,medium
machine_learning,80,70,50,90,high,high
```

---

## 📌 Ghi chú

- Các tác vụ được mã hóa tự động bằng bảng ánh xạ nội bộ.
- Có thể mở rộng sang các mô hình khác như Random Forest, Logistic Regression.
- Thích hợp cho môi trường hệ điều hành, container scheduler hoặc cloud resource planner.

---

## 👨‍💻 Nhóm thực hiện

- Thành viên 1: Huấn luyện & mô hình AI
- Thành viên 2: Tiền xử lý & tích hợp predictor
- Thành viên 3: Giao diện main.py, test, CSV input
- Thành viên 4: Báo cáo, slide, kiểm thử tổng hợp