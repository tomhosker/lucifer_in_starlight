"""
This code defines some utility functions for the project as a whole.
"""

# Standard imports.
import os

def compile_tex_from_string(tex_string):
    """ Takes a tex file - in the form of a string - and compiles it. """
    with open("main.tex", "w") as main_file:
        main_file.write(tex_string)
    os.system("xelatex main.tex")
    os.system("xelatex main.tex")
    os.system("rm -f main.tex main.aux main.log main.out main.toc")

def get_contents(filename):
    """ Return the contents of a file. """
    with open(filename, "r") as the_file:
        result = the_file.read()
    return result
