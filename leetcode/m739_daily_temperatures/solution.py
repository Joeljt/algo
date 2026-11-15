"""739. 每日温度

https://leetcode.com/problems/daily-temperatures/

整数数组 temperatures，answer[i] 为 i 之后要等多少天才有更高温度，没有则为 0。

模型（别写成「固定某天再往后扫」）：
- 只从左到右扫一遍；每一天当作「今天」。
- 不是为下标 i 开内层 j 找更暖日，而是：每当出现更暖的「今天」，顺手给栈里还活着、且比今天冷的那些天写答案。
- 某天的答案一定在它被 pop 的那一刻定下来，那就是它的第一个更暖日。

栈里放什么：
- 下标：这一天之后还没遇到过更高温度，答案未定。
- 从栈底到栈顶：时间越来越晚；温度非严格递减（栈顶在所剩待办里最低或持平）。
- 持平不算更暖，所以相等会一起压在栈里等将来的更暖日。

不变量：
- 处理完下标 i-1 后，栈中每个下标 k 满足：在 (k, i) 内没有任何一天的温度严格大于 temperatures[k]。
- 进入 while 前，若栈非空则 temperatures[i] <= temperatures[栈顶]；while 结束后若栈非空则 temperatures[i] <= temperatures[栈顶]。
- result 里已写入的下标不会再出现在栈里。

步骤：
1. 从左到右看每一天 i；先 while 再 append。
2. 栈非空且 temperatures[i] > temperatures[栈顶]：v = pop()，result[v] = i - v（先 pop 再按下标写，勿写 result[stack[-1]] = i - stack.pop()）。
3. 今天仍可能要等以后 → stack.append(i)。
4. 扫结束后仍留在栈里的下标，后面没有更暖日，保持 result 中的 0。

复杂度：每个下标最多入栈、出栈各一次，O(n) 时间，O(n) 空间。
"""


def daily_temperatures(temperatures: list) -> list:
    result = [0] * len(temperatures)
    stack = []

    # 0、从头查看每一个温度，这是不可避免的
    for i in range(len(temperatures)):

        # 2、容器不为空的情况下，说明前面有尚未找到更高温度的日期
        # 当前的问题是即时解决的，所以容器内的温度都是从低到高排列的，栈顶温度最低
        # 因为如果有比栈顶更高的温度，就直接出栈了
        # 看当前查看的温度是不是比栈顶更高，如果是的话，直接把栈顶温度下标找到
        # 下标对应日期，直接相减就能得到这是第几天之后的值
        # 注意栈内有可能有多个待解决的值，所以需要一直弹栈，直到栈为空再继续
        while stack and temperatures[i] > temperatures[stack[-1]]:
            v = stack.pop()
            result[v] = i - v

        # 1、把当前尚未找到更高温度的下标先存下来，等后面看其他元素的时候求解
        stack.append(i)

    return result

if __name__ == '__main__':
    daily_temperatures([30, 60, 90])