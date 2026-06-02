import pytest

from ..Linked_List.sum_list import Node, sum_list
from ..Linked_List.linked_list_find import linked_list_find
from ..Linked_List.get_node_value import get_node_value
from ..Linked_List.reverse_list import reverse_list


def test_sum_list():
    # TEST CASE 1
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    assert sum_list(a) == 19

    # TEST CASE 2
    x = Node(38)
    y = Node(4)
    x.next = y
    assert sum_list(x) == 42

    # TEST CASE 3
    z = Node(100)
    # 100
    assert sum_list(z) == 100

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

node1 = Node("jason")
node2 = Node("leneli")
node1.next = node2

node3 = Node(42)
linked_list_find(node3, 42)

@pytest.mark.parametrize("head, target, expected_result", [
    (a, "c", True),
    (a, "d", True),
    (a, "d", True),
    (node1, "leneli", True),
    (node3, 42, True),
    (node3, 100, False)

])
def test_linked_list_find(head, target, expected_result):
    assert linked_list_find(head, target) == expected_result

@pytest.mark.parametrize("head, index, expected_result", [
    (a, 2, "c"),
    (a, 3, "d"),
    (a, 7, None),
    (node1, 0, "jason"),
    (node3, -1, None),

])
def test_get_node_value(head, index, expected_result):
    assert get_node_value(head, index) == expected_result

rev1 = Node("a")
rev2 = Node("b")
rev3 = Node("c")
rev4 = Node("d")
rev1.next = rev2
rev2.next = rev3
rev3.next = rev4

rev2_1 = Node(1)
rev2_2 = Node(2)
rev2_3 = Node(3)
rev2_4 = Node(4)

rev2_1.next = rev2_2
rev2_2.next = rev2_3
rev2_3.next = rev2_4

rev3_1 = Node(1)

@pytest.mark.parametrize("head, expected_result", [
    (rev1, rev4),
    (rev2_1, rev2_4),
    (rev3_1, rev3_1),
])
def test_reverse_list(head, expected_result):
    assert reverse_list(head) == expected_result
