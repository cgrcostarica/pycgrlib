from setuptools import setup, find_packages

setup(
    name='pycgrlib',
    version='0.1.2',
    url='https://github.com/cgrcr/pycgrlib.git',
    description='Libreria de funciones para uso de herramientas en la Contraloria General de la Republica (CGR)',
    author='Mario Zamora Madriz',
    author_email='mario.andres.zamora@cgr.go.cr',
    package_dir = {"": "src"},
    packages=find_packages(),
    install_requires=['pandas'],
)