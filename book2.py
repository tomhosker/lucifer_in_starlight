### This code defines a class, which in turn builds and compiles LaTeX code
### for Book 2 of this project.

# Imports.
import os

# Local imports.
import which_poems
from utilities import compile_tex_from_string, get_contents

# The class in question.
class Book2:
  def __init__(self):
    self.tex = None
    self.base = get_contents("book2-base.tex")

  # Add the poems to the .tex document.
  def add_poems(self):
    result = self.base
    the_poems = ""
    for filename in which_poems.book2:
      poem = Poem(filename)
      the_poems = the_poems+poem.printout+"\n\n"
    result = result.replace("#THE_POEMS", the_poems)
    self.tex = result

  # Build the PDF using XeLaTeX.
  def build_pdf(self):
    compile_tex_from_string(self.tex)
    os.system("mv main.pdf book2.pdf")

# A helper class, this handles the properties of a poem.
class Poem:
  def __init__(self, filename):
    self.filename = filename
    self.title = self.parse_title()
    self.body = get_contents("poems/book2/"+filename)
    self.printout = self.get_printout()

  # Converts a filename into a title.
  def parse_title(self):
    minus_extension = self.filename[:self.filename.index(".tex")]
    result = ""
    for character in minus_extension:
      if character == "_":
        result = result+" "
      else:
        result = result+character
    return result

  # Generates a LaTeX printout from the other fields.
  def get_printout(self):
    result = "\\chapter*{"+self.title+"}\n\n"+self.body
    return result
