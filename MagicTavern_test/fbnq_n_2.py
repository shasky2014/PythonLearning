"""
假设n为正整数，斐波那契数列定义为：
f(n) = 1, n < 3;
f(n) = f(n-1) + f(n-2), n>=3

现在请你来计算f(n)的值，但是不需要给出精确值，只要结果的后六位即可。

输入：一行，包含一个正整数n，且0<n<1000
输出：一行，f(n)的后6位（十进制，不足6位不补零）
"""
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        # print(a, end=' ')
        a, b = b, a + b
    return str(a)[-6:]

if __name__ == '__main__':
    # print(mi_on_2(int(input())))

    print(fib(6))
