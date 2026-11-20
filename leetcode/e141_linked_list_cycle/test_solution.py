from __future__ import annotations

import pytest

from leetcode.e141_linked_list_cycle.solution import ListNode, has_cycle


def build_cyclic_list(vals: list[int], pos: int) -> ListNode | None:
    """pos >= 0 时 tail.next 指向下标 pos 的结点；pos == -1 表示无环。"""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


@pytest.mark.parametrize(
    "vals, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
    ],
)
def test_has_cycle(vals, pos, expected):
    assert has_cycle(build_cyclic_list(vals, pos)) == expected