"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os, re

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

VERSION_FILE = os.path.join(here, "saambe", "version.py")

def get_version():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.M)
    if not match:
        raise RuntimeError(f"Unable to find version string in {VERSION_FILE}")
    return match.group(1)

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

VERSION_FILE = os.path.join(here, "saambe", "version.py")

def get_version():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.M)
    if not match:
        raise RuntimeError(f"Unable to find version string in {VERSION_FILE}")
    return match.group(1)

setup(
    name='scipion-chem-saambe',  # Required
    version=get_version(),  # Required
    description='Scipion plugin for Alexov group in http://compbio.clemson.edu/lab/',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/scipion-chem/scipion-chem-saambe',  # Optional
    author='Natalia del Rey',  # Optional
    author_email='scipion@cnb.csic.es',  # Optional
    keywords='scipion chemoinformatics',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(),
    install_requires=[requirements],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/scipion-chem/scipion-chem-saambe/issues',
        'Source': 'https://github.com/scipion-chem/scipion-chem-saambe/',
        'Pull Requests': 'https://github.com/scipion-chem/scipion-chem-saambe/pulls'
    },
    entry_points={'pyworkflow.plugin': 'saambe = saambe'},
    package_data={  # Optional
       'saambe': [_logo, 'protocols.conf'],
    }
)
