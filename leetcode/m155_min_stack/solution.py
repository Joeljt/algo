"""155. 最小栈

https://leetcode.com/problems/min-stack/

实现 MinStack：push、pop、top、getMin 均为 O(1)。

不变量：

步骤：
"""

class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass     

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass

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
