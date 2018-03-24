# setup script
# this script will make the directories needed and any other housekeeping

import sys, os
import numpy as np
import json
import git as pygit
from datetime import date

n_cells = 7 * 52
n_cells = 7 * 1

# load options
opts = json.load(open(os.path.join("options.json")))
print(opts)

# for every cell
for c in np.arange(n_cells):
    # concatenate the directory that will be used for that date
    c_path = os.path.join("cells", str(c))

    # if there is not a folder already at the path, create it
    if not os.path.isdir(c_path):
        os.system("mkdir " + c_path)





# todayOrd = date.toordinal(date(1970,1,1))