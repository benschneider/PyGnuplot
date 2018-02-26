'''
By Ben Schneider

Simple python wrapper for Gnuplot
Thanks to steview2000 for suggesting to separate processes,
    jrbrearley for help with debugging in python 3.4+

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

default_term = 'x11'  # change this if you use a different terminal


class _FigureList(object):

    def __init__(self):
        proc = _Popen(['gnuplot', '-p'], shell=False, stdin=_PIPE, universal_newlines=True)  # persitant -p
        self.instance = {0 : [proc, default_term]}  # {figure number : [process, terminal type]}
        self.n = 0  # currently selected Figure
        # Format:
        # instance[self.n][0] = process
        # instance[self.n][1] = terminal


def figure(number=None):
    '''Make Gnuplot plot in a new Window or update a defined one figure(num=None, term='x11'):
    >>> figure(2)  # would create or update figure 2
    >>> figure()  # simply creates a new figure
    returns the new figure number
    '''
    if not isinstance(number, int):  # create new figure if no number was given
        number = max(fl.instance) + 1

    if number not in fl.instance:  # number is new
        proc = _Popen(['gnuplot', '-p'], shell=False, stdin=_PIPE, universal_newlines=True)
        fl.instance[number] = [proc, default_term]

    fl.n = number
    c('set term ' + str(fl.instance[fl.n][1]) + ' ' + str(fl.n))
    return number


def c(command):
    '''
    Send command to gnuplot
    >>> c('plot sin(x)')
    >>> c('plot "tmp.dat" u 1:2 w lp)
    '''
    proc = fl.instance[fl.n][0]  # this is where the process is
    proc.stdin.write(command + '\n')  # \n 'send return in python 2.7'
    proc.stdin.flush()  # send the command in python 3.4+

def s(data, filename='tmp.dat'):
    '''
    saves numbers arrays and text into filename (default = 'tmp.dat)
    (assumes equal sizes and 2D data sets)
    >>> s(data, filename='tmp.dat')  # overwrites/creates tmp.dat
    '''
    file = open(filename, 'w')
    columns = len(data)
    rows = len(data[0])
    for j in range(rows):
        for i in range(columns):
            file.write(str(data[i][j]))
            file.write(' ')
        file.write('\n')
        if j % 1000 == 0 :
            file.flush()  # write once after every 1000 entries
    file.close()  # write the rest

def plot(data, filename='tmp.dat'):
    ''' Save data into filename (default = 'tmp.dat') and send plot instructions to Gnuplot'''
    s(data, filename)
    c('plot "' + filename + '" w lp')


def p(filename='tmp.ps', width=14, height=9, fontsize=12, term=default_term):
    '''Script to make gnuplot print into a postscript file
    >>> p(filename='myfigure.ps')  # overwrites/creates myfigure.ps
    '''
    c('set term postscript size ' + str(width) + 'cm, ' + str(height) + 'cm color solid ' +
      str(fontsize) + " font 'Calibri';")
    c('set out "' + filename + '";')
    c('replot;')
    c('set term ' + str(term) + '; replot')


def pdf(filename='tmp.pdf', width=14, height=9, fontsize=12, term=default_term):
    '''Script to make gnuplot print into a pdf file
    >>> pdf(filename='myfigure.pdf')  # overwrites/creates myfigure.pdf
    '''
    c('set term pdf enhanced size ' + str(width) + 'cm, ' + str(height) + 'cm color solid fsize ' +
      str(fontsize) + " fname 'Helvetica';")
    c('set out "' + filename + '";')
    c('replot;')
    c('set term ' + str(term) + '; replot')


fl = _FigureList()
