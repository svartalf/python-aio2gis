# -*- coding: utf-8 -*-

"""
python-aio2gis
============

A Python library for accessing the 2gis API via asyncio interface
"""

from setuptools import setup, find_packages


setup(
    name='aio2gis',
    version='0.0.1',
    author='svartalf',
    author_email='self@svartalf.info',
    url='https://github.com/svartalf/python-aio2gis',
    description='asyncio-powered 2gis library for Python',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    install_requires=('aiohttp', ),
    # test_suite='tests',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ),
)
