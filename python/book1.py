"""
This code defines a class which builds and compiles LaTeX code for Book 1 of
this project.
"""

# Standard imports.
from dataclasses import dataclass
from pathlib import Path

# Local imports.
from .utils import (
    MAIN_FN_STEM,
    OUTPUT_EXTENSION,
    PATH_OBJ_TO_ROOT,
    compile_tex_from_string,
    get_contents,
    get_which
)

# Local constants.
WHICH_BK1 = get_which()["book1"]
# Path objects.
PATH_OBJ_TO_TEX_DIR = PATH_OBJ_TO_ROOT/"tex"
PATH_OBJ_TO_BK1_POEMS_DIR = PATH_OBJ_TO_ROOT/"content"/"poems"/"book1"
PATH_OBJ_TO_PRAYERS_DIR = PATH_OBJ_TO_ROOT/"content"/"prayers"
PATH_OBJ_TO_PROSE_DIR = PATH_OBJ_TO_ROOT/"content"/"prose"
PATH_OBJ_TO_IMAGES_DIR = PATH_OBJ_TO_ROOT/"content"/"images"
# Paths.
PATH_TO_BASE = str(PATH_OBJ_TO_TEX_DIR/"book1_base.tex")
PATH_TO_PACKAGE_CODE = str(PATH_OBJ_TO_TEX_DIR/"package_code.tex")
PATH_TO_PLACEHOLDER_POEM = str(PATH_OBJ_TO_ROOT/"poems"/"placeholder_poem.tex")
PATH_TO_PLACEHOLDER_PRAYER = \
    str(PATH_OBJ_TO_PRAYERS_DIR/"placeholder_prayer.tex")
PATH_TO_PLACEHOLDER_PROSE = str(PATH_OBJ_TO_PROSE_DIR/"placeholder_prose.tex")
PATH_TO_PLACEHOLDER_IMAGE = str(PATH_OBJ_TO_IMAGES_DIR/"placeholder_image.png")
# Tex snippets.
POEM_CODE_BEGIN = (
    "\\begin{figure*}[p!]\n"+
    "\\bigskip\n"+
    "\\ding{72}\n"+
    "\\bigskip\n"
)
POEM_CODE_END = "\\end{figure*}"
PRAYER_CODE_BEGIN = (
    "\\bigskip\n"+
    "\\centering \\ding{58}\n"+
    "\\bigskip\n"+
    "\\begin{quote}\n"
)
PRAYER_CODE_END = "\\end{quote}"

##############
# MAIN CLASS #
##############

@dataclass
class Book1:
    """ The class in question. """
    preserve_tex_file: bool = False
    # Generated fields.
    tex: str = None
    base: str = None
    package_code: str = get_contents(PATH_TO_PACKAGE_CODE)
    poems: list = None
    prayers: list = None
    prose: list = None
    images: list = None

    def __post_init__(self):
        self.base = get_contents(PATH_TO_BASE)
        self.poems = self.get_poems()
        self.prayers = self.get_prayers()
        self.prose = self.get_prose()
        self.images = self.get_images()

    def get_poems(self):
        """ Fetch the desired poems from disk. """
        poem_dir = PATH_OBJ_TO_BK1_POEMS_DIR
        result = {
            "autumnal1": get_poem(str(poem_dir/WHICH_BK1["autumnal1"])),
            "autumnal2": get_poem(str(poem_dir/WHICH_BK1["autumnal2"])),
            "hibernal1": get_poem(str(poem_dir/WHICH_BK1["hibernal1"])),
            "hibernal2": get_poem(str(poem_dir/WHICH_BK1["hibernal2"])),
            "vernal1": get_poem(str(poem_dir/WHICH_BK1["vernal1"])),
            "vernal2": get_poem(str(poem_dir/WHICH_BK1["vernal2"])),
            "aestival1": get_poem(str(poem_dir/WHICH_BK1["aestival1"])),
            "aestival2": get_poem(str(poem_dir/WHICH_BK1["aestival2"])),
            "aestival3": get_poem(str(poem_dir/WHICH_BK1["aestival3"]))
        }
        for key in result:
            result[key] = POEM_CODE_BEGIN+result[key]+POEM_CODE_END
        return result

    def get_prayers(self):
        """ Fetch the desired poems from disk. """
        prayers_dir = PATH_OBJ_TO_PRAYERS_DIR
        result = {
            "autumnal": get_prayer(str(prayers_dir/"autumnal.tex")),
            "hibernal": get_prayer(str(prayers_dir/"hibernal.tex")),
            "vernal": get_prayer(str(prayers_dir/"vernal.tex"))
        }
        for key in result:
            result[key] = PRAYER_CODE_BEGIN+result[key]+PRAYER_CODE_END
        return result

    def get_prose(self):
        """ Fetch the desired prose passages from disk. """
        prose_dir = PATH_OBJ_TO_PROSE_DIR
        result = {
            "autumnal": get_prose(str(prose_dir/"autumnal.tex")),
            "hibernal": get_prose(str(prose_dir/"hibernal.tex")),
            "vernal": get_prose(str(prose_dir/"vernal.tex")),
            "aestival": get_prose(str(prose_dir/"aestival.tex"))
        }
        return result

    def get_images(self):
        """ Fetch the desired paths to images from disk. """
        result = {
            "autumnal": get_chapter_image("autumnal"),
            "hibernal": get_chapter_image("hibernal"),
            "vernal": get_chapter_image("vernal"),
            "aestival": get_chapter_image("aestival")
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
        """ Build the PDF. """
        compile_tex_from_string(
            self.tex,
            preserve_tex_file=self.preserve_tex_file
        )
        Path(MAIN_FN_STEM+OUTPUT_EXTENSION).rename("book1"+OUTPUT_EXTENSION)

####################
# HELPER FUNCTIONS #
####################

def get_content(path_to_actual, path_to_placeholder):
    """ Return the contents of a file, or return a placeholder if necessary. """
    if path_to_actual and Path(path_to_actual).exists():
        return get_contents(path_to_actual)
    print("Could not find: "+str(path_to_actual))
    return get_contents(path_to_placeholder)

def get_poem(path_to):
    """ Return the contents of a file, or return a placeholder if necessary. """
    return get_content(path_to, PATH_TO_PLACEHOLDER_POEM)

def get_prose(path_to):
    """ Return the contents of a file, or return a placeholder if necessary. """
    return get_content(path_to, PATH_TO_PLACEHOLDER_PROSE)

def get_prayer(path_to):
    """ Return the contents of a file, or return a placeholder if necessary. """
    return get_content(path_to, PATH_TO_PLACEHOLDER_PRAYER)

def get_chapter_image(stem):
    """ Return the path to a file, or return a placeholder if necessary. """
    if not stem:
        return PATH_TO_PLACEHOLDER_IMAGE
    for path_obj in Path(PATH_OBJ_TO_IMAGES_DIR).glob(stem+".*"):
        result = str(path_obj)
        return result
    return PATH_TO_PLACEHOLDER_IMAGE
