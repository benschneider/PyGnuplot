from os import path as os_path
from os import name as os_name

class UninstalledGnuplotException(Exception):
    """Raise if is not possible to find a gnuplot installation"""
    def __init__(self, message="There is no installation for Gnuplot. Install Gnuplot before using PyGnuplot."):
        self.__message = message
        super().__init__(self.__message)

def verify_gnuplot_installation():
    """ Verify in posix os the installation of Gnuplot"""
    if os_name == "posix":
        has_gnuplot = os_path.exists("/usr/bin/gnuplot")
        if has_gnuplot == False:
            raise UninstalledGnuplotException

if __name__ == "__main__":
    # test
    verify_gnuplot_installation()
    #raise UninstalledGnuplotException