"""141. 环形链表

https://leetcode.cn/problems/linked-list-cycle/

链表 head，判断是否存在环（某个结点的 next 指向前面已出现的结点）。

决定性条件：

不变量：

步骤：
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    raise NotImplementedError