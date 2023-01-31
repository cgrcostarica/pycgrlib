from setuptools import setup, find_packages
exec(open('src/pycgrlib/_version.py').read())

setup(
    name='pycgrlib',
    version= __version__,
    url='https://github.com/cgrcr/pycgrlib.git',
    description='Libreria de funciones para uso de herramientas en la Contraloria General de la Republica (CGR)',
    author='Mario Zamora Madriz',
    author_email='mario.andres.zamora@cgr.go.cr',
    package_dir = {"": "src"},
    packages=find_packages(),
    install_requires=['pandas','pyodbc'],
)

