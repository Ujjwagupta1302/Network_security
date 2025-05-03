'''
by writing setup.py my 
Project becomes a proper python package.
setup.py file helps in packaging and distributing python projects.
It is used by setuptools to define the configuration of my project, such as its metadata, dependencies and more
'''




from setuptools import find_packages,setup
# find_packages -> it searches all the folders, and wherever it finds the 
# __init__.py, it considers it as a package. 
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements 
    that are needed by all the packages in our project
    '''
    requirement_lst:List[str] = [] 
    try:
        with open('requirements.txt','r') as file :
            # Read lines from file 
            lines = file.readlines() 
            # Process each line 
            for line in lines:
                requirement = line.strip() # removing empty spaces from every line that we are getting.
                ## ignore empty line and ignore -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement) 

    except FileNotFoundError:
        print("requirements.txt file not found") 

    return requirement_lst

# it contains all the details of my project packages and dependencies
# that will automatically get installed when someone installs or uses my project as a package.
setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Ujjwal Gupta",
    author_email = "ujjwalgupta1302@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements() 
)