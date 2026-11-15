"""155. 最小栈

https://leetcode.com/problems/min-stack/

实现 MinStack：push、pop、top、getMin 均为 O(1)。

决定性条件：
- 不能在 getMin 里扫栈，四个操作都要 O(1)。
- pop 只能动栈顶，不能在 pop 之后丢失「剩余元素中的最小值」；最小值必须随 push/pop 同步维护。
- 面试默写优先 MinStack2（元组）或 MinStack1（辅助栈）；本文件主类 MinStack 为 diff 空间优化，易错在 push 次序。

三种写法（不变量相同：任意时刻 getMin 等于当前栈内真实最小值）：
- MinStack1：主栈 + 辅助栈，每层压入 min(当前值, 辅助栈顶)，双栈同步 pop。
- MinStack2：单栈存 (值, 当时最小)，getMin 读栈顶元组第二项。
- MinStack（diff）：单栈存 val - 压栈前 min；另维护全局 min。负 diff 表示该次 push 刷新了 min。

diff 不变量：
- 栈中每格 d 对应该层真实值 v：d < 0 时 v = 当前 min；d >= 0 时 v = 压栈时的 min + d（解码用当前 min + d）。
- push 必须先 append(val - min_value)，再 min_value = min(min_value, val)；先改 min 会压成 0 而非负 diff，pop 无法回滚。
- pop：仅 d < 0 时 min_value -= d（等价 min_value -= min(d, 0)）；d >= 0 只弹栈不改 min。
- 首元素：压 0，min_value = val。

步骤（diff）：
1. push：空栈压 0 并设 min；否则压 val - min，再更新 min。
2. pop：按上式维护 min 后 pop。
3. top：d < 0 返回 min；否则 min + d。
4. getMin：返回 min_value。
"""

from math import inf


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_value = inf

    def push(self, val: int) -> None:
        # diff = val - 压栈前的 min；先压 diff，再更新 min（顺序反了会丢负 diff）
        if not self.stack:
            self.stack.append(0)
            self.min_value = val
        else:
            self.stack.append(val - self.min_value)
            self.min_value = min(self.min_value, val)

    def pop(self) -> None:
        # 仅当 diff < 0 时表示当时刷新了 min，弹栈时把 min 倒回：min -= diff
        self.min_value -= min(self.stack[-1], 0)
        self.stack.pop()

    def top(self) -> int:
        # d >= 0：真实值 = min + d；d < 0：这一格就是当时的 min（即现在的 min）
        if self.stack[-1] < 0:
            return self.min_value
        return self.min_value + self.stack[-1]

    def get_min(self) -> int:
        return self.min_value

# 基于元组实现，思路与辅助栈类似，但是不需要额外的 O(n) 开销
class MinStack2:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # 不使用辅助栈，但是同样的思路，直接把插入时已知的最小值同步存下来
        # 当需要的时候直接从栈顶元组里取值即可，没有额外的 O(n) 空间开销
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]


# 辅助栈
class MinStack1:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 借助辅助栈实现 get_min 的 O(1) 操作
        # 与真实 stack 同步操作，只在栈顶记录当前已知的最小值，并在 pop 时一起维护，保证始终与主栈同步
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]

if __name__ == '__main__':
    st = MinStack()
    st.push(-2)
    st.push(0)
    st.push(-3)
    assert st.get_min() == -3
    st.pop()
    assert st.top() == 0
    assert st.get_min() == -2