### This code defines a class, which in turn builds and compiles LaTeX code
### for Book 1 of this project.

# Imports.
import os

# Local imports.
import which_poems
from utilities import compile_tex_from_string

# Local constants.
autumnal_image_ext = "png"
hibernal_image_ext = "png"
vernal_image_ext = "png"
aestival_image_ext = "png"

# The class in question.
class Book1:
  def __init__(self):
    self.tex = None
    self.base = get_contents("book1-base.tex")
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
    self.autumnal_image = get_image("autumnal."+autumnal_image_ext)
    self.hibernal_image = get_image("hibernal."+hibernal_image_ext)
    self.vernal_image = get_image("vernal."+vernal_image_ext)
    self.aestival_image = get_image("aestival."+aestival_image_ext)

  # Replace the tags in the .tex document with the fields created in this
  # class's constructor.
  def make_replacements(self):
    result = self.base
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

  # Build the PDF using XeLaTeX.
  def build_pdf(self):
    compile_tex_from_string(self.tex)
    os.system("mv main.pdf book1.pdf")

# A helper function.
def get_contents(filename):
  f = open(filename, "r")
  result = f.read()
  f.close()
  return result

# Another helper function.
def get_poem(filename):
  if filename == None:
    return get_contents("poems/placeholder_poem.tex")
  else:
    return get_contents("poems/"+filename)

# Another helper function.
def get_prose(filename):
  if os.path.exists("prose/"+filename):
    return get_contents("prose/"+filename)
  else:
    return get_contents("prose/placeholder_prose.tex")

# Another helper function.
def get_image(filename):
  if os.path.exists("images/"+filename):
    return filename
  else:
    return "images/placeholder_image.jpg"
