try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='PyGnuplot',
      py_modules=['PyGnuplot'],
      version='0.11.16',
      license='MIT',
      description='Python Gnuplot wrapper',
      long_description=long_description,
      author='Ben Schneider',
      author_email=' ',
      url='https://github.com/benschneider/PyGnuplot',
      download_url='https://github.com/benschneider/PyGnuplot/archive/0.11.16.tar.gz',
      keywords=['gnuplot', 'plot'],
      # install_requires=['numpy'],
      classifiers=["Topic :: Scientific/Engineering",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.6",
                   "Development Status :: 4 - Beta"],
      )
