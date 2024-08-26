# this setup.py is responsible for install the local packages into the venv
# to install the local packages we do --> pip install -e .

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:
        # Open and read the requirements.txt
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
        
    return requirement_list

print(get_requirements())

setup(
    name="networksecurity",
    version="0.0.1",
    author="aayush garg",
    author_email="aysh.garg2603@gmail.com",
    packages=find_packages(),                   #find_packages() will install the folders containing __init__.py file and save it in the venv folder
    install_requires=get_requirements()
)