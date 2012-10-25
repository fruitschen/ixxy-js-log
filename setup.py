from setuptools import find_packages
from setuptools import setup

setup(name='django-js-log',
      version='0.1',
      description='A Django app that logs JavaScript errors',
      author='Andy Baker, fruitschen',
      packages=find_packages(),
      include_package_data=True,      
)
