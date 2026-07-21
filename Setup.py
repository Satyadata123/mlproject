from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirments(file : str) -> List[str]:
    """
    this fuction will return list of requirments
    """
    
    requirments = []
    with open(file) as file_obj:
        requirments = file_obj.readlines() 
        requirments = [req.replace("\n", "") for req in requirments]
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments

setup(
name = "mlproject",
version= '0.0.1',
author = "Satyam singh",
author_email ='ss8919134@gmail.com',
packages= find_packages(),
install_requires= get_requirments('requirments.txt')

)