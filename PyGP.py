'''
By Ben Schneider

creates a pip using subprocess to gnuplot (requires gnuplot to be installed)

gp is used to send commands to gnuplot.
Example: gp('plot sin(x)')

gpsave saves arrays into a file for gnuplot
Example:
    gpsave([X,Y,Z], filename='something.dat')
    gp('plot "something.dat" u 1:($2/$3) w lp')

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


def gpsave(data, filename='tmp.dat'):
    '''
    gpsave(data, filename='tmp.dat')
    Example:
    import numpy as np
    X = np.arange(10)
    Y = np.sin(X/(2*np.pi))
    Z = Y**2.0
    gpsave([X,Y,Z])
    gp('plot "tmp.dat" u 1:2 w lp)
    gp('replot "tmp.dat" u 1:3' w lp)
    '''
    data = numpy.transpose(data)
    numpy.savetxt(filename, numpy.array(data), delimiter=', ')
