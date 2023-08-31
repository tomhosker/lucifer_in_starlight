"""
This code constructs a main.tex for each book of the project, compiling the
result each time.
"""

# Standard imports.
import argparse

# Local imports.
from python import Book1, Book2

##############
# RUN SCRIPT #
##############

def make_parser():
    """ Return a parser argument. """
    result = \
        argparse.ArgumentParser(
            description="Compile the documents"
        )
    result.add_argument(
        "--preserve-tex-files",
        action="store_true",
        default=False,
        dest="preserve_tex_files",
        help="Preserve the .tex files used to build the PDFs"
    )
    return result

def run():
    """ Run this file. """
    parser = make_parser()
    arguments = parser.parse_args()
    bk1 = Book1(preserve_tex_file=arguments.preserve_tex_files)
    bk1.build_tex()
    bk1.build_pdf()
    bk2 = Book2(preserve_tex_file=arguments.preserve_tex_files)
    bk2.build_tex()
    bk2.build_pdf()

if __name__ == "__main__":
    run()
