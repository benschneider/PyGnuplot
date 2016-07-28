'''
By Ben Schneider

creates a pip using subprocess to gnuplot (requires gnuplot to be installed)

gp is used to send commands to gnuplot.
Example: gp('plot sin(x)')

gpsave saves arrays into a file for gnuplot
Example:
    gsave([X,Y,Z], filename='something.dat')
    gp('plot "something.dat" u 1:($2/$3) w lp')
    gprint('myfigure.ps')

'''

import subprocess
import numpy
proc = subprocess.Popen(['gnuplot', '-p'], shell=False, stdin=subprocess.PIPE)  # persitant


def gp(command):
    '''
    Just send directly a command to gnuplot
    gnuplot('plot "tmp.dat" u 1:2 w lp)
    '''
    proc.stdin.write(command+'\n')  # \n to send 'return after typed command'


def gsave(data, filename='tmp.dat'):
    '''
    gpsave(data, filename='tmp.dat')
    Example:
    import numpy as np
    X = np.arange(10)
    Y = np.sin(X/(2*np.pi))
    Z = Y**2.0
    gsave([X,Y,Z])
    gp('plot "tmp.dat" u 1:2 w lp)
    gp('replot "tmp.dat" u 1:3' w lp)
    '''
    data = numpy.transpose(data)
    numpy.savetxt(filename, numpy.array(data), delimiter=', ')


def gprint(filename='tmp.ps', width=7, height=5, fontsize=12, term='x11'):
    '''Script to make gnuplot print into a postscript file
    gprint(filename='tmp.ps', width=7, height=5, fontsize=12, term='x11')
    (wxgnuplot: gprint(..., term='wxt')
    '''
    gp("set term postscipt size " +
       str(width) + "cm, " +
       str(height) + "cm color solid " +
       str(fontsize) + " font 'Calibri';")
    gp('set out ' + filename + '; replot; set term '+str(term)+'; replot')
