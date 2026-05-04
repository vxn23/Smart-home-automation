import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import os

class SmartModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        self.train()

    def train(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "data.csv")

        data = pd.read_csv(file_path)

        X = data[["Time", "Temperature", "Motion"]]
        y = data["Device"]

        self.model.fit(X, y)

    def predict(self, time, temp, motion):
        return self.model.predict([[time, temp, motion]])[0]
print("Model loaded")