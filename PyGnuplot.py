'''
By Ben Schneider

Simple python wrapper for Gnuplot
Thanks to steview2000 for suggesting to separate processes,
    jrbrearley for help with debugging in python 3.4+

Special Thanks to ddip!
    This code was rewritten according to ddipp's suggestions resulting in
    a cleaner and better code and finnaly giving accesss to gnuplot returns thus
    allowing the use of the gnuplot fit function.

Example:
    from PyGnuplot import gp
    import numpy as np
    X = np.arange(10)
    Y = np.sin(X/(2*np.pi))
    Z = Y**2.0
    fig1 = gp()
    fig1.s([X,Y,Z])  # saves data into tmp.dat
    fig1.c('plot "tmp.dat" u 1:2 w lp)  # send 'plot instructions to gnuplot'
    fig1.c('replot "tmp.dat" u 1:3' w lp)
    fig1.pdf('myfigure.pdf')  # outputs pdf file


'''

import sys
from subprocess import PIPE, Popen
from threading import Thread
from struct import pack

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  # python 2.x

ON_POSIX = 'posix' in sys.builtin_module_names

class gp(object):
    """PyGnuplot object gp
    example:
        fig1 = gp()
        pi = fig1.a('print pi')
    """
    def __init__(self):
        ''' open pipe with gnuplot '''
        self.p = Popen(['gnuplot'], stdin=PIPE, stderr=PIPE, stdout=PIPE, bufsize=1, close_fds=ON_POSIX, shell=False, universal_newlines=True)
        # self.p = Popen(['gnuplot', '-p'], stdin=PIPE, stderr=PIPE, stdout=PIPE, bufsize=1, close_fds=ON_POSIX, shell=False, universal_newlines=True)
        self.q_err = Queue()
        self.t_err = Thread(target=self.enqueue_std, args=(self.p.stderr, self.q_err))
        self.t_err.daemon = True  # thread dies with the program
        self.t_err.start()
        self.q_out = Queue()
        self.t_out = Thread(target=self.enqueue_std, args=(self.p.stdout, self.q_out))
        self.t_out.daemon = True  # thread dies with the program
        self.t_out.start()
        self.default_term = self.a('print GPVAL_TERM')[0]
        # self.w('set print "-"')  # to separate sdtout and stderr

    def enqueue_std(self, out, queue):
        for line in iter(out.readline, ''):
            queue.put(line)
        out.close()

    def c(self, command):
        ''' write a command doesnt check for response
        >>> w('plot sin(x)')  # only send a command to gnuplot'''
        self.p.stdin.write(command + '\n')  # \n 'send return in python 2.7'
        self.p.stdin.flush()  # send the command in python 3.4+
        # if return available return stuff here

    def r(self, vtype=str, timeout=0.05):
        ''' read line without blocking, also clears the buffer.
        >>> r()  # read response from gnuplot'''
        lines = []
        while True:
            try:
                line = self.q_err.get(timeout=timeout)  # or .get_nowait()
                lines.append(vtype(line.strip()))
            except Empty:
                break
        return lines

    def a(self, command='', vtype=str, timeout=0.05):
        ''' ask gnuplot (write and get answer)
        >>> a('print pi')
        '''
        self.c(command)
        return self.r(vtype, timeout)

    def wb(self, bin_data):
        ''' this is used to pipe binary formated data to gnuplot '''
        self.p.stdin.buffer.write(bin_data)
        self.p.stdin.buffer.flush()

    def m_binary(self, data_in, v_format='d'):
        ''' turn data in binary format'''
        columns = len(data_in)
        xy = list(zip(*data_in))
        bin_st = bytearray()
        for i in xy:
            bin_st += pack(v_format*columns, *i)  # convert linewise into binary
        return bin_st

    def m_str(self, data, delimiter=' '):
        ''' turn data into string format'''
        columns = len(data)
        xy = list(zip(*data))
        ascii_st = ''
        for i in xy:
            for j in i:
                ascii_st += str(j) + delimiter
            ascii_st += '\n'
        return ascii_st

    def plot(self, data):
        ''' quick plot data in gnuplot
            it basically pipes the data to gnuplot and plots it
        '''
        d1 = len(data[0])
        self.c('plot "-" u 1:2 w lp')
        str_data = self.m_str(data)
        self.c(str_data+'e')  # add end character to plot string
        return self.a()

    def plot_b(self, data, v1='d', v2="%double"):
        ''' quick plot data in gnuplot
            tell gnuplot to expect binary
            convert data into binary
            send data
            Note this is currently limited to simple 2d graph
        '''
        d1 = len(data[0])
        self.c('plot "-" binary record='+str(d1)+' format="'+str(v2)+'" w lp')
        bin_data = self.m_binary(data, v_format=v1)
        self.wb(bin_data)
        return self.a()

    def s(self, data, filename='tmp.dat', delimiter=' '):
        '''
        saves numbers arrays and text into filename (default = 'tmp.dat)
        (assumes equal sizes and 2D data sets)
        >>> s(data, filename='tmp.dat')  # overwrites/creates tmp.dat
        '''
        with open(filename, 'w') as f:
            filestr = self.m_str(data, delimiter=delimiter)
            f.write(filestr)
            f.close()  # write the rest and close

    def ps(self, filename='tmp.ps', width=14, height=9, fontsize=12):
        '''Script to make gnuplot print into a postscript file
        >>> ps(filename='myfigure.ps')  # overwrites/creates myfigure.ps
        '''
        self.c('set term postscript size ' + str(width) + 'cm, ' + str(height) + 'cm color solid ' +
               str(fontsize) + " font 'Calibri';")
        self.c('set out "' + filename + '";')
        self.c('replot;')
        self.c('set term ' + self.default_term + '; replot')
        return self.r()

    def pdf(self, filename='tmp.pdf', width=8.8, height=6, fontscale=0.5):
        '''Script to make gnuplot print into a pdf file
        >>> pdf(filename='myfigure.pdf')  # overwrites/creates myfigure.pdf
        '''
        self.c('set term pdfcairo fontscale ' + str(fontscale) + 'size ' + str(width) + 'cm, ' + str(height) + "cm;")
        self.c('set out "' + filename + '";')
        self.c('replot;')
        self.c('set term ' + self.default_term + '; replot')
        return self.r() # clear buffer

    def quit(self):
        self.c('set term ' + self.default_term + ' reset')  # close all windows
        aa = self.a('exit')  # close gnuplot
        self.p.kill()  # kill pipe
        return aa


if __name__ == '__main__':
    # test functionality
    x = [0, 1, 2]
    y = [5, -1, 5]
    z = [4, 5, 2]
    f1 = gp()
    # f1.plot_b([x,y])
    dat_b = f1.m_binary([x,y])
    dat_s = f1.m_str([x,y], delimiter='\t')

