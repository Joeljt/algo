"""435. 无重叠区间

https://leetcode.cn/problems/non-overlapping-intervals/

区间数组 intervals，返回移除区间的最小数量，使剩余区间互不重叠。

决定性条件：
- 按终点升序排。结束得晚的排到后面，宽区间 [1, 100] 就是因为终点晚才到末尾。
  按起点排会先留下宽区间，把后面能留下的短区间一起删掉。按长度排则失去位置，没法判断谁和谁重叠。
- 端点相接不算重叠。[1, 2] 和 [2, 3] 都留下，所以用 <。56 题端点相接要合并，用的是 <=。
- 重叠时删正在看的后一段，已经留下的界限不动。
  后一段的终点不会更早，换成它只会把界限推后。界限是下一段要跨过的高度，越早越容易接上。
  能跨过更晚界限的，本来也能跨过更早的界限。起点落在两个终点之间的，只有界限停得更早才留得下。

不变量：
- 数组已按终点从小到大排好。还没看到的区间，终点都不会更早。
- current 是最近留下的区间。比较只用它的终点。
- i 指向还没处理的区间。内层条件是 i 还在数组里，且 intervals[i][0] < current[1]。
- 内层停下时，i 停在第一个接得上的区间，或者已经走到末尾。
  外层下一轮直接用 intervals[i] 当新的 current。这里不用再加 1。

步骤：
1. 按每个区间的终点排序。
2. 外层取 current = intervals[i]，i 后移。这段留下。
3. 下一段起点 < current 的终点，就删掉，计数加 1，i 后移，继续看下一段。
4. 接上了，回到外层，从这段开始当新的界限。
5. 答案是删掉的个数。

假设 [[1, 100], [11, 22], [1, 11], [2, 12]]，按终点排成 [[1, 11], [2, 12], [11, 22], [1, 100]]：
- current = [1, 11]。2 < 11，删掉 [2, 12]。11 < 11 不成立。
- current = [11, 22]。1 < 22，删掉 [1, 100]。
删掉 2 个。
"""

def erase_overlap_intervals(intervals: list) -> int:
    # 按区间终点进行排序
    intervals.sort(key=lambda i: i[1])

    # 然后遍历各个区间，比较区间起点，发现重叠的时候，保留更靠前的区间
    i = 0
    count = 0
    while i < len(intervals):
        current = intervals[i]
        i += 1

        # 比较下一个区间的起点与当前区间的终点，检查是否有重叠
        while i < len(intervals) and intervals[i][0] < current[1]:
            count += 1
            i += 1

    return count

def erase_overlap_intervals1(intervals: list) -> int:
    # 先对原数组进行排序
    intervals.sort(key=lambda i: i[0])

    # 遍历排序后的数组，检查是否存在重叠
    i = 0
    count = 0
    while i < len(intervals):
        current = intervals[i]
        i += 1

        # 这个逻辑有问题，如果排序以后前面有一个大区间，就会把后面的小区间都删掉
        # 这道题要的是最小移除的数量，所以这个解法不对
        while i < len(intervals) and intervals[i][0] >= current[0] and intervals[i][0] < current[1]:
            count += 1
            i += 1
    
    return count

if __name__ == '__main__':
    v = erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]])
    print(v)
