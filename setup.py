from pip.req import parse_requirements
from setuptools import setup

setup(
    name='adventofcode-maubry',
    install_reqs=parse_requirements('requirements.txt', session='hack')
)
