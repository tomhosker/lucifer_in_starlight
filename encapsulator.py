"""
This code defines a class which produces a PDF for a given poem.
"""

# Standard imports.
import os
import sys

# Local imports.
from utilities import compile_tex_from_string, get_contents

# Local constants.
ENCAPSULATOR_BASE = (
    "\\documentclass{amsart}\n\n"+
    "#PACKAGE_CODE\n\n"+
    "\\title{#TITLE}\n\n"+
    "\\begin{document}\n\n"+
    "\\maketitle\n\n"+
    "\\thispagestyle{empty}\n\n"+
    "#CONTENT\n\n"+
    "\\end{document}")

##############
# MAIN CLASS #
##############

class Encapsulator:
    """ The class in question. """
    def __init__(self, path_to, title="\ding{72}"):
        self.path_to = path_to
        self.title = title
        self.tex = None
        self.base = ENCAPSULATOR_BASE
        self.package_code = get_contents("package_code.tex")
        self.content = get_contents(self.path_to)

    def make_replacements(self):
        """ Ronseal. """
        self.tex = self.base
        self.tex = self.tex.replace("#PACKAGE_CODE", self.package_code)
        self.tex = self.tex.replace("#TITLE", self.title)
        self.tex = self.tex.replace("#CONTENT", self.content)

    def build_pdf(self):
        """ Ronseal. """
        compile_tex_from_string(self.tex)
        os.system("mv main.pdf poem.pdf")

###########
# TESTING #
###########

def demo():
    """ Run a demo. """
    encapsulator = Encapsulator("poems/book1/the_tide.tex")
    encapsulator.make_replacements()
    encapsulator.build_pdf()

###################
# RUN AND WRAP UP #
###################

def run():
    path_to = "poems/book1/afterwards_we.tex"
    encapsulator = Encapsulator(path_to)
    encapsulator.make_replacements()
    encapsulator.build_pdf()

if __name__ == "__main__":
    run()
