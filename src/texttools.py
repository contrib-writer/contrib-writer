import sys, os
import numpy as np
import json
import git as pygit
from datetime import date

def placeholder_text():
    mat = np.zeros((7, 52))
    mat[3, :] = 1
    return mat