from src.exception import CustomException
import os 
import sys
from src.logger import logging
def test():
    try:
        logging.info("error of division by 0")
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)




if __name__ == "__main__":

    #the above line sets the module
    #prevents excecution on import
    try:
        test()
    except Exception as e:
        print(e)


