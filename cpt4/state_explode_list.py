def state_explode_list(arg0):
    arg0_bin = bin(arg0).replace('0b', '')
    # print(arg0_bin, type(arg0_bin))
    a_explore = []
    for n, _one in enumerate(arg0_bin):
        if _one == '1':
            x_bin_str = _one + ''.join(['0'] * (len(arg0_bin) - n - 1))
            a_explore.append(int(x_bin_str, 2))
    return '|'.join([str(x) for x in a_explore])


# bb = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 32, 33, 34, 35, 36, 38, 40, 64, 66, 67, 70, 72, 74, 128, 129, 130, 131,
#       133, 135, 136, 137, 139, 161, 163, 167, 169, 171, 200]
# for b in bb:
#     print(b, state_explode_list(b))


print(31, '=', state_explode_list(31), '=', eval(state_explode_list(31)))
# print(16|8|4|2|1)
