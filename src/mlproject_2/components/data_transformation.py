import os
import sys
import pandas as pd
from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    prerocessor_obj_file_path = os.path.join('artifacts', "preprocessor_obj.pkl")

class DataTransformation:
    def __init__(self):
        self.data_config = DataTransformationConfig()

    def get_data_transformation(self, X_train, X_test):
        try:
            logging.info("DataTransformation object started")

            # Preprocess the data
            

        except Exception as e:
            raise CustomException(e, sys.exc_info())