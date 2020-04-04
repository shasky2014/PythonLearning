#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from tkinter import *
root = Tk()
root.title('我是root窗口')
l=Label(root,text='我属于root')
l.pack()

f=Toplevel(root,width=30,height=30)
f.title('我是toplevel窗口')
lf = Label(f,text='我是TopLevel')
lf.pack()
root.mainloop()