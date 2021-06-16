"""
This code defines a class, which in turn builds and compiles LaTeX code for
Book 2 of this project.
"""

# Imports.
import os

# Local imports.
import which_poems
from utilities import compile_tex_from_string, get_contents

##############
# MAIN CLASS #
##############

class Book2:
    """ The class in question. """
    def __init__(self):
        self.tex = None
        self.base = get_contents("book2_base.tex")
        self.package_code = get_contents("package_code.tex")

    def build_tex(self):
        """ Add the poems to the .tex document. """
        result = self.base
        result = result.replace("#PACKAGE_CODE", self.package_code)
        the_poems = ""
        for filename in which_poems.book2:
            poem = Poem(filename)
            the_poems = the_poems+poem.printout+"\n\n"
        result = result.replace("#THE_POEMS", the_poems)
        self.tex = result

    def build_pdf(self):
        """ Build the PDF using XeLaTeX. """
        compile_tex_from_string(self.tex)
        os.system("mv main.pdf book2.pdf")

class Poem:
    """ A helper class, this handles the properties of a poem. """
    def __init__(self, filename):
        self.filename = filename
        self.title = self.parse_title()
        self.body = get_contents("poems/book2/"+filename)
        self.printout = self.get_printout()

    def parse_title(self):
        """ Converts a filename into a title. """
        result = self.filename[:self.filename.index(".tex")]
        result = result.replace("_", " ")
        return result

    def get_printout(self):
        """ Generates a LaTeX printout from the other fields. """
        result = "\\chapter*{"+self.title+"}\n\n"+self.body
        return result
