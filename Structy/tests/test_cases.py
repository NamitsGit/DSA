import pytest
from ..Hashing.anagrams_ import anagrams
from ..Hashing.most_frequent_char import most_frequent_char


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


@pytest.mark.parametrize("s, expected_result", [
    ('bookeeper', 'e'),
    ('david', 'd'),
    ('abby', 'b'),
    ('mississippi', 'i'),
    ('eleventennine', 'e'),
    ('riverbed', 'r')
])
def test_most_frequent_char(s, expected_result):
    assert most_frequent_char(s) == expected_result
