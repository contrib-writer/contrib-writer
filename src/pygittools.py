import sys, os
import numpy as np
import json
import git as pygit
from datetime import date


def configure_repo():
    _repo = pygit.Repo(os.path.join("../"))
    assert not _repo.bare
    return _repo


def authenticate_github():
    creds = json.load(open(os.path.join("../untracked/credentials.json")))
    return creds

def commit_file(_repo, file):
    _repo.git.add(file)
    _repo.git.commit('-m "add file ' + file + '"')
    return _repo