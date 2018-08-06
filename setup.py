# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import find_packages, setup

setup(
    name='sit',
    version='0.0.1',
    description='SI timesheets',
    url='https://github.com/dtgoitia/si-timesheets',
    author='David Torralba Goitia',
    author_email='david.torralba.goitia@gmail.com',
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    keywords=['timesheets'],
    entry_points={
        'console_scripts': [
            'sit=sit.__main__:main'
        ]
    },
    install_requires=[
        'openpyxl',
        # 'click',
    ]
)
