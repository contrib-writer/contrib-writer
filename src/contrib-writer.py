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
n_cells = 7 * 2


# load options
opts = json.load(open(os.path.join("../options.json")))


# setup the file structure
dtools.clear_directory()
dtools.directory_structure(n_cells)


# get the text to write
_text = ttools.placeholder_text()


# get the pygit repo configured
_repo = pygtools.configure_repo()
# print(_repo.git.status())


# loop through cells to fill out history
background_n_level = opts["background_level"]
for cell in np.arange(n_cells):
    cell_n_variance = np.random.normal(0, opts["background_noise"])
    cell_n_commits = background_n_level + cell_n_variance
    cell_path = os.path.join("cells", str(cell))
    for comm in np.arange(cell_n_commits):
        n_file_name = str(int(comm)) + ".txt"
        n_file_path = os.path.join(cell_path, n_file_name)
        dtools.make_n_file(n_file_path)
        pygtools.commit_file(_repo, os.path.join("src", n_file_path))


# push new status of repository to github
creds = pygtools.authenticate_github()


# todayOrd = date.toordinal(date(1970,1,1))