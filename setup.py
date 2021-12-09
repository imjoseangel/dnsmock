#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0120

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import codecs
from glob import glob
import os
from os.path import abspath, dirname, normpath
from shutil import rmtree
from setuptools import setup, Command
import dnsmock


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    CLEAN_FILES = ('./build', './dist', './*.pyc',
                   './*.tgz', './*.egg-info', './.pytest_cache',
                   '.benchmarks', './tests/__pycache__',
                   './dnsmock/__pycache__',
                   './__pycache__')

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        here = normpath(abspath(dirname(__file__)))

        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob(os.path.normpath(
                os.path.join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError(
                        f"{path} is not a path inside {here}")
                print(f'removing {os.path.relpath(path)}')
                rmtree(path)


def read(rel_path):

    here = normpath(abspath(dirname(__file__)))

    with codecs.open(os.path.join(here, rel_path), 'r') as fullpath:
        return fullpath.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('VERSION'):
            delim = '?= '
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='dnsmock',
    description='Python custom resolver',
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    version=dnsmock.VERSION,
    keywords='dns resolver socket',
    license='MIT',
    author='Jose Angel Munoz',
    author_email='josea.munoz@gmail.com',
    url='https://github.com/imjoseangel/dnsmock',
    packages=['dnsmock'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
    install_requires=[],
    cmdclass={
        'clean': CleanCommand,
    }
)
