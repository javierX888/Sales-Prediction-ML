class ModelTrainer:
    def __init__(self, model, scaler):
        self.model = model
        self.scaler = scaler

    def train(self, X_train, y_train):
        X_scaled = self.scaler.transform(X_train)
        self.model.fit(X_scaled, y_train)

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def save_model(self, filepath):
        import joblib
        joblib.dump(self.model, filepath)

    def load_model(self, filepath):
        import joblib
        self.model = joblib.load(filepath)