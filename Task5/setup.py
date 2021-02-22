from setuptools import setup

setup(
    name='pytest plugin',
    version='0.1.0',
    description='A pytest plugin to generate a CSV report',
    author='TSV',
    py_modules=['pytest plugin'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['testplan=pytest plugin', ]}
)
