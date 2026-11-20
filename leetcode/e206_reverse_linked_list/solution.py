"""206. 反转链表

https://leetcode.cn/problems/reverse-linked-list/

单链表 head，原地反转，返回新头结点。

决定性条件：
- 原地反转：只改 next 指针，不新建结点存一串新链表（除非先练熟再优化）。
- 单链表：每个结点最多一个 next；反转 = 每条边从「指向右」改成「指向左」。

不变量：
- prev：当前已完全反转的那段链表的头（初始 None，表示「已反段」前面没有结点）。
- curr：原链表中下一个待翻转的结点。
- 每轮处理 curr：把它从原链摘下，接到 prev 前面，然后 prev、curr 各向前走一格。

步骤（迭代）：
1. prev = None，curr = head。
2. 当 curr 非空：先 next = curr.next（留住右边）；curr.next = prev；prev = curr；curr = next。
3. 返回 prev（原链最右结点成为新头）。

勿写 next.next = curr：那是去扳「后面的结点」，且未先保存 next.next 会丢链；应改 curr.next = prev。
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

# 反转链表的重点，在于意识到整个流程相比于链表的遍历是相反的过程
# 核心流程大概是：
# 1、确定前一个节点的位置；2、提前取出下一个节点，避免链断开；3、改变指向关系；4、继续向后遍历；
# 整个过程中，因为锚点是前一个节点的位置，所以也并不需要关心头尾节点
# 类似于，初始指针在链表外，然后每次操作完变更才更新指针到刚看完的数据，遍历结束时该指针正好处于原链表末尾，即反转后的链表头
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # 默认在链表外
    prev = None
    # 从当前链表头开始
    curr = head
    # 依次遍历链表
    while curr is not None:
        # 取出下一个节点备用，避免丢失链接信息
        next = curr.next
        # 改变当前节点的链接，指向前一个节点
        curr.next = prev
        # 更新前一个节点为当前节点
        prev = curr
        # 移动指针到下一个节点
        curr = next
    # 遍历结束后，prev 就是原本的链表末尾，即新的链表头
    return prev

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
    reverse_list(build_list([1, 2, 3, 4, 5]))
