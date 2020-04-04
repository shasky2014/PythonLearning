a = ['6.14.2', '6.7.1', '10.2.1', '10.2.13', '9.2']

z = '4321'
print(z, z[-1:], z[-3:])


def avt(aversion):
    v_no_l = aversion.split('.')
    a1 = v_no_l[0]
    a2 = ('000' + v_no_l[1])[-3:]
    if len(v_no_l) == 3:
        a3 = ('000' + v_no_l[2])[-3:]
    # elif len(v_no_l) > 3:
    # 有四位版本号，第四版本号有字母
    #     a4 = v_no_l[3]
    else:
        a3 = '000'
    return int('{0}{1}{2}'.format(a1, a2, a3))


for version in a:
    print('{0:<10}{1:10}'.format(version, avt(version)))
