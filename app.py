from src.mlproject_2.logger import logging
from src.mlproject_2.exception import CustomException
from src.mlproject_2.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    try:
        logging.info("Starting the main app.py function") 

        # Initialize the data ingestion
        data_ingestion = DataIngestion()
        data_ingestion.init_data_ingesion()
        
    except Exception as e:
        raise CustomException(e, sys.exc_info())    