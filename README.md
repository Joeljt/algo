# 算法练习

用 Python 手写 LeetCode。数据结构用语言自带的。

题型顺序、每周节奏、过关标准、卡住怎么办，都在 [PLAN.md](PLAN.md)。

## 一道题怎么写

1. 在 `solution.py` 顶部先写**决定性条件**，再写不变量和变量含义（格式见 [PLAN.md](PLAN.md)）。
2. 自己把步骤写成 Python。可以查语法，不要让 AI 把函数写出来。
3. 运行 `.venv/bin/pytest <题目目录>`。
4. 讲解题隔天从空文件在 LeetCode 默写到 AC，才算完成。

## 当前位置

| 状态 | 内容 |
| --- | --- |
| 已完成 | 同向双指针 283、27；滑动窗口 209、3、643；哈希 1、49、128（217 作热身）；对撞指针 167、11、15；区间 56、57、435 |
| 进行中（第 4 周，11/9–11/15） | 栈：[20](leetcode/e20_valid_parentheses/solution.py)、[155](leetcode/m155_min_stack/solution.py)、[739](leetcode/m739_daily_temperatures/solution.py) |
| 复习 | 规则见 [PLAN.md 复习](PLAN.md#复习)。当前 A 级：283、209、1、167、56；B 级：27、3、643、49、128、11、15、57、435 |

模板只建到下一周为止，其余题型到了那一周再建。

## 命令

```bash
python3 -m venv .venv
.venv/bin/pip install "pytest>=7,<9"
.venv/bin/pytest leetcode/m3_longest_substring_without_repeating
```
