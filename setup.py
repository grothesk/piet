from setuptools import setup, find_packages

import piet


setup(
    name='piet',
    version=piet.__version__,
    packages=find_packages(),
    description='piet ist eine Tool-Sammlung',
    author='Malte Groth',
    author_email='malte.groth@gmx.net',
    install_requires=[],
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
