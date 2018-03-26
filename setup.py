# -*- coding: utf-8 -*-
"""
Наш кривой скрипт установки.
"""
from distutils.core import setup

from setuptools import find_packages

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='smeshnyavka-matrix-bot',
    version='0.0.0.1',
    description='Постит смешнявки с башорга по команде.',
    long_description=readme,
    author='saber-nyan',
    author_email='saber-nyan@ya.ru',
    url='https://github.com/saber-nyan/smeshnyavka-matrix-bot',
    license='WTFPL',
    install_requires=[
        'matrix_bot_api',
        'requests',
    ],
    packages=find_packages(),
    include_package_data=True
)
