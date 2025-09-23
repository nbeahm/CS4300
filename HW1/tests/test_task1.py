import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from task1 import helloworld

def helloworldTest():
    assert helloworld() == "hello world!"
helloworldTest()