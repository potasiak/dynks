#!/usr/bin/env python
from setuptools import setup

with open('README.rst') as readme_file:
    long_description = readme_file.read()

docs_require = ['sphinx']
tests_require = ['pytest']

setup(
    name='dynks',
    version='1.0.b',

    packages=['dynks'],

    tests_require=tests_require,
    extras_require={
        "docs": docs_require,
        "dev": docs_require + tests_require + ['pytest-runner'],
    },
    python_requires='>=3.6',

    author='Sebastian Potasiak',
    author_email='sebastian@potasiak.dev',
    description=(
        'A collection of various Python utilities that make software '
        'developer\'s life easier.'
    ),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='MIT License',
    url='https://github.com/potasiak/dynks',
    project_urls={
        'Bug Tracker': '',
        'Documentation': '',
        'Source Code': '',
    },
    keywords=[
        'utilities', 'utility', 'utils', 'util', 'ordering', 'order',
        'ordered', 'sorting', 'sort', 'sorted',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    zip_safe=True,
)

