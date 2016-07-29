import numpy as np
import PyGnuplot as pg

x = np.arange(1000)/20.0
y1 = x-25
y2 = y1*np.sin(x-25)

pg.s([x, y1, y2], filename='example.out')  # save data into a file t.out
pg.c('set title "example.pdf"; set xlabel "x-axis"; set ylabel "y-axis"')
pg.c('set yrange [-25:25]; set key center top')
pg.c("plot 'example.out' u 1:2 w l t 'y=x-25")  # plot fist part
pg.c("replot 'example.out' u 1:3 w l t 'y=(x-25)*sin(x-25)'")
pg.c("replot 'example.out' u 1:(-$2) w l t 'y=25-x'")
pg.pdf('example.pdf')  # export figure into a pdf file
