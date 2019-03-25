#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='alphabot2',
      version='0.0.1',
      description='clients package for controlling alphabot2',
      author='Yap Seng Kuang',
      author_email='skyap79@hotmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )