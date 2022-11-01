"""
This code defines a class which builds and compiles LaTeX code for Book 1 of
this project.
"""

# Standard imports.
import os
from argparse import Namespace
from dataclasses import dataclass
from pathlib import Path

# Local imports.
import which_poems
from utilities import compile_tex_from_string, get_contents

# Local constants.
DEFAULT_PATH_TO_BASE = "book1_base.tex"
DEFAULT_IMAGE_EXTENSIONS = {
    "autumnal": "jpg",
    "hibernal": "jpg",
    "vernal": "jpg",
    "aestival": "jpg"
}
DEFAULT_PATH_TO_POEM_DIR = str(Path("poems")/"book1")
DEFAULT_PATH_TO_PLACEHOLDER_POEM = str(Path("poems")/"placeholder_poem.tex")
DEFAULT_PATH_TO_PRAYER_DIR = "prayers"
DEFAULT_PATH_TO_PLACEHOLDER_PRAYER = \
    str(Path(DEFAULT_PATH_TO_PRAYER_DIR)/"placeholder_prayer.tex")
DEFAULT_PATH_TO_PROSE_DIR = "prose"
DEFAULT_PATH_TO_PLACEHOLDER_PROSE = \
    str(Path(DEFAULT_PATH_TO_PROSE_DIR)/"placeholder_prose.tex")
DEFAULT_PATH_TO_IMAGE_DIR = "images"
DEFAULT_PATH_TO_PLACEHOLDER_IMAGE = \
    str(Path(DEFAULT_PATH_TO_IMAGE_DIR)/"placeholder.png")
DEFAULT_POEM_CODE_BEGIN = (
    "\\begin{figure*}[p!]\n"+
    "\\bigskip\n"+
    "\\ding{72}\n"+
    "\\bigskip\n"
)
DEFAULT_POEM_CODE_END = "\\end{figure*}"
DEFAULT_PRAYER_CODE_BEGIN = (
    "\\bigskip\n"+
    "\\centering \\ding{58}\n"+
    "\\bigskip\n"+
    "\\begin{quote}\n"
)
DEFAULT_PRAYER_CODE_END = "\\end{quote}"

##############
# MAIN CLASS #
##############

@dataclass
class Book1:
    """ The class in question. """
    # Fields.
    image_extensions: dict = None
    poem_code_begin: str = DEFAULT_POEM_CODE_BEGIN
    poem_code_end: str = DEFAULT_POEM_CODE_END
    prayer_code_begin: str = DEFAULT_PRAYER_CODE_BEGIN
    prayer_code_end: str = DEFAULT_PRAYER_CODE_END
    force_placeholders: Namespace = Namespace()
    path_to_base: str = DEFAULT_PATH_TO_BASE
    # Generated fields.
    tex: str = None
    base: str = None
    package_code: str = get_contents("package_code.tex")
    poems: list = None
    prayers: list = None
    prose: list = None
    images: list = None

    def __post_init__(self):
        if not self.image_extensions:
            self.image_extensions = DEFAULT_IMAGE_EXTENSIONS
        self.base = get_contents(self.path_to_base)
        self.poems = self.get_poems()
        self.prayers = self.get_prayers()
        self.prose = self.get_prose()
        self.images = self.get_images()

    def get_poems(self):
        """ Fetch the desired poems from disk. """
        if self.force_placeholders.force_placeholders_poems:
            result = get_poems_all_placeholders()
        else:
            result = {
                "autumnal1": get_poem(which_poems.autumnal1),
                "autumnal2": get_poem(which_poems.autumnal2),
                "hibernal1": get_poem(which_poems.hibernal1),
                "hibernal2": get_poem(which_poems.hibernal2),
                "vernal1": get_poem(which_poems.vernal1),
                "vernal2": get_poem(which_poems.vernal2),
                "aestival1": get_poem(which_poems.aestival1),
                "aestival2": get_poem(which_poems.aestival2),
                "aestival3": get_poem(which_poems.aestival3)
            }
        for key in result:
            result[key] = self.poem_code_begin+result[key]+self.poem_code_end
        return result

    def get_prayers(self):
        """ Fetch the desired poems from disk. """
        if self.force_placeholders.force_placeholders_prayers:
            result = get_prayers_all_placeholders()
        else:
            result = {
                "autumnal": get_prayer("autumnal.tex"),
                "hibernal": get_prayer("hibernal.tex"),
                "vernal": get_prayer("vernal.tex")
            }
        for key in result:
            result[key] = \
                self.prayer_code_begin+result[key]+self.prayer_code_end
        return result

    def get_prose(self):
        """ Fetch the desired prose passages from disk. """
        if self.force_placeholders.force_placeholders_prose:
            result = get_prose_all_placeholders()
        else:
            result = {
                "autumnal": get_prose("autumnal.tex"),
                "hibernal": get_prose("hibernal.tex"),
                "vernal": get_prose("vernal.tex"),
                "aestival": get_prose("aestival.tex")
            }
        return result

    def get_images(self):
        """ Fetch the desired paths to images from disk. """
        if self.force_placeholders.force_placeholders_images:
            result = get_images_all_placeholders()
        else:
            result = {
                "autumnal": (
                    get_image("autumnal."+self.image_extensions["autumnal"])
                ),
                "hibernal": (
                    get_image("hibernal."+self.image_extensions["hibernal"])
                ),
                "vernal": (
                    get_image("vernal."+self.image_extensions["vernal"])
                ),
                "aestival": (
                    get_image("aestival."+self.image_extensions["aestival"])
                )
            }
        return result

    def build_tex(self):
        """ Replace the tags in the .tex document with the fields created in
        this class's constructor. """
        result = self.base
        result = result.replace("#PACKAGE_CODE", self.package_code)
        result = result.replace("#AUTUMNAL_POEM_1", self.poems["autumnal1"])
        result = result.replace("#AUTUMNAL_POEM_2", self.poems["autumnal2"])
        result = result.replace("#HIBERNAL_POEM_1", self.poems["hibernal1"])
        result = result.replace("#HIBERNAL_POEM_2", self.poems["hibernal2"])
        result = result.replace("#VERNAL_POEM_1", self.poems["vernal1"])
        result = result.replace("#VERNAL_POEM_2", self.poems["vernal2"])
        result = result.replace("#AESTIVAL_POEM_1", self.poems["aestival1"])
        result = result.replace("#AESTIVAL_POEM_2", self.poems["aestival2"])
        result = result.replace("#AESTIVAL_POEM_3", self.poems["aestival3"])
        result = result.replace("#AUTUMNAL_PRAYER", self.prayers["autumnal"])
        result = result.replace("#HIBERNAL_PRAYER", self.prayers["hibernal"])
        result = result.replace("#VERNAL_PRAYER", self.prayers["vernal"])
        result = result.replace("#AUTUMNAL_PROSE", self.prose["autumnal"])
        result = result.replace("#HIBERNAL_PROSE", self.prose["hibernal"])
        result = result.replace("#VERNAL_PROSE", self.prose["vernal"])
        result = result.replace("#AESTIVAL_PROSE", self.prose["aestival"])
        result = result.replace("#AUTUMNAL_IMAGE", self.images["autumnal"])
        result = result.replace("#HIBERNAL_IMAGE", self.images["hibernal"])
        result = result.replace("#VERNAL_IMAGE", self.images["vernal"])
        result = result.replace("#AESTIVAL_IMAGE", self.images["aestival"])
        self.tex = result

    def build_pdf(self):
        """ Build the PDF using XeLaTeX. """
        compile_tex_from_string(self.tex)
        os.rename("main.pdf", "book1.pdf")

