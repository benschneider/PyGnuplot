'''
By Ben Schneider

Simple python wrapper for Gnuplot

Example:
    import PyGnuplot as gp
    import numpy as np
    X = np.arange(10)
    Y = np.sin(X/(2*np.pi))
    Z = Y**2.0
    gp.s([X,Y,Z])  # saves data into tmp.dat
    gp.c('plot "tmp.dat" u 1:2 w lp)  # send 'plot instructions to gnuplot'
    gp.c('replot "tmp.dat" u 1:3' w lp)
    gp.p('myfigure.ps')  # creates postscript file

'''
from subprocess import Popen as _Popen, PIPE as _PIPE
from numpy import array as _array, transpose as _transpose, savetxt as _savetxt
proc = _Popen(['gnuplot', '-p'], shell=False, stdin=_PIPE)  # persitant -p


def c(command):
    '''
    Send command to gnuplot
    c('plot sin(x)')
    c('plot "tmp.dat" u 1:2 w lp)
    '''
    proc.stdin.write(command+'\n')  # \n to send 'return after typed command'


def s(data, filename='tmp.dat'):
    '''
    saves arrays into an ASCII file
    s(data, filename='tmp.dat')
    (overwrite existing files)
    '''
    data = _transpose(data)
    _savetxt(filename, _array(data), delimiter=', ')


def p(filename='tmp.ps', width=7, height=5, fontsize=12, term='x11'):
    '''Script to make gnuplot print into a postscript file
    p(filename='myfigure.ps')
    (overwrites existing files)
    '''
    c('set term postscript size ' + str(width) + 'cm, ' + str(height) + 'cm color solid ' +
      str(fontsize) + " font 'Calibri';")
    c('set out "' + filename + '";')
    c('replot;')
    c('set term '+str(term)+'; replot')
