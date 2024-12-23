import sys
import logging
import os
from src.logger import logging
#sys is used to store any exceptional 
def error_message_detail(error, error_detail:sys):
    #error_details is a function in exc_info , it gives three thing, first 2 things are not needed
    #gives line number:
    _,_,exc_tb=error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))
    return error_message
# when we are doing a project, it is dynamic so in order to not do changes in code regularly we use OOPS

class CustomException(Exception):
    #exception is inherited, so we have to use super() to access it
    #Making a constructor
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

   
