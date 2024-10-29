from setuptools import setup, find_packages

def get_requirements():
    requirements_list = []
    try:
        with open("requirements.txt") as f:
            requirements_list = f.read().splitlines()
            requirements_list = [req for req in requirements_list if req != "-e ."]
    except FileNotFoundError as e:
        raise e
    return requirements_list

PROJECT_NAME = "DocuMate"
AUTHOR_NAME = "Satyam Kumar"
AUTHOR_EMAIL = "sirsatyamchaudhary@gmail.com"
VERSION = "0.1.0"

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements(),
)
