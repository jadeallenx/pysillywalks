
"""
============
pysillywalks
============

This is an example project for learning about git and python.

**It is very silly**

Installation
============

Use the standard ``python setup.py install``

Quick Usage
===========

The constructor expects the following keyword arguments:

    - **walk**: A string of the walk type or genre
    - **silly**: An integer rating of the silliness level

Example initialization:

    from pysillywalks import Silly

    s = Silly(walk="pirate", silly=2)
    if s.is_very_silly:
        s.action()
    else:
        print "Not silly enough, sorry!"


License
=======
Copyright (c) 2012 Mark Allen

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from distutils.core import setup

setup(author='Mark Allen',
      author_email='mrallen1@yahoo.com',
      description='A very silly library',
      long_description=__doc__,
      fullname='pysillywalks',
      name='pysillywalks',
      url='https://github.com/mrallen1/pysillywalks',
      download_url='https://github.com/mrallen1/pysillywalks',
      version='1.0.0',
      license='MIT',
      platforms=['Linux','Windows'],
      packages=['pysillywalks'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ]
)
