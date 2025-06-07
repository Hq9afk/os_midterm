import joblib
import pandas as pd
from utils.preprocessing import preprocess_for_prediction

TASK_TYPE_MAP = {
    "Network-bound": 0,
    "GPU-bound": 1,
    "CPU-bound": 2,
    "I/O-bound": 3,
    "Memory-bound": 4,
    "Unknown": 5
}

PRIORITY_MAP = {
    "low": 0,
    "medium": 1,
    "high": 2
}

def encode_input(task_type, priority):
    return TASK_TYPE_MAP.get(task_type, 0), PRIORITY_MAP.get(priority, 1)

def load_model(path="model/model.pkl"):
    return joblib.load(path)

def predict(task_type, cpu, mem, io, duration, priority):
    model = load_model()
    task_type_enc, priority_enc = encode_input(task_type, priority)

    input_df = pd.DataFrame([{
        "task_type": task_type_enc,
        "cpu_usage": cpu,
        "mem_usage": mem,
        "io_usage": io,
        "duration": duration,
        "priority": priority_enc
    }])

    return model.predict(input_df)[0]

def predict_from_csv(input_path, output_path, model_path='model/model.pkl'):
    x, df = preprocess_for_prediction(input_path)  # Lấy cả X và df gốc

    model = joblib.load(model_path)
    predictions = model.predict(x)

    df['predicted_allocation'] = predictions
    df.to_csv(output_path, index=False)
