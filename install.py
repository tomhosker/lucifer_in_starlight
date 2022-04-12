"""
This code makes the necessary installations to run the other code in this
repository.
"""

# Standard imports.
import os
import shutil
import subprocess
from glob import glob
from pathlib import Path

#############
# FUNCTIONS #
#############

def install_latex():
    """ Ronseal. """
    print("I'm going to need superuser privileges for this bit...")
    subprocess.run(["sudo", "apt-get", "--yes", "install", "texlive-full"])

def install_fonts():
    """ Ronseal. """
    files_to_copy = glob("./fonts/*.ttf")
    destination = str(Path.home()/".fonts")
    if not Path(destination).exists():
        os.mkdir(destination)
    for path in files_to_copy:
        shutil.copy(path, destination)

def install():
    """ Make the necessary installations. """
    install_latex()
    install_fonts()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    install()

if __name__ == "__main__":
    run()
