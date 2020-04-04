# import sys
#
# import openpyxl
#
# l=[1,2,4]
# print(l)
# print(len(l))
# # print('\udc1d')
# s=u'\udc1d'.encode('UTF-8', 'replace')
# print(s)
# # print('\udc1d'.decode('utf8','replace'))
#
# def creatwb(wbname):
#     wb=openpyxl.Workbook()
#     wb.save(filename=wbname)
#     print ("新建Excel："+wbname+"成功")
# creatwb('sss.xlsx')
import os
import sys

import openpyxl

input_file = '/Users/admin/PycharmProjects/pygui/xxxx.xlsx'
f = os.open(input_file)

print(f)

wb = openpyxl.load_workbook(filename=input_file, read_only=True)
ws = wb.active
print(ws)
