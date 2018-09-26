# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import find_packages, setup


def get_packages_from_pipfile():
    """Return package names from Pipfile."""
    with open('Pipfile', 'r') as f:
        content = f.read()
    packages = []
    extract_line = False
    for line in content.split('\n'):
        if line == '[packages]':
            extract_line = True
            continue
        if line == '':
            extract_line = False
            continue
        if extract_line:
            package_name = line.split(' ')[0]
            packages.append(package_name)
    return packages


setup(
    name='sit',
    version='0.0.1',
    description='SI timesheets',
    url='https://github.com/dtgoitia/si-timesheets',
    author='David Torralba Goitia',
    author_email='david.torralba.goitia@gmail.com',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
    keywords=['timesheets'],
    install_requires=get_packages_from_pipfile(),
    entry_points={
        'console_scripts': [
            'sit=sit.__main__:main'
        ]
    }
)
