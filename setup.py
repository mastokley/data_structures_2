# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="data_structures_2",
    description="Implementation of classic data structures using Python classes",
    version=0.1,
    author="Patrick Trompeter and Michael Stokley",
    author_email="",
    license='GPL',
    py_modules={
        "deque",
    },
    package_dir={'': 'src'},
    install_requires=['numpy'],
    extras_require={
        'test': ['pytest', 'tox']
    }
)
