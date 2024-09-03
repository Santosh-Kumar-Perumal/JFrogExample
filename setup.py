# setup.py
from setuptools import setup, find_packages

setup(
    name="jfrog-example-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Dependencies go here (optional)
    ],
    entry_points={
        'console_scripts': [
            'jfrog-example-app=app:main',
        ],
    },
)
