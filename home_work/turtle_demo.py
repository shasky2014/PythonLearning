import turtle as t

s = t.Screen()  # 也是表示默认画布大小，注意S大写
# s.setup(width=200, height=200)
p = t.Pen()
p.up()
p.speed(0)


def draw_xy(size):
    for x in range(11):
        p.up()
        if x == 10:
            p.goto(-15, x * 10 * size - 5)
        else:
            p.goto(-10, x * 10 * size - 5)
        p.write(x)
        p.goto(0, x * 10 * size)
        p.down()
        p.goto(100 * size, x * 10 * size)
        p.up()

    for x in range(11):
        p.up()
        p.goto(x * 10 * size, -10)
        p.write(x)
        p.goto(x * 10 * size, 0)
        p.down()
        p.goto(x * 10 * size, 100 * size)
        p.up()


def draw_path(size):
    a = (10, 1)
    b = (5, 2)
    c = (7, 4)
    d = (9, 7)
    e = (6, 6)
    f = (3, 8)
    g = (2, 10)

    p.up()
    for ll in [a, b, c, d, e, f, g]:
        x = ll[0] * 10 * size
        y = ll[1] * 10 * size
        p.goto(x, y)
        p.pencolor('red')
        p.up()
        p.goto(x, y - 2)
        p.down()
        p.pensize(3)
        p.circle(2)
        p.up()
        p.goto(x, y)

        p.down()
        p.pensize(1)


size = 3
draw_xy(size)
draw_path(size)

p.up()
p.goto(-20, -20)

print(s.getshapes())
s.mainloop()
