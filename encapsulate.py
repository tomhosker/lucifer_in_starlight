"""
This code defines a script which produces a PDF for a poem file at a given path.
"""

# Local imports.
from python import Encapsulator

# Configs.
PATH_TO = "content/poems/book1/afterwards_we.tex"
TITLE = None
OUTPUT_FN = None

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this script. """
    encapsulator = Encapsulator(PATH_TO, title=TITLE, output_fn=OUTPUT_FN)
    encapsulator.make_replacements()
    encapsulator.build_pdf()

if __name__ == "__main__":
    run()
