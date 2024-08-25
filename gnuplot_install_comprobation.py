from os import path as os_path
from os import name as os_name

class UninstalledGnuplotError(Exception):
    """Raise if is not possible to find a gnuplot installation"""
    def __init__(self, gnuplot_path):
        self.__gnuplot_path = gnuplot_path
        super().__init__(
            f"There is no installation for Gnuplot in {self.__gnuplot_path}. Install Gnuplot before using PyGnuplot."
        )

def verify_gnuplot_installation():
    """ Verify Gnuplot installation in default paths in posix os nt"""
    if os_name == "posix":
        gnuplot_path = "/usr/bin/gnuplot"
    elif os_name == "nt":
        gnuplot_path = r"C:\Program Files\gnuplot"
    has_gnuplot = os_path.exists(gnuplot_path)
    if has_gnuplot == False:
        raise UninstalledGnuplotError(gnuplot_path)

if __name__ == "__main__":
    # test
    verify_gnuplot_installation()
    #raise UninstalledGnuplotError(r"C:\Program Files\gnuplot")
