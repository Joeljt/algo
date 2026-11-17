"""21. 合并两个有序链表

https://leetcode.cn/problems/merge-two-sorted-lists/

两个非递减链表 list1、list2，合并为一个非递减链表并返回头结点。

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


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    raise NotImplementedError