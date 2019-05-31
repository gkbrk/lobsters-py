#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name = "lobsters",
    version = "0.2.1",
    packages = find_packages(),
    install_requires = ['requests>=2.0', 'testsimple>=0.1'],
    url = "https://github.com/gkbrk/lobsters-py",
    author = "Gokberk Yaltirakli",
    author_email = "opensource@gkbrk.com",
    description = "API Client for lobste.rs",
    keywords = "api client lobsters lobste",
    project_urls = {
        'Bug Tracker': 'https://github.com/gkbrk/lobsters-py/issues',
        'Source Code': 'https://github.com/gkbrk/lobsters-py'
    }
)
