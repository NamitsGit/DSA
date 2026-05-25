import pytest
from ..Hashing.anagrams_ import anagrams
from ..Hashing.most_frequent_char import most_frequent_char
from ..Hashing.pair_sum import pair_sum
from ..Hashing.pair_product import pair_product
from ..Hashing.intersection import intersection
from ..Hashing.exclusive_items import exclusive_items
from ..Hashing.all_unique import all_unique
from ..Hashing.intersection_with_dupes import intersection_with_dupes


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
    ([6, 4, 2, 8], 12, (1, 3)),
    ([5, 4, 1, 4], 8, (1, 3)),
    ([i for i in range(1, 6001)], 11999, (5998, 5999))
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
    ([i for i in range(1, 6001)], 35994000, (5998, 5999))
])
def test_pair_product(nums, target, expected_result):
    assert pair_product(nums, target) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [
    ([4, 2, 1, 6], [3, 6, 9, 2, 10], [2, 6]),
    ([2, 4, 6], [4, 2], [2, 4]),
    ([4, 2, 1], [1, 2, 4, 6], [1, 2, 4]),
    ([0, 1, 2], [10, 11], []),
    ([i for i in range(0, 50000)], [i for i in range(
        0, 50000)], [i for i in range(0, 50000)])
])
def test_intersection(a, b, expected_result):
    assert intersection(a, b) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [
    ([4,2,1,6], [3,6,9,2,10], [1,3,4,9,10]),
    ([2,4,6], [4,2], [6]),
    ([4,2,1], [1,2,4,6], [6]),
    ([0,1,2], [10,11], [0,1,2,10,11]),
    ([i for i in range(0, 50000)], [i for i in range(
        0, 50000)], [])
])
def test_exclusive_items(a, b, expected_result):
    assert exclusive_items(a, b) == expected_result

@pytest.mark.parametrize("li, expected_result", [
    (["q", "r", "s", "a"], True),
    (["q", "r", "s", "a", "r", "z"], False),
    (["red", "blue", "yellow", "green", "orange"], True),
    (["cat", "cat", "dog"], False),
    (["a", "u", "t", "u", "m", "n"], False)
])
def test_all_unique(li, expected_result):
    assert all_unique(li) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [
    (
        ["a", "b", "c", "b"], 
        ["x", "y", "b", "b"],
        ["b", "b"]
    ),
    (
        ["q", "b", "m", "s", "s", "s"], 
        ["s", "m", "s"],
        ["m", "s", "s"]
    ),
    (
        ["r"], 
        ["p", "r", "r", "r"],
        ["r"],
    ),
    (
        ["t", "v", "u"], 
        ["g", "e", "d", "f"],
        []
    ),
    (
        ["a", "a", "a", "a", "a", "a",], 
        ["a", "a", "a", "a"],
        ["a", "a", "a", "a"]
    )
])
def test_intersection_with_dupes(a, b, expected_result):
    assert intersection_with_dupes(a, b) == expected_result