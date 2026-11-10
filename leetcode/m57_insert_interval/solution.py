"""57. 插入区间

https://leetcode.cn/problems/insert-interval/

不重叠且按区间起点升序排列的区间列表 intervals，以及新区间 newInterval。
把 newInterval 插入列表，使结果仍不重叠且有序（必要时合并）。

决定性条件：
- 原列表已经按起点升序，且彼此不重叠。一遍扫过去只会碰到三段：完全在新区间左边的、和它相交的连续一段、剩下的右边。
- 闭区间，端点相接算重叠。[1, 5] 和 [5, 7] 要合成 [1, 7]。
  左边的判断是当前终点 < new 起点。相交的判断是当前起点 <= merged 终点。
- merged 从 new 的拷贝开始，这段合并完只放进结果一次。
  没有区间和它相交时，放进去的就是 new 自己。空列表、插在最左边、最右边、夹在空隙里，都是这次放入。
- 起点取两者里更小的，终点取两者里更大的。new 可能从一段中间插进来，[1, 5] 遇上 [0, 3]，起点要留 0。

不变量：
- i 左边的区间已经放进 result，或者已经并进 merged。
- 第一段停下时，i 停在第一个终点不小于 new 起点的区间，或者已经走到末尾。
- 第二段里 merged 盖住 new 和已经并进来的区间。起点只减不增，终点只增不减。
- 第二段停下时，后面每个区间的起点都大于 merged 的终点。它们原来互不重叠，接上去仍然有序。

步骤：
1. 当前终点 < new 起点，原样放进 result，i 后移。
2. merged 先取 new 的拷贝。当前起点 <= merged 终点，起点改为 min，终点改为 max，i 后移，直到这段相交结束。
3. 把 merged 放进 result。
4. i 后面剩下的区间原样接上。

假设 [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]，插入 [4, 8]：
- [1, 2] 的终点 2 < 4，放入 [1, 2]，i = 1。
- merged = [4, 8]。3 <= 8，并成 [3, 8]。6 <= 8，仍是 [3, 8]。8 <= 8，终点改成 10。12 <= 10 不成立。
- 放入 [3, 10]。剩下 [12, 16] 原样接上。
结果是 [[1, 2], [3, 10], [12, 16]]。
"""

def insert(intervals: list, new_interval: list) -> list:
    result = []
    i = 0

    # 先找所有位于 new 左侧的数据，直接原样复制即可
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 从这里开始处理合并的数据，条件就是目标区间的左边界和 new 的右边界哪个更大
    # 比如某个区间的起点刚好是 new 的终点，那就应该合并到一起
    merged = [new_interval[0], new_interval[1]]
    while i < len(intervals) and intervals[i][0] <= merged[1]:
        merged[0] = min(merged[0], intervals[i][0])
        merged[1] = max(merged[1], intervals[i][1])
        i += 1
    result.append(merged)

    # 剩下的说明完全在 new 右侧，直接拼接即可
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result

# 无法处理空数组或者完全在原数组区间右侧的场景，现有循环会丢数据
def insert0(intervals: list, new_interval: list) -> list:
    result = []
    i = 0
    while i < len(intervals):
        if intervals[i][1] < new_interval[0] or intervals[i][0] > new_interval[1]:
            # 当前子区间的右边界比待插入区间的左边界更小，说明没有重叠，直接插入
            # 当前子区间的左边界比待插入区间的右边界更大，说明完全在待插入区间右侧，直接插入
            result.append(intervals[i])
            i += 1
        else:
            # 当前子区间的右边界比待插入区间的左边界大，说明有重叠，开始找可合并区间
            merged = [intervals[i][0], intervals[i][1]]
            while i < len(intervals) and (intervals[i][1] <= new_interval[1] or intervals[i][0] <= new_interval[1]):
                merged[1] = max(intervals[i][1], new_interval[1])
                i += 1
            result.append(merged)

    return result


def insert1(intervals: list, new_interval: list) -> list:
    """左边原样拷贝，相交段并进 new 的拷贝，这份拷贝只放入一次，右边原样接上。"""
    result = []
    i = 0

    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    merged = [new_interval[0], new_interval[1]]
    while i < len(intervals) and intervals[i][0] <= merged[1]:
        merged[0] = min(merged[0], intervals[i][0])
        merged[1] = max(merged[1], intervals[i][1])
        i += 1
    result.append(merged)
    result.extend(intervals[i:])
    return result


if __name__ == "__main__":
    v = insert( [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8])
    print(v)
