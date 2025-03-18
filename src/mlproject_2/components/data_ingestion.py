import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
import os
from src.mlproject_2.utils import read_data
import sys
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    main_df_file_path = os.path.join('artifacts', "deliveries_df.csv")
    train_df_file_path = os.path.join('artifacts', "train_df.csv")
    test_df_file_path = os.path.join('artifacts', "test_df.csv")


class DataIngestion:
    def __init__(self):
        self.data_config = DataIngestionConfig()    
    
    def init_data_ingesion(self):        
        try:
            logging.info("DataIngestion object started")
            
            # Load main dataframe
            main_df = read_data()

            # Create the directory if it does not exist and save the main dataframe
            os.makedirs(os.path.dirname(self.data_config.main_df_file_path), exist_ok=True) 

            main_df.to_csv(self.data_config.main_df_file_path, index=False, header=True)

            # Split the data into train and test
            X_train, X_test = train_test_split(main_df, test_size=0.20, random_state=42)

            # Save the train and test dataframes
            X_train.to_csv(self.data_config.train_df_file_path, index=False, header=True)
            X_test.to_csv(self.data_config.test_df_file_path, index=False, header=True)

            return (self.data_config.train_df_file_path, self.data_config.test_df_file_path)

        except Exception as e:            
            raise CustomException(e, sys)

        