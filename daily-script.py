import sys, os
import numpy as np
import json
import git as pygit
from datetime import date

n_cells = 7 * 52

# load options
opts = json.load(open(os.path.join("options.json")))
print(opts)