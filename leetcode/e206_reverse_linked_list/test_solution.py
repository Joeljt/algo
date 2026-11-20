from __future__ import annotations

import pytest

from leetcode.e206_reverse_linked_list.solution import ListNode, reverse_list


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
    "vals, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_reverse_list(vals, expected):
    head = build_list(vals)
    assert list_values(reverse_list(head)) == expected