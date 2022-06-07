"""
This code defines some utility functions for the project as a whole.
"""

# Standard imports.
import os
import subprocess
from glob import glob

# Constants.
DEFAULT_LATEX_COMMAND = "lualatex"
DEFAULT_FN_STEM = "main"
DEFAULT_LATEX_EXTENSION = ".tex"
DEFAULT_OUTPUT_EXTENSION = ".pdf"

def compile_tex_from_string(
        tex_string,
        latex_command=DEFAULT_LATEX_COMMAND,
        fn_stem=DEFAULT_FN_STEM,
        latex_extension=DEFAULT_LATEX_EXTENSION,
        output_extension=DEFAULT_OUTPUT_EXTENSION
    ):
    """ Take a tex file, in the form of a string, and compile it. """
    with open("main.tex", "w") as main_file:
        main_file.write(tex_string)
    subprocess.run([latex_command, fn_stem+latex_extension], check=True)
    subprocess.run([latex_command, fn_stem+latex_extension], check=True)
#    for item in glob(fn_stem+".*"):
#        if item != fn_stem+output_extension:
#            os.remove(item)

def get_contents(path_to):
    """ Return the contents of a file. """
    with open(path_to, "r") as the_file:
        result = the_file.read()
    return result
