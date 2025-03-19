from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
from src.mlproject_2.components.data_ingestion import DataIngestion
from src.mlproject_2.components.data_transformation import DataTransformation
from src.mlproject_2.components.model_tranier import ModelTrainer

import sys

if __name__ == "__main__":
    try:
        logging.info("Starting the main app.py function") 

        # Initialize the data ingestion
        data_ingestion = DataIngestion()
        X_train_file_path, X_test_file_path = data_ingestion.init_data_ingesion()

        # Initialize the data transformation
        data_transformation = DataTransformation()
        X_train_arry, X_test_arry = data_transformation.init_data_transformation(
            X_train_file_path, X_test_file_path)

        # Initialize the model trainer
        model_trainer = ModelTrainer()
        model_trainer.init_model_trainer(X_train_arry, X_test_arry)
    except Exception as e:
        raise CustomException(e, sys)    