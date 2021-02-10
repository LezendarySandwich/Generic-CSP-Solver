from setuptools import setup
import os

REQUIRES_PYTHON = ">=3.0.0"
here = os.path.abspath(os.path.dirname(__file__))
CSP_Solver_path = os.path.join(here, 'CSP_Solver')

try:
    with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
        REQUIRED = f.read().split("\n")
except:
    REQUIRED = []

PACKAGES = ['CSP_Solver']

for folder in os.listdir(CSP_Solver_path):
    path = os.path.join(CSP_Solver_path, folder)
    if os.path.isdir(path): PACKAGES.append(f'{PACKAGES[0]}.{folder}')

with open("README.md", "r") as fh:
    long_description = fh.read()

short_description = 'Library to solve Constraint satisfation problems'

setup(
    name='CSP_Solver',
    version='0.1.2',
    author='Sanskar Mani',
    author_email='mani.1@iitj.ac.in',
    packages=PACKAGES,
    install_requires=REQUIRED,
    description=short_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LezendarySandwich/Generic-CSP-Solver',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=REQUIRES_PYTHON,
)
