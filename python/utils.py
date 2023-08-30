"""
This code defines some utility functions for the project as a whole.
"""

# Standard imports.
import json
import subprocess
from pathlib import Path

# Constants.
DEFAULT_LATEX_COMMAND = "lualatex"
DEFAULT_LATEX_EXTENSION = ".tex"
DEFAULT_PATH_TO_WHICH = \
    str(Path(__file__).resolve().parent/"content"/"poems"/"which.json")
OUTPUT_EXTENSION = ".pdf"
MAIN_FN_STEM = "main"
PATH_OBJ_TO_ROOT = Path(__file__).parent

#############
# FUNCTIONS #
#############

def compile_tex_from_string(
        tex_string,
        latex_command=DEFAULT_LATEX_COMMAND,
        latex_extension=DEFAULT_LATEX_EXTENSION,
    ):
    """ Take a tex file, in the form of a string, and compile it. """
    with open("main.tex", "w") as main_file:
        main_file.write(tex_string)
    subprocess.run([latex_command, MAIN_FN_STEM+latex_extension], check=True)
    subprocess.run([latex_command, MAIN_FN_STEM+latex_extension], check=True)
    for item in Path().glob(MAIN_FN_STEM+".*"):
        if item.suffix != OUTPUT_EXTENSION:
            item.unlink()

def get_contents(path_to):
    """ Return the contents of a file. """
    with open(path_to, "r") as the_file:
        result = the_file.read()
    return result

def get_which(path_to=DEFAULT_PATH_TO_WHICH):
    """ Get the dictionary stating which poems go where. """
    with open(path_to, "r") as which_file:
        result = json.load(which_file)
    return result
