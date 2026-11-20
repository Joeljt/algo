from __future__ import annotations

import pytest

from leetcode.e21_merge_two_sorted_lists.solution import ListNode, merge_two_lists


def build_list(vals: list[int]) -> ListNode | None:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def list_values(head: ListNode | None) -> list[int]:
    out: list[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_merge_two_lists(a, b, expected):
    assert list_values(merge_two_lists(build_list(a), build_list(b))) == expected