### This code constructs a main.tex for each book of the project, compiling
### the result each time.

# Local imports.
from book1 import Book1
from book2 import Book2

####################
# HELPER FUNCTIONS #
####################

# Ronseal.
def make_book1():
  bk1 = Book1()
  bk1.make_replacements()
  bk1.build_pdf()

# Ronseal.
def make_book2():
  bk2 = Book2()
  bk2.add_poems()
  bk2.build_pdf()

##############
# RUN SCRIPT #
##############

def run():
  make_book1()
  #make_book2()
run()
