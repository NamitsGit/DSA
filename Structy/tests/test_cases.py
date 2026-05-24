import pytest
from ..Hashing.anagrams_ import anagrams
from ..Hashing.most_frequent_char import most_frequent_char
from ..Hashing.pair_sum import pair_sum
from ..Hashing.pair_product import pair_product


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


@pytest.mark.parametrize("nums, target, expected_result", [
    ([3, 2, 5, 4, 1], 8, (0, 2)),
    ([4, 7, 9, 2, 5, 1], 5, (0, 5)),
    ([4, 7, 9, 2, 5, 1], 3, (3, 5)),
    ([1, 6, 7, 2], 13, (1, 2)),
    ([9, 9], 18, (0, 1)),
    ([6, 4, 2, 8 ], 12, (1, 3)),
    ([5, 4, 1, 4], 8, (1, 3)),
    ([ i for i in range(1, 6001) ], 11999, (5998, 5999))
])
def test_pair_sum(nums, target, expected_result):
    assert pair_sum(nums, target) == expected_result

@pytest.mark.parametrize("nums, target, expected_result", [
    ([3, 2, 5, 4, 1], 8, (1, 3)),
    ([3, 2, 5, 4, 1], 10, (1, 2)),
    ([4, 7, 9, 2, 5, 1], 5, (4, 5)),
    ([4, 7, 9, 2, 5, 1], 35, (1, 4)),
    ([3, 2, 5, 4, 1], 10, (1, 2)),
    ([4, 6, 8, 2], 16, (2, 3)),
    ([ i for i in range(1, 6001) ], 35994000, (5998, 5999))
])
def test_pair_product(nums, target, expected_result):
    assert pair_product(nums, target) == expected_result