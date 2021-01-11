from distutils.core import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
        REQUIRED = f.read().split("\n")
except:
    REQUIRED = []

REQUIRED.append('CSP_Solver')

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='CSP_Solver',
    version='0.1dev',
    author='Sanskar Mani',
    author_email='mani.1@iitj.ac.in',
    packages=REQUIRED,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LezendarySandwich/Generic-CSP-Solver',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
