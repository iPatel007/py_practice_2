from sklearn.preprocessing import StandardScaler
from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
from dataclasses import dataclass
import os
import pandas as pd
import numpy as np
import sys


@dataclass
class DataTransformationConfig:
    prerocessor_obj_file_path = os.path.join('artifacts', "preprocessor_obj.pkl")

class DataTransformation:
    def __init__(self):
        self.data_config = DataTransformationConfig()

    def init_data_transformation(self, train_file_path, test_file_path):
        try:
            logging.info("DataTransformation object started")
            
            print(train_file_path)
            print(test_file_path)
            X_train = pd.read_csv(train_file_path)
            X_test = pd.read_csv(test_file_path)
            
            

            # Remove % in the Change column
            X_train['Change'] = X_train['Change %'].str.replace('%', '')
            X_test['Change'] = X_test['Change %'].str.replace('%', '')
            X_train['Change'] = X_train['Change'].astype(float)
            X_test['Change'] = X_test['Change'].astype(float)

            # Remove % in the Change column
            X_train.drop(columns=['Change %'], inplace=True, axis=1)
            X_test.drop(columns=['Change %'], inplace=True, axis=1)


            # Split Date column to Day, Month and Year
            X_train['Day'] = X_train['Date'].map(lambda x: x.split('-')[0])
            X_train['Month'] = X_train['Date'].map(lambda x: x.split('-')[1])
            X_train['Year'] = X_train['Date'].map(lambda x: x.split('-')[2])

            X_test['Day'] = X_test['Date'].map(lambda x: x.split('-')[0])
            X_test['Month'] = X_test['Date'].map(lambda x: x.split('-')[1])
            X_test['Year'] = X_test['Date'].map(lambda x: x.split('-')[2])
            
            # Drop the Date column
            X_train.drop(columns=['Date'], axis=1, inplace=True)
            X_test.drop(columns=['Date'], axis=1, inplace=True)
            
            for col in X_train.columns:
                if X_train[col].dtype == 'object':
                    X_train[col] = pd.to_numeric(X_train[col], errors='coerce').fillna(0).astype(int)

            for col in X_test.columns:
                if X_test[col].dtype == 'object':
                    X_test[col] = pd.to_numeric(X_test[col], errors='coerce').fillna(0).astype(int)                    

            # Drop the target variable
            X_train_final = X_train.drop(columns=['Low'], axis=1)
            y_train = X_train['Low']

            X_test_final = X_test.drop(columns=['Low'], axis=1)
            y_test = X_test['Low']

            # Standardize the data
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train_final)
            X_test_scaled = scaler.transform(X_test_final)

            # Save the preprocessor object
            X_train_arry = np.c_[X_train_scaled, np.array(y_train)]
            X_test_arry = np.c_[X_test_scaled, np.array(y_test)]

            logging.info("DataTransformation Finished")

            return (X_train_arry, X_test_arry)

        except Exception as e:
            raise CustomException(e, sys)