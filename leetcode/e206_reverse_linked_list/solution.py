"""206. 反转链表

https://leetcode.cn/problems/reverse-linked-list/

单链表 head，原地反转，返回新头结点。

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


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    raise NotImplementedError