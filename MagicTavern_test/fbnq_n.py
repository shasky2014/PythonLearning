def fbnq(n):
    if n <= 2:
        return 1
    if n > 2:
        b = int(str(fbnq(n - 1) + fbnq(n - 2))[-6:])
        return b


if __name__ == '__main__':
    # print(mi_on_2(int(input())))

    print(fbnq(39))
