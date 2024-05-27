from setuptools import find_packages
from setuptools import Extension
from setuptools import setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]

    return requirements



setup(
    name="mplprojects",
    version="0.0.1",
    author="smruti",
    author_email="charmy.smrutidash@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
