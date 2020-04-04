"""
描述
请使用递归的方式判断一个给定的整数是否为2的整数次幂。
提示：当一个数 n = 2^k （k为非负整数）时，我们说n是2的整数（k）次幂。比如 2、4、8、16都是2的整数次幂，但3、7、14就不是。

输入
一行，一个正整数n

输入约束：
1<=n<=2^31

输出
一行，数字1或0。
如果输入为2的整数次幂，则输出1，否则输出0。
"""
def mi_on_2(n):
    if n < 1 or n >= 2 ** 32:
        return 'out of range'
    if n == 2:
        return 1
    if n == 1:
        return 0

    if n % 2 == 0:
        return mi_on_2(n / 2)
    else:
        return 0


if __name__ == '__main__':
    # print(mi_on_2(int(input())))

    print(2 ** 0)

    import sys
    line = sys.stdin.readline()
    n = int(line)
    print(mi_on_2(n))