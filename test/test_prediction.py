from model import predictor

def test_prediction():
    task = {
        "task_type": "data_analysis",
        "cpu": 50,
        "mem": 30,
        "io": 20,
        "duration": 45,
        "priority": "medium"
    }

    result = predictor.predict(
        task["task_type"],
        task["cpu"],
        task["mem"],
        task["io"],
        task["duration"],
        task["priority"]
    )

    print(f"✔ Dự đoán mức phân bổ cho '{task['task_type']}': {result.upper()}")

if __name__ == "__main__":
    test_prediction()
