"""
This code defines a class which builds and compiles LaTeX code for Book 1 of
this project.
"""

# Standard imports.
import os

# Local imports.
import which_poems
from utilities import compile_tex_from_string, get_contents

# Local constants.
DEFAULT_PATH_TO_BASE = "book1_base.tex"
DEFAULT_IMAGE_EXTENSIONS = {
    "autumnal": "jpg", "hibernal": "jpg", "vernal": "jpg",
    "aestival": "jpg" }
DEFAULT_PATH_TO_POEM_DIR = "poems/"
DEFAULT_PATH_TO_PLACEHOLDER_POEM = os.path.join(
    DEFAULT_PATH_TO_POEM_DIR, "placeholder_poem.tex")
DEFAULT_PATH_TO_PROSE_DIR = "prose/"
DEFAULT_PATH_TO_PLACEHOLDER_PROSE = os.path.join(
    DEFAULT_PATH_TO_PROSE_DIR, "placeholder_prose.tex")
DEFAULT_PATH_TO_IMAGE_DIR = "images/"
DEFAULT_PATH_TO_PLACEHOLDER_IMAGE = os.path.join(
    DEFAULT_PATH_TO_IMAGE_DIR, "placeholder_image.jpg")

##############
# MAIN CLASS #
##############

class Book1:
    """ The class in question. """
    def __init__(self, path_to_base=DEFAULT_PATH_TO_BASE,
                 image_extensions=DEFAULT_IMAGE_EXTENSIONS):
        self.image_extensions = image_extensions
        self.tex = None
        self.base = get_contents(path_to_base)
        self.package_code = get_contents("package_code.tex")
        self.autumnal1 = get_poem(which_poems.autumnal1)
        self.autumnal2 = get_poem(which_poems.autumnal2)
        self.autumnal3 = get_poem(which_poems.autumnal3)
        self.hibernal1 = get_poem(which_poems.hibernal1)
        self.hibernal2 = get_poem(which_poems.hibernal2)
        self.hibernal3 = get_poem(which_poems.hibernal3)
        self.vernal1 = get_poem(which_poems.vernal1)
        self.vernal2 = get_poem(which_poems.vernal2)
        self.vernal3 = get_poem(which_poems.vernal3)
        self.aestival1 = get_poem(which_poems.aestival1)
        self.aestival2 = get_poem(which_poems.aestival2)
        self.aestival3 = get_poem(which_poems.aestival3)
        self.autumnal_prose = get_prose("autumnal.tex")
        self.hibernal_prose = get_prose("hibernal.tex")
        self.vernal_prose = get_prose("vernal.tex")
        self.aestival_prose = get_prose("aestival.tex")
        self.autumnal_image = get_image(
                                  "autumnal."+image_extensions["autumnal"])
        self.hibernal_image = get_image(
                                  "hibernal."+image_extensions["hibernal"])
        self.vernal_image = get_image(
                                "vernal."+image_extensions["vernal"])
        self.aestival_image = get_image(
                                  "aestival."+image_extensions["aestival"])

    def build_tex(self):
        """ Replace the tags in the .tex document with the fields created in
        this class's constructor. """
        result = self.base
        result = result.replace("#PACKAGE_CODE", self.package_code)
        result = result.replace("#AUTUMNAL_POEM_1", self.autumnal1)
        result = result.replace("#AUTUMNAL_POEM_2", self.autumnal2)
        result = result.replace("#AUTUMNAL_POEM_3", self.autumnal3)
        result = result.replace("#HIBERNAL_POEM_1", self.hibernal1)
        result = result.replace("#HIBERNAL_POEM_2", self.hibernal2)
        result = result.replace("#HIBERNAL_POEM_3", self.hibernal3)
        result = result.replace("#VERNAL_POEM_1", self.vernal1)
        result = result.replace("#VERNAL_POEM_2", self.vernal2)
        result = result.replace("#VERNAL_POEM_3", self.vernal3)
        result = result.replace("#AESTIVAL_POEM_1", self.aestival1)
        result = result.replace("#AESTIVAL_POEM_2", self.aestival2)
        result = result.replace("#AESTIVAL_POEM_3", self.aestival3)
        result = result.replace("#AUTUMNAL_PROSE", self.autumnal_prose)
        result = result.replace("#HIBERNAL_PROSE", self.hibernal_prose)
        result = result.replace("#VERNAL_PROSE", self.vernal_prose)
        result = result.replace("#AESTIVAL_PROSE", self.aestival_prose)
        result = result.replace("#AUTUMNAL_IMAGE", self.autumnal_image)
        result = result.replace("#HIBERNAL_IMAGE", self.hibernal_image)
        result = result.replace("#VERNAL_IMAGE", self.vernal_image)
        result = result.replace("#AESTIVAL_IMAGE", self.aestival_image)
        self.tex = result

    def build_pdf(self):
        """ Build the PDF using XeLaTeX. """
        compile_tex_from_string(self.tex)
        os.system("mv main.pdf book1.pdf")

####################
# HELPER FUNCTIONS #
####################

def get_poem(filename, path_to_dir=DEFAULT_PATH_TO_POEM_DIR,
             path_to_placeholder=DEFAULT_PATH_TO_PLACEHOLDER_POEM):
    """ Return the contents of a file, or return a placeholder if
    necessary. """
    if not filename:
        return get_contents(path_to_placeholder)
    path_to = os.path.join(path_to_dir, filename)
    if os.path.exists(path_to):
        result = get_contents(path_to)
    else:
        return get_contents(path_to_placeholder)
    return result

def get_prose(filename, path_to_dir=DEFAULT_PATH_TO_PROSE_DIR,
              path_to_placeholder=DEFAULT_PATH_TO_PLACEHOLDER_PROSE):
    """ Return the contents of a file, or return a placeholder if
    necessary. """
    return get_poem(filename, path_to_dir=path_to_dir,
                    path_to_placeholder=path_to_placeholder)

def get_image(filename, path_to_image_dir=DEFAULT_PATH_TO_IMAGE_DIR,
              path_to_placeholder=DEFAULT_PATH_TO_PLACEHOLDER_IMAGE):
    """ Return the path to a file, or return a placeholder if
    necessary. """
    result = os.path.join(path_to_image_dir, filename)
    if os.path.exists(result):
        return result
    else:
        return path_to_placeholder
