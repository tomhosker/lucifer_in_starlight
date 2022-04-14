"""
This code constructs a main.tex for each book of the project, compiling the
result each time.
"""

# Standard imports.
import argparse

# Local imports.
from book1 import Book1
from book2 import Book2

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
        "--force-placeholders-all",
        action="store_true",
        default=False,
        dest="force_placeholders_all",
        help="Replace all content with placeholders"
    )
    result.add_argument(
        "--force-placeholders-poems",
        action="store_true",
        default=False,
        dest="force_placeholders_poems",
        help="Replace all poems with placeholders"
    )
    result.add_argument(
        "--force-placeholders-prayers",
        action="store_true",
        default=False,
        dest="force_placeholders_prayers",
        help="Replace all prayers with placeholders"
    )
    result.add_argument(
        "--force-placeholders-prose",
        action="store_true",
        default=False,
        dest="force_placeholders_prose",
        help="Replace all prose with placeholders"
    )
    result.add_argument(
        "--force-placeholders-images",
        action="store_true",
        default=False,
        dest="force_placeholders_images",
        help="Replace all images with placeholders"
    )
    return result

def run():
    """ Run this file. """
    parser = make_parser()
    arguments = parser.parse_args()
    if arguments.force_placeholders_all:
        for attribute in vars(arguments).keys():
            if not getattr(arguments, attribute):
                setattr(arguments, attribute, True)
    bk1 = Book1(force_placeholders=arguments)
    bk1.build_tex()
    bk1.build_pdf()
    bk2 = Book2()
    bk2.build_tex()
    bk2.build_pdf()

if __name__ == "__main__":
    run()
