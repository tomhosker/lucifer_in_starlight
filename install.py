"""
This code makes the necessary installations to run the other code in this
repository.
"""

# Standard imports.
import shutil
from pathlib import Path

# Non-standard imports.
from hosker_utils import install_apt_package

#############
# FUNCTIONS #
#############

def install_fonts():
    """ Ronseal. """
    path_obj_to_source = Path(__file__).parent/"fonts"
    path_obj_to_dest = Path.home()/".fonts"
    path_objects_to_copy = path_obj_to_source.glob("*.ttf")
    path_obj_to_dest.mkdir(parents=True, exist_ok=True)
    for path_obj in path_objects_to_copy:
        shutil.copy(str(path_obj), str(path_obj_to_dest))

def install():
    """ Make the necessary installations. """
    install_apt_package("texlive-full")
    install_fonts()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    install()

if __name__ == "__main__":
    run()
