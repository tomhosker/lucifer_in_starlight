### This code constructs a main.tex for each book of the project, compiling
### the result each time.

# Local imports.
from book1 import Book1
#from book2 import Book2

# Run script.
def run():
  bk1 = Book1()
  bk1.make_replacements()
  bk1.build_pdf()
run()
