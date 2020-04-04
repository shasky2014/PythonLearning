"""
一个典型的电话拨号盘如下：

1 2 3
4 5 6
7 8 9
* 0 #

手指在两个按键之间的移动距离被定义成这两个键的x、y坐标差的绝对值之和。比如，6到自身的距离是0，到3、5、9的距离是1，到2、4、8、#的距离是2，到1、7、0的距离是3，到*的距离是4。
现在要你算一下，拨一个号手指所需要移动的最小距离是多少？假设手指初始位置在“5”。

输入
一行，一个字符串，表示需要拨的电话号码。

输入约束
电话号码的每一位仅包含数字“0”到“9”，且总长度范围是 [3,20]

输出
一个整数，表示拨完这个号码手指最少需要移动的距离

例子
输入
911
输出
6
"""


def distence_1(a, b):
    return abs(a['x'] - b['x']) + abs(a['y'] - b['y'])


def num_xy(m):
    n = str(m)

    if n == '1':
        xy = dict(x=-1, y=1)
    elif n == '2':
        xy = dict(x=0, y=1)
    elif n == '3':
        xy = dict(x=1, y=1)

    elif n == '4':
        xy = dict(x=-1, y=0)
    elif n == '5':
        xy = dict(x=0, y=0)
    elif n == '6':
        xy = dict(x=1, y=0)

    elif n == '7':
        xy = dict(x=-1, y=-1)
    elif n == '8':
        xy = dict(x=0, y=-1)
    elif n == '9':
        xy = dict(x=1, y=-1)

    elif n == '0':
        xy = dict(x=0, y=-2)
    elif n == '#':
        xy = dict(x=1, y=-2)
    elif n == '*':
        xy = dict(x=-1, y=-2)

    else:
        print('error')
        raise
    return xy


def get_end_dist(str_1):
    all_dist = 0
    bf_char = 5
    for char in str_1:
        all_dist = all_dist + distence_1(num_xy(bf_char), num_xy(char))
        print(bf_char, char, distence_1(num_xy(bf_char), num_xy(char)), all_dist)
        bf_char = char
    return all_dist


if __name__ == '__main__':
    import sys

    line = str(sys.stdin.readline()).strip()

    print(get_end_dist(line))
