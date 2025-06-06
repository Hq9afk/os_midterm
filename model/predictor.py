import joblib
from utils.preprocessing import preprocess_for_prediction

def predict_from_csv(input_path, output_path, model_path='model/model.pkl'):
    X, df = preprocess_for_prediction(input_path)  # Lấy cả X và df gốc

    model = joblib.load(model_path)
    predictions = model.predict(X)

    df['predicted_allocation'] = predictions
    df.to_csv(output_path, index=False)
