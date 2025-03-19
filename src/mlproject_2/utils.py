from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
import sys
import os
import pandas as pd
import pickle


def read_data():
    try:
        logging.info("Reading data from DataFrame")
        df = pd.read_csv("/Users/ipatel/Documents/Amit/Python/Practice/p2/csv/deliveries.csv")
        return df
    except Exception as e:
        raise CustomException(e, sys)
    

def save_model_trainer_obj(model, model_file_path):
    try:
        print('model_file_path:', model_file_path)  
        
        logging.info("Saving the model")
        dir_path = os.path.dirname(model_file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(model_file_path, 'wb') as file_obj:
            pickle.dump(model, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
        