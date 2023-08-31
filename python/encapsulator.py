"""
This code defines a class which produces a PDF for a given poem.
"""

# Standard imports.
from pathlib import Path

# Local imports.
from .utils import (
    OUTPUT_EXTENSION,
    MAIN_FN_STEM,
    compile_tex_from_string,
    get_contents
)
from .book1 import PATH_TO_PACKAGE_CODE

# Local constants.
ENCAPSULATOR_BASE = (
    "\\documentclass{amsart}\n\n"+
    "#PACKAGE_CODE\n\n"+
    "\\title{#TITLE}\n\n"+
    "\\begin{document}\n\n"+
    "\\maketitle\n\n"+
    "\\thispagestyle{empty}\n\n"+
    "#CONTENT\n\n"+
    "\\end{document}"
)
DEFAULT_TITLE = "\ding{72}"
DEFAULT_OUTPUT_FN = "poem.pdf"

# Configs.
PATH_TO = "poems/book2/A_Love-Letter.tex"
TITLE = "A Love-Letter"

##############
# MAIN CLASS #
##############

class Encapsulator:
    """ The class in question. """
    def __init__(
            self,
            path_to,
            title=DEFAULT_TITLE,
            output_fn=DEFAULT_OUTPUT_FN
        ):
        self.path_to = path_to
        self.title = title
        self.output_fn = output_fn
        self.tex = None
        self.base = ENCAPSULATOR_BASE
        self.package_code = get_contents(PATH_TO_PACKAGE_CODE)
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
        Path(MAIN_FN_STEM+OUTPUT_EXTENSION).rename(self.output_fn)

###################
# RUN AND WRAP UP #
###################

def run():
    encapsulator = Encapsulator(PATH_TO, title=TITLE)
    encapsulator.make_replacements()
    encapsulator.build_pdf()

if __name__ == "__main__":
    run()
