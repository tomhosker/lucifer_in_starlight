### This code defines a class, which in turn builds and compiles LaTeX code
### for Book 2 of this project.

# Imports.
import os

# Local imports.
import which_poems
from utilities import compile_tex_from_string

# The class in question.
class Book2:
  def __init__(self):
    self.tex = None
