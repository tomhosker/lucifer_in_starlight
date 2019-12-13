### This code defines some utility functions for the project as a whole.

# Imports.
import os

# Takes a tex file - in the form of a string - and compiles it.
def compile_tex_from_string(tex_string):
  f = open("main.tex", "w")
  f.write(tex_string)
  f.close()
  os.system("xelatex main.tex")
  os.system("xelatex main.tex")
  os.system("rm -f main.tex main.aux main.log main.out main.toc")

# Return the contents of a file.
def get_contents(filename):
  f = open(filename, "r")
  result = f.read()
  f.close()
  return result
