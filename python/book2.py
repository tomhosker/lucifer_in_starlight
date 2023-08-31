"""
This code defines a class, which in turn builds and compiles LaTeX code for
Book 2 of this project.
"""

# Imports.
from pathlib import Path

# Local imports.
from .utils import (
    PATH_OBJ_TO_ROOT,
    MAIN_FN_STEM,
    OUTPUT_EXTENSION,
    compile_tex_from_string,
    get_contents,
    get_which
)
from .book1 import PATH_OBJ_TO_TEX_DIR, PATH_TO_PACKAGE_CODE

# Local constants.
WHICH_BK2 = get_which()["book2"]
# Path objects.
PATH_OBJ_TO_BK2_POEMS_DIR = PATH_OBJ_TO_ROOT/"content"/"poems"/"book2"
# Paths.
PATH_TO_BASE = str(PATH_OBJ_TO_TEX_DIR/"book2_base.tex")

##############
# MAIN CLASS #
##############

class Book2:
    """ The class in question. """
    def __init__(self, preserve_tex_file=False):
        self.tex = None
        self.base = get_contents(PATH_TO_BASE)
        self.package_code = get_contents(PATH_TO_PACKAGE_CODE)
        self.preserve_tex_file = preserve_tex_file

    def build_tex(self):
        """ Add the poems to the .tex document. """
        result = self.base
        result = result.replace("#PACKAGE_CODE", self.package_code)
        the_poems = ""
        for filename in WHICH_BK2:
            poem = Poem(filename)
            the_poems += poem.printout+"\n\n"
        result = result.replace("#THE_POEMS", the_poems)
        self.tex = result

    def build_pdf(self):
        """ Build the PDF. """
        compile_tex_from_string(
            self.tex,
            preserve_tex_file=self.preserve_tex_file
        )
        Path(MAIN_FN_STEM+OUTPUT_EXTENSION).rename("book2"+OUTPUT_EXTENSION)

################################
# HELPER CLASSES AND FUNCTIONS #
################################

class Poem:
    """ A helper class, this handles the properties of a poem. """
    def __init__(self, filename):
        self.filename = filename
        self.path_to = str(PATH_OBJ_TO_BK2_POEMS_DIR/filename)
        self.title = self.parse_title()
        self.body = get_contents(self.path_to)
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
