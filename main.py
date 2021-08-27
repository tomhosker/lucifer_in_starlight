"""
This code constructs a main.tex for each book of the project, compiling the
result each time.
"""

# Standard imports.
from sys import argv

# Local imports.
from book1 import Book1
from book2 import Book2

# Constants.
FORCE_PLACEHOLDERS_ALL_TUPLE = ("poems", "prayers", "prose", "images")
RECOGNISED_ARGUMENTS = (
    "--force-placeholders-all", "--force-placeholders-poems",
    "--force-placeholders-prayers", "--force-placeholders-prose",
    "--force-placeholders-images")

##################
# CORE FUNCTIONS #
##################

def make_book1(flags):
    """ Ronseal. """
    bk1 = Book1(force_placeholders=build_force_placeholders(flags))
    bk1.build_tex()
    bk1.build_pdf()

def make_book2():
    """ Ronseal. """
    bk2 = Book2()
    bk2.build_tex()
    bk2.build_pdf()

####################
# HELPER FUNCTIONS #
####################

def make_flags(cl_arguments):
    """ Interpret the command line arguments. """
    result = dict()
    for recognised_argument in RECOGNISED_ARGUMENTS:
        if recognised_argument in cl_arguments:
            result[recognised_argument] = True
        else:
            result[recognised_argument] = False
    return result

def build_force_placeholders(flags):
    """ Build the "force_placeholders" argument from the various flags. """
    result = []
    if flags["--force-placeholders-all"]:
        return FORCE_PLACEHOLDERS_ALL_TUPLE
    if flags["--force-placeholders-poems"]:
        result.append("poems")
    if flags["--force-placeholders-prayers"]:
        result.append("prayers")
    if flags["--force-placeholders-prose"]:
        result.append("prose")
    if flags["--force-placeholders-images"]:
        result.append("images")
    result = tuple(result)
    return result

##############
# RUN SCRIPT #
##############

def run():
    flags = make_flags(argv)
    make_book1(flags)
    make_book2()

if __name__ == "__main__":
    run()