####################
# HELPER FUNCTIONS #
####################

def get_poem(
        filename,
        path_to_dir=DEFAULT_PATH_TO_POEM_DIR,
        path_to_placeholder=DEFAULT_PATH_TO_PLACEHOLDER_POEM
    ):
    """ Return the contents of a file, or return a placeholder if necessary. """
    if not filename:
        return get_contents(path_to_placeholder)
    path_to = str(Path(path_to_dir)/filename)
    if Path(path_to).exists():
        return get_contents(path_to)
    return get_contents(path_to_placeholder)

def get_prose(
        filename,
        path_to_dir=DEFAULT_PATH_TO_PROSE_DIR,
        path_to_placeholder=DEFAULT_PATH_TO_PLACEHOLDER_PROSE
    ):
    """ Return the contents of a file, or return a placeholder if necessary. """
    result = \
        get_poem(
            filename,
            path_to_dir=path_to_dir,
            path_to_placeholder=path_to_placeholder
        )
    return result

def get_prayer(
        filename,
        path_to_dir=DEFAULT_PATH_TO_PRAYER_DIR,
        path_to_placeholder=DEFAULT_PATH_TO_PLACEHOLDER_PRAYER
    ):
    """ Return the contents of a file, or return a placeholder if necessary. """
    result = \
        get_poem(
            filename,
            path_to_dir=path_to_dir,
            path_to_placeholder=path_to_placeholder
        )
    return result

def get_image(
        filename,
        path_to_image_dir=DEFAULT_PATH_TO_IMAGE_DIR,
        path_to_placeholder=DEFAULT_PATH_TO_PLACEHOLDER_IMAGE
    ):
    """ Return the path to a file, or return a placeholder if necessary. """
    result = str(Path(path_to_image_dir)/filename)
    if Path(result).exists():
        return result
    return path_to_placeholder

def get_poems_all_placeholders(path_to=DEFAULT_PATH_TO_PLACEHOLDER_POEM):
    """ Ronseal. """
    result = {
        "autumnal1": get_contents(path_to),
        "autumnal2": get_contents(path_to),
        "hibernal1": get_contents(path_to),
        "hibernal2": get_contents(path_to),
        "vernal1": get_contents(path_to),
        "vernal2": get_contents(path_to),
        "aestival1": get_contents(path_to),
        "aestival2": get_contents(path_to),
        "aestival3": get_contents(path_to)
    }
    return result

def get_prayers_all_placeholders(path_to=DEFAULT_PATH_TO_PLACEHOLDER_PRAYER):
    """ Ronseal. """
    result = {
        "autumnal": get_contents(path_to),
        "hibernal": get_contents(path_to),
        "vernal": get_contents(path_to)
    }
    return result

def get_prose_all_placeholders(path_to=DEFAULT_PATH_TO_PLACEHOLDER_PROSE):
    """ Ronseal. """
    result = {
        "autumnal": get_contents(path_to),
        "hibernal": get_contents(path_to),
        "vernal": get_contents(path_to),
        "aestival": get_contents(path_to)
    }
    return result

def get_images_all_placeholders(path_to=DEFAULT_PATH_TO_PLACEHOLDER_IMAGE):
    """ Ronseal. """
    result = {
        "autumnal": path_to,
        "hibernal": path_to,
        "vernal": path_to,
        "aestival": path_to
    }
    return result
