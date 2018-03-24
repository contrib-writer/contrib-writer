# setup tools
import sys, os
import numpy as np
import json
import git as pygit
from datetime import date

def clear_directory():
    os.system("rm -rf " + "cells/")

def directory_structure(n_cells):
    os.system("mkdir " + "cells")

    for c in np.arange(n_cells):
        # concatenate the directory that will be used for that date
        c_path = os.path.join("cells", str(c))

        # if there is not a folder already at the path, create it
        if not os.path.isdir(c_path):
            os.system("mkdir " + c_path)