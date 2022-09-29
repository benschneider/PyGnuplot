try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='PyGnuplot',
      py_modules=['PyGnuplot'],
      version='0.12.3',
      license='MIT',
      description='Python Gnuplot wrapper',
      long_description=long_description,
      author='Ben Schneider',
      author_email=' ',
      url='https://github.com/benschneider/PyGnuplot',
      download_url='https://github.com/benschneider/PyGnuplot/archive/0.12.3.tar.gz',
      keywords=['gnuplot', 'plot'],
      classifiers=["Topic :: Scientific/Engineering",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Development Status :: 4 - Beta"],
      )
