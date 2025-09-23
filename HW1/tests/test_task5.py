import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from task5 import printList, returndict

def printListTest():
    assert printList(["hunger games catching fire by Suzanne Collins", "Eragon by Christopher Paolini", "Throne of glass by Sarah J maas", "The false prince by Jennifer A. Nielsen", "Dragon run by Patrick Matthews"]) == ["hunger games catching fire by Suzanne Collins", "Eragon by Christopher Paolini", "Throne of glass by Sarah J maas"]
def dictTest():
    assert returndict() == {"Nathan B": 12033, "Joe A": 19225, "Ella P": 45921, "Tanner B": 23491, "Lukas S": 67292}
printListTest()
dictTest()