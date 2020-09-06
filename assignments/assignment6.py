"""
Assignment 6: Write some tests for prior assignments

Checklist of tests:
    - New instance is a ConfigDict
    - New instance is also a dict
    - filename passed to init is stored in the _filename attribute
    - a pre-existing file still exists after constructing a new
      instance
    - a new, not-yet-existing file exists after constructing a new
      instnace
    - Bad file path to constructor raises IOError

Instructions: Run `pytest assignment6.py`
"""

import pytest
import os
from assignment4 import ConfigDict, ConfigKeyError

class TestConfigDict(object):

    @pytest.fixture
    def example(self):
        configdict = ConfigDict('config_file.txt')

        return configdict
   
    def test_obj(self, example):
        assert isinstance(example, ConfigDict)
        assert isinstance(example, dict)

    def test_attributes(self, example):
        example._filename

    def test_preexisting_file(self, example):
        assert os.path.isfile('config_file.txt')

    def test_new_file(self):
        if os.path.isfile('config_file.txt'):
            os.system('rm config_file.txt')

        dict1 = ConfigDict('config_file.txt')
        assert os.path.isfile('config_file.txt')
        os.system('rm config_file.txt')

    def test_bad_path(self):
        with pytest.raises(IOError):
            ConfigDict('badpath/config_file.txt')
