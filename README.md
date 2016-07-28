#Python wrapper for Gnuplot

Author: Ben Schneider

###Requires:
Gnuplot
Python modules: numpy, subprocess

###Installation:
Mac/Unix
		./install

Windows
		install.bat

or
		python setup.py install

###Example 1:
    import PyGnuplot as gp
    import numpy as np
    X = np.arange(10)
    Y = np.sin(X/(2*np.pi))
    Z = Y**2.0
    gp.s([X,Y,Z])  # saves data into tmp.dat
    gp.c('plot "tmp.dat" u 1:2 w lp)  # send 'plot instructions to gnuplot'
    gp.c('replot "tmp.dat" u 1:3' w lp)
    gp.p('myfigure.ps')  # creates postscript file


###Example 2:
example.py 

![example](https://cloud.githubusercontent.com/assets/4573907/17227765/2bfa344e-5510-11e6-908b-38c490ad597f.png)


##Functions:

c(command)
	pipe a command to gnuplot

	example:
	c('plot sin(x)')

	# (tell gnuplot to plot sin(x))

s(data, filename='tmp.dat')
	save arrays into file easily read by Gnuplot
	Existing file would be overwritten

	example:
	s([X,Y,Z])

	# (creates tmp.dat file)

	c('plot "tmp.dat" u 1:2')
	# (whould then plot the data )

p(filename='tmp.ps', width=14, height=9, fontsize=12, term='x11')
	Gnuplot script to print the output
	Existing file would be overwritten

	example:
	p('myfile.ps')

	# (creates postscript file myfile.ps)

pdf(filename='tmp.pdf', width=14, height=9, fontsize=12, term='x11'):
	similar to p, but created pdf files instead.

	example
	pdf('myfile.pdf')

	# (creates pdf file myfile.pdf)
