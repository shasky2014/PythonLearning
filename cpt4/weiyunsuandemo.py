import json

map_list = dict({1: "缺少招生群助手", 2: "缺少话术助手", 4: "机器人心跳不正常", 8: "近似满员", 32: "群二维码过期", 64: "满员", 128: "二维码分享者中不在群中"})
map_json = json.dump(map_list, fp=(',', ":"))
print(map_json)


def state_explode_list(a):
    a_explore = []
    for n, _one in enumerate(str(bin(a)).replace('0b', '')):
        if _one == '1':
            x_bin_str = _one + ''.join(['0'] * (len(str(bin(a)).replace('0b', '')) - n - 1))
            a_explore.append(int(x_bin_str, 2))
    return a_explore


def state_explode_map(a, map_json):
    map_list = dict({1: "缺少招生群助手", 2: "缺少话术助手", 4: "机器人心跳不正常", 8: "近似满员", 32: "群二维码过期", 64: "满员", 128: "二维码分享者中不在群中"})

    a_explore = {}
    for n, _one in enumerate(str(bin(a)).replace('0b', '')):
        if _one == '1':
            x_bin_str = _one + ''.join(['0'] * (len(str(bin(a)).replace('0b', '')) - n - 1))
            a_explore[int(x_bin_str, 2)] = map_list[int(x_bin_str, 2)]
    return a_explore


bb = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 32, 33, 34, 35, 36, 38, 40, 64, 66, 67, 70, 72, 74, 128, 129, 130, 131,
      133,
      135, 136, 137, 139, 161, 163, 167, 169, 171, 200]
for b in bb:
    print(b, state_explode_list(b))

print('-' * 100)

a = 163
print(int('11111111', 2))
print(map_list)
# print(a & 4 == 2)
print(map_list[2])

print(1 | 2)
print(1 | 4)

# print(bin(a))
print(str(bin(a)).replace('0b', ''))

for i in map_list.keys():
    print(str(bin(i)).replace('0b', ''), map_list[i])
