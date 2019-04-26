#!/usr/bin/env python
from distutils.core import setup

setup(
    name='numpy2gif',
    version='1.0',
    author='Andreas Bunkahle',
    author_email='abunkahle@t-online.de',
    description='Convert single and multiple numpy images to a gif image without PIL or pillow',
    license='BSD 3',
    py_modules=['numpy2gif'],
    python_requires='>=2.7',
    url='https://github.com/bunkahle/numpy2gif',
    long_description=open('README.txt').read(),
    platforms = ['any'],
    install_requires=['numpy'],
    keywords = 'GIF Converter from Numpy to GIF',
    classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'],
)
