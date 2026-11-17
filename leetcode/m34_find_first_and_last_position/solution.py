"""34. 在排序数组中查找元素的第一个和最后一个位置

https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

非递减数组 nums 与 target，返回 [first, last]；不存在则返回 [-1, -1]。

语义：
- 不能「找到 nums[mid]==target 就 return」：重复元素时 mid 可能是区间中间任意一个。
- 拆成两次边界二分：左 = 第一个 >= target；右 = 最后一个 == target（或第一个 > target 的前一位）。

决定性条件：
- 与 704 不同：要整段重复值的起止，不是任意一个命中下标。
- 与 35 不同：相等时不能 return mid，要继续缩区间找最左 / 最右。
- 左边界不存在则整题不存在，不必再求右边界（可剪枝）。

不变量（闭区间 [left, right]，记 F = 第一个下标 i 使 nums[i] >= target）：
- lower_bound：∀ i < left, nums[i] < target；∀ i > right, nums[i] >= target；F 始终在 [left, right] 内。
- `nums[mid] < target` → left = mid + 1；`nums[mid] >= target` → right = mid - 1（含相等，因 F 可能在 mid 左侧）。
- 结束 left > right 且 right = left - 1 ⇒ left = F；存在 target 当且仅当 left < n 且 nums[left] == target。

右边界（找最后一个 target，等价于第一个 > target 的 left，答案为 right = left - 1）：
- `nums[mid] > target` → right = mid - 1；`nums[mid] <= target` → left = mid + 1（含相等，因最右可能在 mid 右侧）。
- 结束若 right >= 0 且 nums[right] == target，则 right 为右端点。

步骤：
1. first = lower_bound(...)；若 first == -1 返回 [-1, -1]。
2. last = upper_bound(...)（本文件函数名为右端点语义，非「第一个 > target 的下标」本身）。
3. 返回 [first, last]。

复杂度：两次 O(log n)，共 O(log n) 时间与 O(1) 额外空间（递归版栈 O(log n)）。
"""


def search_range(nums: list[int], target: int) -> list[int]:
    lower = lower_bound(nums, target, 0, len(nums) - 1)
    if lower == -1:
        # 剪枝，左侧都没有找到，说明数组里没有 target，不必浪费右端检查
        return [-1, -1]
    upper = upper_bound(nums, target, 0, len(nums) - 1)
    return [lower, upper]

def lower_bound(nums, target, left, right) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            # 找左边界，找到等于向前元素的值时，不停止循环，继续向下二分
            # 直到不满足条件跳出：right = left - 1
            right = mid - 1
    return left if left < len(nums) and nums[left] == target else -1

def upper_bound(nums, target, left, right) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return right if right >= 0 and nums[right] == target else -1

if __name__ == '__main__':
    print(search_range([2, 2], 3))