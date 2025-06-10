import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os


def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)

    if df["task_type"].dtype == object:
        df["task_type"] = df["task_type"].astype("category").cat.codes
    if df["priority"].dtype == object:
        df["priority"] = df["priority"].astype("category").cat.codes

    X = df[["task_type", "cpu_usage", "mem_usage", "io_usage", "duration", "priority"]]
    y = df["resource_allocated"]

    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_and_save_model():
    x_train, x_test, y_train, y_test = load_and_preprocess("data/input_data.csv")
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    print("=== Evaluation on Test Set ===")
    print(classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    print("✅ Model saved at model/model.pkl")


if __name__ == "__main__":
    train_and_save_model()
