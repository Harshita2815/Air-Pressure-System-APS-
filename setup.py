from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function reads the requirements.txt file and returns a list of requirements.
    """
    requirement_list: List[str] = []
    try:
        with open(file_path, 'r') as file:
            requirement_list = file.read().splitlines()
            # Remove any empty strings or "-e ." entries
            requirement_list = [req for req in requirement_list if req and req.strip() != '-e .']
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return requirement_list
    """

    This function will return list of requirements
    
    requirement_list:List[str] = []

    
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    
    return requirement_list """
 
setup(
    name='mlproject',
    version='0.0.1',
    author='Harshita',
    author_email='harshitaprakash2815@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    #['pymongo[srv]==4.2.0','pandas','numpy','scikit-learn','pymongo','python-dotenv','PyYAML','dill','scipy','imblearn==0.0']
    #install_requires=get_requirements('requirements.txt')







)