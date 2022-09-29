.. image:: https://badge.fury.io/py/PyGnuplot@2x.svg
    :target: https://badge.fury.io/py/PyGnuplot

.. image:: https://anaconda.org/benschneider/pygnuplot/badges/version.svg
    :target: https://anaconda.org/benschneider/pygnuplot

.. image:: https://travis-ci.org/benschneider/PyGnuplot.svg?branch=experimental
    :target: https://travis-ci.org/benschneider/PyGnuplot

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/benschneider/PyGnuplot/blob/master/LICENSE


PyGnuplot: Python wrapper for Gnuplot
-------------------------------------

Author: Ben Schneider

Requires:
.........
Gnuplot (http://www.gnuplot.info)

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

Basic Usage:
............
.. code::

        from PyGnuplot import gp
        figure1 = gp()  # Create a new figure handle
        figure2 = gp(r"C:\Program Files\gnuplot\bin\gnuplot.exe")  # Can also specify which gnuplot to use
        figure1.a("plot sin(x)")
        figure2.a("plot cos(x)")
        pi = figure.a("print pi")


Functions available with each figure:
.....................................

**c(command)**

pipe a command to gnuplot as if in gnuplot command promt

.. code:: python

	c('plot sin(x)')

**save(data, filename='tmp.dat')**

save arrays into file (filename = 'tmp.dat') easily read by Gnuplot

.. code:: python

	s([X,Y,Z])  # creates tmp.dat


.. code:: python

	c('plot "tmp.dat" u 1:2')

**a(command='', vtype=str, timeout=0.05)**

   asks gnuplot: it sends a command to gnuplot and returns its response
   This is paricularly handy when using gnuplots fitting features
   vtype can be used to change the return format
   timeout is the time to wait for a response 

.. code:: python

      a('print pi')  # returns the value of pi

.. code:: python

      a('print pi; print pi')  # returns 2 times the value of pi

**r(vtype=str, timeout=0.05)**

   reads the gnuplot return buffer until its empty


**plot(data, filename='tmp.dat')**
  
  Plot some data. 
  Sends plot instructions and the data to Gnuplot

.. code:: python

        plot([x,y])

**plot_b(data, v1='d', v2='%double')**

   Similar to plot:
   Sends plot instructions and the data to Gnuplot
   However it sends them in binary format,
   which can be beneficial when the dealing with larger quanities of numbers

**p(filename='tmp.ps', width=14, height=9, fontsize=12, term='x11')**

Create postscript file (overwrites existing)

.. code:: python

	p('myfile.ps')


**pdf(filename='tmp.pdf', width=14, height=9, fontsize=12, term='x11')**

Create a pdf file (overwrites existing)

.. code:: python

	pdf('myfile.pdf')


**quit()**

   Closes windows,then  gnuplot, then the pipe

Setup terminal
..............

   This script will use the same default terminal that gnuplot used
   (it reads the GPVAL_TERM value when gnuplot starts up)
   it can still be modified by the 'default_term' variable:


.. code:: python

    from PyGnuplot import gp
    fig1 = gp()
    fig1.default_term = 'wxt'


New features:
.............


**fit2d(data, func='y(x)=a + b*x', via='a,b', limit=1e-9)**

    Quickly Fit a simple 2-D data set and return the fitting results.
    This uses the new ask function "a()"
    Here we gather the fitting info from gnuplot

and:

**fit(self, data, func='y(x)=a + b*x', via='a,b', limit=1e-9, filename='tmp.dat', wait=1)**

    Allows for sligtly more complex fitting, 
    filename: stores data first into a temporary file default: tmp.dat
    wait: define a waiting time in sec for gnuplot to finish its fitting default: 1sec

.. code:: python

    import numpy as np
    f1 = gp()
    x = np.linspace(0, 20, 1001)
    yn = np.random.randn(1001)/10
    y = np.sin(x)
    data = [x, y+yn]
    func = 'y(x) = a + b*cos(x + c)'  # define a fitting function here.
    (a, b, c), report = f1.fit2d(data, func, via='a,b,c', limit=1e-9) # sending in the data the function used to fit and the variables that are to be found.
    f1.save(data, "tmp.dat")
    f1.a('plot "tmp.dat" w lp')
    f1.a('replot y(x)')

+-----------------------------------------------------------------------------------------------------------------+
|.. figure:: https://user-images.githubusercontent.com/4573907/193154658-92513c20-ab3c-4b29-b487-d98b79d85942.png |
+-----------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------+
|.. figure:: https://user-images.githubusercontent.com/4573907/193154419-133761a1-3e2f-4c00-87d2-2c47b7da62c5.png |
+-----------------------------------------------------------------------------------------------------------------+

Examples:
.........

* 1 Example code

.. code:: python

    from PyGnuplot import gp
    import numpy as np
    X = np.arange(10)
    Y = np.sin(X/(2*np.pi))
    Z = Y**2.0
    fig1 = gp()
    fig1.save([X,Y,Z])
    fig1.c('plot "tmp.dat" u 1:2 w lp)
    fig1.c('replot "tmp.dat" u 1:3' w lp)
    fig1.p('myfigure.ps')


* 2 Example file

.. code::
        
        python example.py 

+-----------------------------------------------------------------------------------------------------------------+
|.. figure:: https://cloud.githubusercontent.com/assets/4573907/17233530/e4be9342-5530-11e6-9c71-e812a2fb4000.png |
+-----------------------------------------------------------------------------------------------------------------+
