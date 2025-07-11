from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'
def get_requirements(filepath:str)-> List[str]:
    
    requirements=[]
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
            
    return requirements

setup(
    name='Student Performance Indicator Project',
    version='0.0.1',
    author = "Prathap",
    email = "vprathap2004@gmail.com",
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt')
)