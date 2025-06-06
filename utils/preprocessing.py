import pandas as pd

def preprocess_for_prediction(filepath):
    df = pd.read_csv(filepath)

    if df['task_type'].dtype == object:
        df['task_type'] = df['task_type'].astype('category').cat.codes
    if df['priority'].dtype == object:
        df['priority'] = df['priority'].astype('category').cat.codes

    x = df[['task_type', 'cpu_usage', 'mem_usage', 'io_usage', 'duration', 'priority']]
    return x, df

