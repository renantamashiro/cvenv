import os
import sys
import venv


def create(name_venv: str):
    venv.create(name_venv)    

def remove(name_venv: str):
    venv.shutil.rmtree(name_venv)

def build():
    pass

def default():
    pass

