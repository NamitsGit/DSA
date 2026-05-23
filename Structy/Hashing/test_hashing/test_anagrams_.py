import pytest
from ..anagrams_ import anagrams

def test_anagrams():
    assert anagrams('restful', 'fluster') == True
    assert anagrams('cats', 'tocs') == False
    assert anagrams('monkeyswrite', 'newyorktimes') == True
    assert anagrams('monkeyswrite', 'newyorktimes') == True
    assert anagrams('paper', 'reapa') == False
    assert anagrams('elbow', 'below') == True
    assert anagrams('tax', 'taxi') == False
    assert anagrams('taxi', 'tax') == False
    assert anagrams('night', 'thing') == True
    assert anagrams('abbc', 'aabc') == False
    assert anagrams('po', 'popp') == False
    assert anagrams('pp', 'oo') == False


