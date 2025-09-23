import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from task2 import addInt, subtractInt, multiplyInt, addFloats, addStrings

def addIntTest():
    assert addInt(4, 5) == 9
def subtractIntTest():
    assert subtractInt(4, 5) == -1
def multiplyIntTest():
    assert multiplyInt(4, 5) == 20
def addFloatsTest():
    assert addFloats(4.5, 5.3) == 9.8
def addStringsTest():
    assert addStrings("I love", " coding") == "I love coding"
addIntTest()
subtractIntTest()
multiplyIntTest()
addFloatsTest()
addStringsTest()