"""
This code constructs a main.tex for each book of the project, compiling the
result each time.
"""

# Local imports.
from book1 import Book1
from book2 import Book2

####################
# HELPER FUNCTIONS #
####################

def make_book1():
    """ Ronseal. """
    bk1 = Book1()
    bk1.build_tex()
    bk1.build_pdf()

def make_book2():
    """ Ronseal. """
    bk2 = Book2()
    bk2.build_tex()
    bk2.build_pdf()

##############
# RUN SCRIPT #
##############

def run():
    make_book1()
    make_book2()

if __name__ == "__main__":
    run()
