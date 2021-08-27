"""
This code defines some utility functions for the project as a whole.
"""

# Standard imports.
import os

def compile_tex_from_string(tex_string):
    """ Takes a tex file - in the form of a string - and compiles it. """
    with open("main.tex", "w") as main_file:
        main_file.write(tex_string)
    os.system("lualatex main.tex")
    os.system("lualatex main.tex")
    os.system("rm -f main.aux main.log main.out main.tex main.toc")

def get_contents(path_to):
    """ Return the contents of a file. """
    with open(path_to, "r") as the_file:
        result = the_file.read()
    return result
