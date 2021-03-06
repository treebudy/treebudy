#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = ['pytest']

setup(
    name='treebudy',
    version='0.1.0',
    description="a set of Mapping and Sequence objects that keep references to their parent container.",
    long_description=readme + '\n\n' + history,
    author="Bryce DeAlessio",
    author_email='brycevtr250@gmail.com',
    url='https://github.com/drafter250/treebudy',
    packages=[
        'treebudy',
    ],
    package_dir={'treebudy':
                 'treebudy'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='treebudy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
