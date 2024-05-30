print("hii app file")
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("The Execution has been  started ")
    print("hii app file")
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    
    