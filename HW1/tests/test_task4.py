import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from task4 import discountCalc

def discountCalcTest():
    assert discountCalc(50, .40) == 30.0
discountCalcTest()