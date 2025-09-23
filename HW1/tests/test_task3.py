import pytest
import sys
import os
sys.setrecursionlimit(20000)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from task3 import numberCheck, printprimes, sum100

def numberCheckTest():
    assert numberCheck(-1) == "number is negative"
def printprimesTest():
    prime = [1,3,5,7,11,13,17,19,23,29]
    assert printprimes() == prime
    #reaches recusionlimit, tried setting it higher to no avail
def sum100Test():
    assert sum100Test() == 5050
numberCheckTest()
printprimesTest()
sum100Test()