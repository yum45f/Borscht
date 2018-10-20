from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="borscht",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    url='https://github.com/yu-san-19/Borscht',
    author='YuSan19',
    author_email='ysoga19@gmail.com',
    description='The Python Module of The japanese sentence generator by markov chain.',
    long_description=readme,
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    long_description_content_type="text/markdown",
    license="Apache-2.0"
)
