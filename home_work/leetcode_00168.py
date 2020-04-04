# print(65, chr(65))
# print(65 + 20 - 1, chr(20 - 1 + 65))
# print(66, chr(66))


def convertToTitle(n: int) -> str:
    s = ''
    while (n):
        n -= 1
        s = chr(n % 26 + 65) + s
        print(n % 26, s)
        n = n // 26
    return s


if __name__ == '__main__':
    for n in [52]:
        print(n, convertToTitle(n))
