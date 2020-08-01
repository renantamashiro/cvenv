import os

from src import cvenv


def test_create_venv():
    virtual_env_name = 'test_venv'
    cvenv.create(virtual_env_name)
    paths = os.listdir()
    assert virtual_env_name in paths

def test_remove_venv():
    cvenv.remove('test_venv')
    paths = os.listdir()
    assert 'test_venv' not in paths

def test_build_venv():
    

def test_default_venv():
    pass
