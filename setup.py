#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages
try:
    import incolumepy.curso_flask_rizza as package
except (ImportError, ModuleNotFoundError):
    import src.incolumepy.curso_flask_rizza as package


NAME = package.__package__
NAMESPACE = NAME.split('.')[:-1]
DESCRIPTION = "package incolumepy {}".format(NAME)
KEYWORDS = 'python incolumepy {}'.format(NAME)
AUTHOR = '@britodfbr'
AUTHOR_EMAIL = 'contato@incolume.com.br'
URL = F'https://gitlab.com/development-incolume/{NAME}/'
PROJECT_URLS = {
    'Documentation': F'https://gitlab.com/development-incolume/{NAME}/',
    'Funding': None,
    'Say Thanks!': None,
    'Source': F'https://gitlab.com/development-incolume/{NAME}',
    'Git': F'https://gitlab.com/development-incolume/{NAME}.git',
    'Tracker': F'https://gitlab.com/development-incolume/{NAME}/issues',
    'Oficial': '',
}
LICENSE = 'BSD'

# Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Natural Language :: Portuguese (Brazilian)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities']

VERSION = package.__version__

with open('README.md') as f:
    readme = f.read()
with open(os.path.join('docs', 'HISTORY.rst')) as f:
    history = f.read()
with open(os.path.join('docs', 'EXAMPLES.rst')) as f:
    examples = f.read()

LONG_DESCRIPTION = '\n\n'.join((readme, history, examples))

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    project_urls=PROJECT_URLS,
    license=LICENSE,
    namespace_packages=NAMESPACE,
    packages=find_packages('src', exclude=['testes', 'exemplos']),
    package_dir={'': 'src'},
    test_suite='nose.collector',
    tests_require='nose',
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        # 'pytest',
        'nose',
    ],
    entry_points={
        'console_scripts': [
            'interval = incolumepy.checkinterval.Check:Check.interval'
        ],
        'gui_scripts': [
            'baz = my_package_gui:start_func',
        ],
    },
    # -*-Data files-*-
    include_package_data=True,
    exclude_package_data={'': ['saj_projects']},
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        # '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'data': ['data/*.cvs', 'data/*.xlsx'],
        # 'drivers': ['drivers/*']
    },
    dependency_links=[
        "http://peak.telecommunity.com/snapshots/"
    ],
    # entry_points="""
    # -*- Entry points: -*-

    # [distutils.setup_keywords]
    # paster_plugins = setuptools.dist:assert_string_list
    # [egg_info.writers]
    # paster_plugins.txt = setuptools.command.egg_info:write_arg
    # """,
    # paster_plugins = [''],
)
