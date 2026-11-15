"""704. 二分查找

https://leetcode.com/problems/binary-search/

非递减数组 nums 与整数 target，存在则返回下标，否则返回 -1。

决定性条件：
- 数组非递减：中点与 target 比大小才能确定答案只可能在左半边或右半边；无序不能这样缩区间。
- 找的是「某个下标」本身，不是「第一个 ≥ target」；与 35、34 的边界写法不同。
- 闭区间写法：初始 left=0、right=len(nums)-1，循环条件 left <= right；若用半开区间 [left, right) 则初始 right=len(nums) 且条件为 left < right，不能混用。

不变量：
- 闭区间 [left, right]：若 target 在数组里出现，其下标一定仍在当前区间内。
- 每轮取 mid，用 nums[mid] 与 target 比；小于则丢弃 mid 及左侧（left = mid + 1），大于则丢弃 mid 及右侧（right = mid - 1），相等则返回 mid。
- left > right 时区间为空，返回 -1。

步骤：
1. left=0，right=len(nums)-1。
2. 当 left <= right：mid = left + (right - left) // 2（Python 用 // 取下标，勿用 /）。
3. target < nums[mid] → 只搜右界改为 mid-1；target > nums[mid] → 左界 mid+1；相等 → 返回 mid。
4. 未找到 → -1。

复杂度：每轮区间减半，O(log n) 时间，O(1) 额外空间（若用迭代）；递归写法为 O(log n) 栈空间。
"""


def search(nums: list[int], target: int) -> int:
    return _search(nums, target, left=0, right=len(nums) - 1)

def _search(nums: list[int], target: int, left: int, right: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            return _search(nums, target, left, mid - 1)
        elif target > nums[mid]:
            return _search(nums, target, mid + 1, right)
        else:
            return mid
    return -1

if __name__ == '__main__':
    search([5], 5)