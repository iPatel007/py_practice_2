import os
import sys
from dataclasses import dataclass
from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from src.mlproject_2.utils import save_model_trainer_obj

@dataclass
class ModelTrainerConfig:
    model_obj_file_path = os.path.join('artifacts', "model_obj.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_config = ModelTrainerConfig()

    def init_model_trainer(self, X_train, X_test):
        try:
            logging.info("ModelTrainer object started")

            # Split the data into X_train, y_train, X_test, y_test
            X_train, y_train, X_test, y_test = [
                X_train[:, :-1],
                X_train[:, -1],
                X_test[:, :-1],
                X_test[:, -1],
            ]

            # Train the model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Make predictions
            y_pred = model.predict(X_test)

            # Calculate and print the accuracy score
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            print(f'Mean Squared Error: {mse}')
            print(f'R^2 Score: {r2}')

            # Save the model
            logging.info("Save model trainer object as model_obj.pkl")

            save_model_trainer_obj(model, self.model_config.model_obj_file_path)

            # Finish the ModelTrainer
            logging.info("Finish the ModelTrainer") 
            
    
        except Exception as e:
            raise CustomException(e, sys)
                