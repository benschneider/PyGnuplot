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


class _emptyClass(object):
    def __init__(self):
        self.figNum = [0]

_vc = _emptyClass()


def c(command):
    '''
    Send command to gnuplot
    >>> c('plot sin(x)')
    >>> c('plot "tmp.dat" u 1:2 w lp)
    '''
    proc.stdin.write(command+'\n')  # \n to send 'return after typed command'


def s(data, filename='tmp.dat'):
    '''
    saves arrays into an ASCII file easily read in gnuplot
    >>> s(data, filename='tmp.dat')  # overwrites/creates tmp.dat
    '''
    data = _transpose(data)
    _savetxt(filename, _array(data), delimiter=', ')


def figure(number=None, term='x11'):
    '''Make Gnuplot plot in a new Window or update a defined one
    figure(num=None, term='x11'):
    >>> figure(2)  # would create or update figure 2
    >>> figure()  # simply creates a new figure
    returns the new figure number
    '''
    _vc.figNum.sort()
    if not isinstance(number, int):
        number = _vc.figNum[-1]+1

    if number not in _vc.figNum:
        _vc.figNum.append(number)

    c('set term '+str(term)+' '+str(number))
    return _vc.figNum[-1]


def p(filename='tmp.ps', width=14, height=9, fontsize=12, term='x11'):
    '''Script to make gnuplot print into a postscript file
    >>> p(filename='myfigure.ps')  # overwrites/creates myfigure.ps
    '''
    c('set term postscript size ' + str(width) + 'cm, ' + str(height) + 'cm color solid ' +
      str(fontsize) + " font 'Calibri';")
    c('set out "' + filename + '";')
    c('replot;')
    c('set term '+str(term)+'; replot')


def pdf(filename='tmp.pdf', width=14, height=9, fontsize=12, term='x11'):
    '''Script to make gnuplot print into a pdf file
    >>> pdf(filename='myfigure.pdf')  # overwrites/creates myfigure.pdf
    '''
    c('set term pdf enhanced size ' + str(width) + 'cm, ' + str(height) + 'cm color solid fsize ' +
      str(fontsize) + " fname 'Helvetica';")
    c('set out "' + filename + '";')
    c('replot;')
    c('set term '+str(term)+'; replot')
