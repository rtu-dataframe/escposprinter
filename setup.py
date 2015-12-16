#!/usr/bin/python

from distutils.core import setup

setup(
    name='escposprinter',
    version='2.2',
    url='https://github.com/Simonefardella/escposprinter',
    download_url='https://github.com/Simonefardella/escposprinter/archive/master.zip',
    description='Python library to manipulate ESC/POS Printers with support for python >= 3',
    long_description=open('README.txt').read(),
    license='LGPL',
    author=['Simone Fardella'],
    author_email=['fardella93@gmail.com'],
    platforms=['linux'],
    packages=[
        'escposprinter',
    ],
    install_requires=[
        'pyusb',
        'Pillow>=2.0',
        'qrcode>=4.0',
        'pyserial',
    ],
)
