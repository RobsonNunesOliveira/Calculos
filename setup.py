from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Calculos",
    version="0.0.1",
    author="Robson",
    author_email="my_email",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RobsonNunesOliveira/Calculos",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)

""" Comandos de instalação
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools


Comandos para criar distribuições
OBS: PRECISA FAZER A INSTALAÇAO DO PACOTE WHEEL ANTES (pip install wheel), senão vai dar comando inválido 
no terminal.
python setup.py sdist bdist_wheel """