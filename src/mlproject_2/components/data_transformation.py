import os
import sys
import pandas as pd
from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler

@dataclass
class DataTransformationConfig:
    prerocessor_obj_file_path = os.path.join('artifacts', "preprocessor_obj.pkl")

class DataTransformation:
    def __init__(self):
        self.data_config = DataTransformationConfig()

    def init_data_transformation(self, X_train, X_test):
        try:
            logging.info("DataTransformation object started")

            X_train = pd.read_csv(X_train)
            X_test = pd.read_csv(X_test)

            # Remove % in the Change column
            X_train['Change'] = X_train['Change'].str.replace('%', '')
            X_test['Change'] = X_test['Change'].str.replace('%', '')

            # Split Date column to Day, Month and Year
            X_train['Date'] = pd.to_datetime(X_train['Date'])
            X_train['Day'] = X_train['Date'].dt.day
            X_train['Month'] = X_train['Date'].dt.month
            X_train['Year'] = X_train['Date'].dt.year

            X_test['Date'] = pd.to_datetime(X_test['Date'])
            X_test['Day'] = X_test['Date'].dt.day
            X_test['Month'] = X_test['Date'].dt.month
            X_test['Year'] = X_test['Date'].dt.year

            # Drop the target variable
            X_train = X_train.drop(columns=['Low'])
            y_train = X_train['Low']

            X_test = X_test.drop(columns=['Low'])
            y_test = X_test['Low']

            # Standardize the data
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Save the preprocessor object
            X_train_arry = np.c_[X_train_scaled, np.array(y_train)]
            X_test_arry = np.c_[X_test_scaled, np.array(y_test)]

            return (X_train_arry, X_test_arry)

        except Exception as e:
            raise CustomException(e, sys.exc_info())