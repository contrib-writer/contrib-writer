# the main script to run when you want to update text
# set up a chron job to execut if desired

import sys, os
import numpy as np
import json
import git as pygit
from datetime import date

import directorytools as dtools
import texttools as ttools
import pygittools as pygtools

n_cells = 7 * 52
n_cells = 7 * 1

# load options
opts = json.load(open(os.path.join("../options.json")))
print(opts)

# setup the file structure
dtools.clear_directory()
dtools.directory_structure(n_cells)

# get the text to write
txt = ttools.placeholder_text()





# todayOrd = date.toordinal(date(1970,1,1))