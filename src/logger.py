import logging 
import os
import sys
from datetime import datetime
#we don't want to give a name to the log_file so we used datetime.now function to save the name as time when it was ran, and then sonverted to string
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#joining
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#made a directory when it doesn't exist
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #s : to print in string
    #d : to print line number in form of digit
    level=logging.INFO,


)

