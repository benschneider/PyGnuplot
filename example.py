from PyGnuplot import gp


f1 = gp()
e = 2.718281828459045


def sin(x):
    ''' returns sin for each x '''
    return (e**(i*1j)).imag


x = list(range(1000))
x = [i/20 for i in x]  # x = x/20
y1 = [i-25 for i in x]  # y1 = x-25
y2 = []  # calculate y2 = y1*sin(y1)
for i, j1 in enumerate(y1):
    y2.append(j1*sin(j1))

f1.s([x, y1, y2], filename='example.out')  # save data into a file t.out
f1.c('set title "example.pdf"; set xlabel "x-axis"; set ylabel "y-axis"')
f1.c('set yrange [-25:25]; set key center top')
f1.c("plot 'example.out' u 1:2 w l t 'y=x-25")  # plot fist part
f1.c("replot 'example.out' u 1:3 w l t 'y=(x-25)*sin(x-25)'")
f1.c("replot 'example.out' u 1:(-$2) w l t 'y=25-x'")
f1.pdf('example.pdf')  # export figure into a pdf file
