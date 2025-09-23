import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from task6 import fileRead, wordcount
file = open("task6_read_me.txt")
text = file.read()
def fileReadTest():
    assert fileRead("task6_read_me.txt") == text

def wordcountTest():
    assert wordcount("task6_read_me.txt") == 127
fileReadTest()
wordcountTest()