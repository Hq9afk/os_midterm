import joblib
from utils.preprocessing import preprocess_for_prediction

TASK_TYPE_MAP = {
    "image_processing": 0,
    "data_analysis": 1,
    "network_request": 2,
    "machine_learning": 3
}
PRIORITY_MAP = {
    "low": 0,
    "medium": 1,
    "high": 2
}

def encode_input( priority: str):
    return  PRIORITY_MAP.get(priority, 1)

def load_model(path="model/model.pkl"):
    return joblib.load(path)

def predict(task_type: str, cpu: float, mem: float, io: float, duration: float, priority: str):
    model = load_model()
    priority_enc = encode_input(priority)
    input_vector = [task_type, cpu, mem, io, duration, priority_enc]
    return model.predict([input_vector])[0]


def predict_from_csv(input_path, output_path, model_path='model/model.pkl'):
    X, df = preprocess_for_prediction(input_path)  # Lấy cả X và df gốc

    model = joblib.load(model_path)
    predictions = model.predict(X)

    df['predicted_allocation'] = predictions
    df.to_csv(output_path, index=False)
