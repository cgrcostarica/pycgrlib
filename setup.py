from setuptools import setup, find_packages

setup(
    name='pycgrlib',
    version='0.1.1',
    url='https://github.com/cgrcr/pycgrlib.git',
    description='Biblioteca de funciones útiles de Python para uso de la CGR',
    author='Mario Zamora Madriz',
    author_email='mario.andres.zamora@cgr.go.cr',
    package_dir = {"": "src"},
    packages=find_packages(),
    install_requires=['pandas'],
)