import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
from geopy.distance import geodesic
from datetime import datetime, timedelta


class BusPrediction:
    def __init__(self):
        self.model = self._build_model()
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.005)

    def _build_model(self):
        model = nn.LSTM(input_size=2, hidden_size=128, num_layers=3, batch_first=True)
        return nn.Sequential(model, nn.Linear(128, 2))

    def train(self, df):
        lat_lng = df[["Latitude", "Longitude"]].values
        sequence_length = 5
        X, y = [], []
        for i in range(len(lat_lng) - sequence_length):
            X.append(lat_lng[i:i + sequence_length])
            y.append(lat_lng[i + sequence_length][:2])
        X, y = np.array(X), np.array(y)
        X_train = torch.tensor(X, dtype=torch.float32)
        y_train = torch.tensor(y, dtype=torch.float32)

        for epoch in range(500):  # Reduced epochs for efficiency
            self.optimizer.zero_grad()
            output = self.model(X_train)
            loss = self.criterion(output, y_train)
            loss.backward()
            self.optimizer.step()

    def predict(self, sequence):
        self.model.eval()
        sequence_tensor = torch.tensor([sequence], dtype=torch.float32)
        with torch.no_grad():
            prediction = self.model(sequence_tensor).numpy()
        return tuple(prediction[0])


def calculate_error(predicted, actual):
    return geodesic((predicted[0], predicted[1]), (actual[0], actual[1])).meters


def simulate_bus_movement(df, loops=1):
    current_time = datetime.now()
    simulated_data = []
    for _ in range(loops):
        for i in range(len(df) - 1):
            lat1, lon1 = df.iloc[i]["Latitude"], df.iloc[i]["Longitude"]
            lat2, lon2 = df.iloc[i + 1]["Latitude"], df.iloc[i + 1]["Longitude"]
            distance = geodesic((lat1, lon1), (lat2, lon2)).meters
            speed = 10  # Assume constant speed of 10 m/s
            time_per_step = 1  # 1 second per step
            num_steps = max(1, int(distance / speed))
            for step in range(num_steps + 1):
                fraction = step / num_steps
                lat = lat1 + fraction * (lat2 - lat1)
                lon = lon1 + fraction * (lon2 - lon1)
                current_time += timedelta(seconds=time_per_step)
                simulated_data.append([current_time, lat, lon])
    return pd.DataFrame(simulated_data, columns=["Timestamp", "Latitude", "Longitude"])



