import pandas as pd

from api.prediction import BusPrediction, simulate_bus_movement

predictor = BusPrediction()

def train_model():
    df = pd.read_csv("data/sample_bus_data.csv")
    df.columns = df.columns.str.strip()
    df_simulated = simulate_bus_movement(df)
    predictor.train(df_simulated)
    return "Model trained successfully."

def predict_next(data):
    sequence = data[:5]
    return predictor.predict(sequence)

# Example Django usage:
# Call `train_model()` to train using simulated data
# Call `predict_next(list_of_coordinates)` to get a prediction