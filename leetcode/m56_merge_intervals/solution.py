"""56. 合并区间

https://leetcode.cn/problems/merge-intervals/

区间数组 intervals，合并所有重叠区间，返回不重叠的区间数组。

决定性条件：
- 区间是闭区间，端点碰上就算重叠。[1, 4] 和 [4, 5] 要合成 [1, 5]，所以用 <=。
  [1, 3] 和 [4, 5] 中间有空隙，4 > 3，保持两段。
- 先按起点排序。排好以后，后一个起点不会比前一个起点更小，只拿它和当前终点比。
  不排序的话，[1, 4] 后面的 [0, 4] 起点更小，一遍扫过去会漏。
- 终点取两者里更大的那个。后一段可能整个落在当前区间里，[1, 4] 遇上 [2, 3]，终点仍是 4。

不变量：
- 数组已按起点从小到大排好。
- merged 是当前这一段的拷贝，起点取这段第一个区间的起点，之后只改终点。
  拷贝一份，改终点不会改到原数组，也不会改到已经放进 result 的区间。
- i 指向还没归进 merged 的区间。内层条件是 i 还在数组里，且 intervals[i][0] <= merged[1]。
- 内层停下时，i 停在第一个接不上的区间，或者已经走到末尾。
  外层再 i += 1，下一轮用 intervals[i - 1] 当新一段的起点。少了这一步，下一轮会从已经合并过的区间重读。
- 外层条件是 i <= len(intervals)。i 刚好等于长度时，还要把最后一段放进 result。

步骤：
1. 按每个区间的起点排序。
2. i 从 1 开始。merged 先取 intervals[i - 1]。
3. 后一个起点小于等于 merged 的终点，就把终点更新为 max(merged[1], intervals[i][1])，i 后移，继续看下一段。
4. 接不上了，把 merged 放进 result，i 再加 1，从刚接不上的那个区间开始新的一段。
5. 最后一段没有后继来触发“接不上”，靠 i == len(intervals) 再进一次外层，把它放进 result。

假设 [[1, 3], [2, 6], [8, 10], [15, 18]]，排序后不变：
- merged = [1, 3]。2 <= 3，终点改成 6，i = 2。8 <= 6 不成立，加入 [1, 6]，i = 3。
- merged = [8, 10]。15 <= 10 不成立，加入 [8, 10]，i = 4。
- i = 4 时等于长度，merged = [15, 18]，没有下一段，加入 [15, 18]。
结果是 [[1, 6], [8, 10], [15, 18]]。
"""

from copy import deepcopy


def merge(intervals: list) -> list:
    result = []
    intervals.sort(key=lambda i: i[0])

    index = 0
    while index < len(intervals):
        merged = deepcopy(intervals[index])
        # 从 0 开始，但是直接开始看下一个元素，更符合直觉
        index += 1
        while index < len(intervals) and intervals[index][0] <= merged[1]:
            merged[1] = max(merged[1], intervals[index][1])
            index += 1
        result.append(merged)

    return result

def merge1(intervals: list) -> list:
    
    result = list()
    
    # 对原数组基于第一个元素进行排序
    intervals.sort(key=lambda interval: interval[0])

    i = 1
    merged = []

    while i <= len(intervals):

        # 从前一个元素开始
        merged = [intervals[i - 1][0], intervals[i - 1][1]]

        # 如果当前区间的起点 <= 合并区间的终点
        # 只要还满足重叠条件，就继续向后检查
        while i < len(intervals) and intervals[i][0] <= merged[1]:
            # 扩大合并区间的右边界为最新的区间
            # 注意这里要对区间的边界取 max，而不是一味地用当前数组，因为有可能是个完全的子区间
            merged[1] = max(merged[1], intervals[i][1])
            # 移动指针到下一个元素
            i += 1
        
        # 直到不再满足条件，得到一个完整的区间，加入结果集
        result.append(merged)
        i += 1

    return result

if __name__ == "__main__":
    v = merge([[1, 4], [2, 3]])
    print(v)

