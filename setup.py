# setup.py

from setuptools import setup, find_packages

setup(
    name='addrexr',
    version='0.1.0',
    description='A regex search tool for identifying crypto addresses and smart contracts.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Knot Here',
    author_email='your_email@example.com',
    url='https://github.com/Knot-Here/addrexr',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

