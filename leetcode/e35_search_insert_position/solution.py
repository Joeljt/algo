"""35. 搜索插入位置

https://leetcode.cn/problems/search-insert-position/

非递减数组 nums 与 target，返回 target 下标或按升序应插入的位置。

语义：
- 等价于第一个下标 i 使 nums[i] >= target（lower_bound / bisect_left）。
- 存在则返回该下标；不存在则返回「若插入仍保持非递减」的位置（可在尾部，即 len(nums)）。

决定性条件：
- 数组非递减，可在 O(log n) 内用二分，不能线性扫。
- 闭区间写法 `while left <= right`；未命中时不能返回 -1，必须给出插入下标。

不变量（循环中 [left, right] 为候选区间）：
- 真正的插入点始终在 [left, right + 1] 内（闭区间缩小但答案不丢）。
- 每次 `right = mid - 1`：插入点 ≤ mid - 1，故下标 ≥ mid 可排除。
- 每次 `left = mid + 1`：插入点 ≥ mid + 1，故下标 ≤ mid 可排除。
- 循环结束 `left > right`，且 `left == right + 1`：
  下标 < left 的元素均 < target；下标 ≥ left 上若还有元素则 ≥ target（或 left == n）。

步骤：
1. left = 0，right = len(nums) - 1。
2. mid = left + (right - left) // 2；三分支更新边界或命中 return mid。
3. 区间为空时 return left（同 return right + 1）；勿理解成 left/right 谁「更近」。

复杂度：O(log n) 时间，O(1) 额外空间（递归调用栈 O(log n)）。
"""


def search_insert(nums: list[int], target: int) -> int:
    return find(nums, target, 0, len(nums) - 1)

def find(nums, target, left, right) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if target < nums[mid]: 
            # 目标值在左半区，更新右边界
            right = mid - 1
        elif target > nums[mid]:
            # 目标值在右半区，更新左边界
            left = mid + 1
        else:
            # 找到了目标值 所在下标
            return mid
    # 没有找到目标值，标准二分法会返回 -1，我们这里需要找到待插入的位置
    # 循环终止条件是 left <= right，left 是第一个 ≥ target 的位置
    return left