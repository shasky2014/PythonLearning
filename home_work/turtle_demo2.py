import turtle as t

s = t.Screen()  # 也是表示默认画布大小，注意S大写
s.bgcolor('brown')

p = t.Pen()
p.up()


p.goto(-200, -200)
p.down()
p.circle(50)

p.up()
p.goto(-200, -160)
p.down()
p.pencolor('blue')
p.pensize(19)
p.circle(10)

p.up()
p.goto(-200, -166)
p.down()
p.pencolor('white')
p.pensize(5)
p.circle(16)

p.up()
p.goto(-20, -20)


# a = [[-70,-70],[-90,-85],[-90,-55],[-70,-70]]
# for ll in a:
#     x = ll[0]
#     y = ll[1]
#     p.goto(x, y)
#     p.down()

p.up()
p.goto(-20, -20)

s.register_shape("triangle", ((5,-3),(0,5),(-5,-3)))
s.mainloop()
