import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class ChessPredictor:
    def __init__(self, data):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = ['player_rating', 'opponent_rating', 'is_white']
        self.X = pd.DataFrame({
            'player_rating': data['brengall99_rating'],
            'opponent_rating': data['opponent_rating'],
            'is_white': (data['white_username'] == 'brengall99').astype(int)
        })
        
        self.y = (data['game_outcome'] == 'Win').astype(int) # target vector
        
        # train the model if we haven't already
        if not self.model:
            self.train_model() 
    
    def train_model(self):
        """Train the model on the provided data."""
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        
        X_train_scaled = X_train.copy()
        X_test_scaled = X_test.copy()
        
        rating_columns = ['player_rating', 'opponent_rating']
        X_train_scaled[rating_columns] = self.scaler.fit_transform(X_train[rating_columns])
        X_test_scaled[rating_columns] = self.scaler.transform(X_test[rating_columns])
        
        self.model = LogisticRegression(random_state=42)
        self.model.fit(X_train_scaled, y_train)
        
        # optionally print evaluation metrics here
        # self.print_evaluation(X_test_scaled, y_test)
    
    def predict_probability(self, player_rating, opponent_rating, is_white):
        """Predict the probability of winning a chess game."""
        if not self.model:
            raise ValueError("Model has not been trained.")
        
        scaled_ratings = self.scaler.transform([[player_rating, opponent_rating]])
        features = np.array([[scaled_ratings[0,0], scaled_ratings[0,1], int(is_white)]])
        
        features_df = pd.DataFrame(features, columns=self.feature_names)
        return self.model.predict_proba(features_df)[0][1]
    
    # optionally: evaluate model performance
    # def print_evaluation(self, X_test, y_test):
    #     print("\nModel Evaluation:")
    #     print("-----------------")
    #     y_pred = self.model.predict(X_test)
    #     print(f"Test Set Accuracy: {accuracy_score(y_test, y_pred):.2%}")
    #     print("\nClassification Report:")
    #     print(classification_report(y_test, y_pred))