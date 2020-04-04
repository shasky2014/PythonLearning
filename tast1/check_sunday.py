import datetime

s = """
ds=20190726
ds=20190727
ds=20190728
ds=20190729
ds=20190730
ds=20190731
ds=20190801
ds=20190802
ds=20190803
ds=20190804
ds=20190805
ds=20190806
ds=20190807
ds=20190808
ds=20190809
ds=20190810
ds=20190811
ds=20190812
ds=20190813
ds=20190814
ds=20190815
ds=20190816
ds=20190817
ds=20190818
"""

ds_list = s.strip().replace('ds=', '').split('\n')
print(ds_list)


def is_sunday(ds='20190818'):
    today = datetime.datetime.strptime(ds, '%Y%m%d')
    # print(today.weekday())
    return today.isoweekday() == 7
    pass


# print(list(map(is_sunday, ds_list)))
# print(is_sunday())

# sunday_list = [x if is_sunday(x) else None for x in ds_list]
# print(sunday_list)

print(list(filter(is_sunday, ds_list)))

print(','.join(map(str,list(range(1, 55555)))))
