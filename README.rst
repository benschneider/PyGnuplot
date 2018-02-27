.. image:: https://badge.fury.io/py/PyGnuplot@2x.svg
    :target: https://badge.fury.io/py/PyGnuplot

.. image:: https://anaconda.org/benschneider/pygnuplot/badges/version.svg
    :target: https://anaconda.org/benschneider/pygnuplot

.. image:: https://travis-ci.org/benschneider/PyGnuplot.svg?branch=master
    :target: https://travis-ci.org/benschneider/PyGnuplot

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/benschneider/PyGnuplot/blob/master/LICENSE


PyGnuplot: Python wrapper for Gnuplot
-------------------------------------

Author: Ben Schneider

Requires:
.........
Gnuplot (http://www.gnuplot.info)

numpy 

Installation:
.............

Using pip

.. code::
        
        pip install PyGnuplot

Using conda

.. code::

        conda install -c benschneider pygnuplot

Upgrade:
........
.. code::

        pip install --upgrade  PyGnuplot

Functions:
..........

**c(command)**

  pipe a command to gnuplot as if in gnuplot command promt

.. code:: python

	c('plot sin(x)')

**s(data, filename='tmp.dat')**

  save arrays into file (filename = 'tmp.dat') easily read by Gnuplot

.. code:: python

	s([X,Y,Z])  # creates tmp.dat


.. code:: python

	c('plot "tmp.dat" u 1:2')

**plot(data, filename='tmp.dat')**
  
  Plot some data.
  Saves data into filename (default = 'tmp.dat') and then sends plot instructions to Gnuplot

.. code:: python

        plot([x,y])

**figure(number=None, term='x11')**
  
  Create a new or update a figure

.. code:: python
        
        figure(1)

**p(filename='tmp.ps', width=14, height=9, fontsize=12, term='x11')**

  Create postscript file (overwrites existing)

.. code:: python

	p('myfile.ps')


**pdf(filename='tmp.pdf', width=14, height=9, fontsize=12, term='x11')**

  Create a pdf file (overwrites existing)

.. code:: python

	pdf('myfile.pdf')


Setup terminal
..............

   Default terminal is 'x11' unless defined otherwise i.e. for windows:

.. code:: python

    import PyGnuplot as gp
    gp.default_term = 'wxt'


Examples:
.........

* 1 Example code

.. code:: python

    import PyGnuplot as gp
    import numpy as np
    X = np.arange(10)
    Y = np.sin(X/(2*np.pi))
    Z = Y**2.0
    gp.s([X,Y,Z])
    gp.c('plot "tmp.dat" u 1:2 w lp)
    gp.c('replot "tmp.dat" u 1:3' w lp)
    gp.p('myfigure.ps')


* 2 Example file

.. code::
        
        python example.py 

+-----------------------------------------------------------------------------------------------------------------+
|.. figure:: https://cloud.githubusercontent.com/assets/4573907/17233530/e4be9342-5530-11e6-9c71-e812a2fb4000.png |
+-----------------------------------------------------------------------------------------------------------------+
