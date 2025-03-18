from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
import sys
import os
import pandas as pd

def read_data():
    try:
        logging.info("Reading data from DataFrame")
        df = pd.read_csv("/Users/ipatel/Documents/Amit/Python/Practice/p2/src/mlproject_2/cvs/deliveries.csv")
        return df
    except Exception as e:
        raise CustomException(e, sys.exc_info())