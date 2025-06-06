# AI Task Resource Allocator

A system based on a machine learning model (Decision Tree) to predict the required resource level (low / medium / high) for each AI task, helping to allocate resources efficiently in an operating system or cloud environment.

---

## 📁 Project Structure

```
ai_task_allocator/
├── data/
│   ├── raw_data.csv             # Training data
│   └── test_tasks.csv           # Test data (optional)
├── model/
│   ├── train_model.py           # Model training
│   ├── predictor.py             # Single and CSV prediction
│   └── model.pkl                # Saved model
├── utils/
│   └── preprocessing.py         # Data processing functions
├── test/
│   └── test_prediction.py       # Quick test
├── main.py                      # CLI program
└── README.md                    # User guide
```

---

## ⚙️ Environment Requirements

- Python 3.8+
- Libraries:
  ```bash
  pip install pandas scikit-learn joblib
  ```

---

## 🚀 How to Run

### 🔹 Step 1: Train the Model

```bash
python model/train_model.py
```

- Reads data from `data/raw_data.csv`
- Saves the model to `model/model.pkl`

---

### 🔹 Step 2: Single Prediction (CLI)

```bash
python main.py
```

- Enter task information:
  ```
  Task type: data_analysis
  CPU usage (%): 50
  Memory usage (%): 40
  I/O usage (%): 30
  Duration (s): 60
  Priority: medium
  ```
- Result:
  ```
  📊 Predicted resource allocation: MEDIUM
  ```

---

### 🔹 Step 3: Batch Prediction from CSV

```bash
python -c "from model import predictor; predictor.predict_from_csv('data/test_data.csv', 'data/output.csv')"
```

- Prints results to terminal
- Writes to `data/output.csv` if specified

---

### 🔹 Step 4: Quick Test

```bash
python test/test_prediction.py
```

- Runs a sample example to check the system
- Prints result to screen

---

## 🧪 Sample Data (`raw_data.csv`)

```csv
task_type,cpu_usage,mem_usage,io_usage,duration,priority,resource_allocated
image_processing,70,60,30,45,high,high
data_analysis,40,20,10,60,medium,medium
network_request,50,50,60,30,low,medium
machine_learning,80,70,50,90,high,high
```

---

## 📌 Notes

- Tasks are automatically encoded using an internal mapping table.
- Can be extended to other models such as Random Forest, Logistic Regression.
- Suitable for OS environments, container schedulers, or cloud resource planners.

---

## 👨‍💻 Team Members

- Member 1: AI training & modeling
- Member 2: Preprocessing & predictor integration
- Member 3: main.py interface, test, CSV input
- Member 4: Report, slides, overall testing