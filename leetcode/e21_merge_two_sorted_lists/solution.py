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

    dummy = ListNode(0) 
    tail = dummy
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # while list1 is not None:
    #     tail.next = list1
    #     list1 = list1.next
    #     tail = tail.next

    # while list2 is not None:
    #     tail.next = list2
    #     list2 = list2.next
    #     tail = tail.next

    # list1 / list2 只剩下最后一段了，直接改变指向即可，不再需要遍历
    tail.next = list1 if list1 is not None else list2

    return dummy.next


def build_list(vals: list[int]) -> ListNode | None:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

if __name__ == '__main__':
    merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))