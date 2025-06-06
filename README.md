# AI Task Resource Allocator

A system based on a machine learning model (Decision Tree) to predict the required resource level (low / medium / high) for each AI task, helping to allocate resources efficiently in an operating system or cloud environment.

---

## 📁 Project Structure

```
ai_task_allocator/
├── data/
│   ├── iuput_data.csv           # Iutput data
│   ├── ouput_data.csv           # Output data
│   └── train_data.csv           # Training data
├── model/
│   ├── train_model.py           # Model training
│   ├── predictor.py             # Single and CSV prediction
│   └── model.pkl                # Saved model
├── utils/
│   └── preprocessing.py         # Data processing functions
├── test/
│   └── test_prediction.py       # Quick test
├── generate_input_data.py       # Collect tasks metrics
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

### 🔹 Step 0: Collect task metrics

```bash
python generate_input_data.py
```
- Task metrics are used as input data for AI model
- Data saved to `data/input_data.csv`
### 🔹 Step 1: Train the Model

```bash
python model/train_model.py
```

- Reads data from `data/train_data.csv`
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
python -c "from model import predictor; predictor.predict_from_csv('data/input_data.csv', 'data/output.csv')"
```

- Prints results to terminal
- Writes to `data/output.csv` 

---

### 🔹 Step 4: Quick Test

```bash
python test/test_prediction.py
```

- Runs a sample example to check the system
- Prints result to screen

---

## 🧪 Sample Data (`train_data.csv`)

```csv
task_type,cpu_usage,mem_usage,io_usage,duration,priority,resource_allocated
System Idle Process,2094,0,0,0,unknown,medium
System,16,0,100,8126,low,medium
unknown,0,0,0,8127,low,medium
Registry,0,0,100,8128,low,medium
smss.exe,0,0,0,8126,low,medium
svchost.exe,0,0,0,8123,low,medium
...
```

---

## 📌 Notes

- Tasks are automatically encoded using an internal mapping table.
- Can be extended to other models such as Random Forest, Logistic Regression.
- Suitable for OS environments, container schedulers, or cloud resource planners.

---

## 👥 Team Members

- **Member 1**: Preprocessing & workload monitoring system  
  - Built the workload simulation module
  - Collected system resource usage data using `psutil`
  - Created workload input for the AI model.

- **Member 2**: AI model training  
  - Designed and trained the prediction model using Random Forest
  - Handled data splitting, training, evaluation, and model saving.

- **Member 3**: Integration & testing  
  - Integrated the AI model with the system
  - Implemented `main.py` to process CSV input and write predictions. 
  - Performed functional testing.

- **Member 4**: Report & presentation  
  - Wrote project documentation, testing reports, and created presentation slides. 
  - Participated in overall testing.
