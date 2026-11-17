"""704. 二分查找

https://leetcode.cn/problems/binary-search/

非递减数组 nums 与整数 target，存在则返回下标，否则返回 -1。

决定性条件：
- 数组非递减：中点与 target 比大小才能确定答案只可能在左半边或右半边；无序不能这样缩区间。
- 找的是「某个下标」本身，不是「第一个 ≥ target」；与 35、34 的边界写法不同。
- 闭区间写法：初始 left=0、right=len(nums)-1，循环条件 left <= right；若用半开区间 [left, right) 则初始 right=len(nums) 且条件为 left < right，不能混用。

不变量：
- 闭区间 [left, right]：若 target 在数组里出现，其下标一定仍在当前区间内。
- 每轮取 mid，用 nums[mid] 与 target 比；小于则丢弃 mid 及左侧（left = mid + 1），大于则丢弃 mid 及右侧（right = mid - 1），相等则返回 mid。
- left > right 时区间为空，返回 -1。

步骤（主实现 `find` 迭代）：
1. left=0，right=len(nums)-1，一根 while left <= right 搜完，不靠递归缩区间。
2. mid = left + (right - left) // 2（Python 用 // 取下标，勿用 /）。
3. target < nums[mid] → right = mid - 1；target > nums[mid] → left = mid + 1；相等 → 立刻 return mid（不递归）。
4. while 结束仍未命中 → return -1。

与递归版 `search1`：每轮仍只比一次 mid，但小/大时改 left/right 继续循环，而不是 `return _search(..., mid±1, ...)`；思路相同，无调用栈。

复杂度：O(log n) 时间；迭代 O(1) 额外空间，`search1` 递归 O(log n) 栈空间。
"""

def search(nums: list[int], target: int) -> int:
    return find(nums, target, 0, len(nums) - 1)

def find(nums: list[int], target: int, left: int, right: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if target < nums[mid]: right = mid - 1
        elif target > nums[mid]: left = mid + 1
        else: return mid
    return -1

def search1(nums: list[int], target: int) -> int:
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
  assert search([-1, 0, 3, 5, 9, 12], 9) == 4
  assert search([-1, 0, 3, 5, 9, 12], 2) == -1