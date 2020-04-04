import json, time

map_list = dict({1: "缺少招生群助手", 2: "缺少话术助手", 4: "机器人心跳不正常", 8: "近似满员", 32: "群二维码过期", 64: "满员", 128: "二维码分享者中不在群中"})
map_list_str = json.dumps(map_list, ensure_ascii=False)
print(type(map_list_str), map_list_str)

print('-' * 100)
time.sleep(0.1)


def state_explode_map(a, map_list_str):
    map_list = json.loads(map_list_str)
    # print(map_list)
    a_explore = {}
    for n, _one in enumerate(str(bin(a)).replace('0b', '')):
        if _one == '1':
            x_bin_str = _one + ''.join(['0'] * (len(str(bin(a)).replace('0b', '')) - n - 1))
            # print(int(x_bin_str, 2),x_bin_str)
            a_explore[str(int(x_bin_str, 2))] = map_list[str(int(x_bin_str, 2))]
    return a_explore


bb = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 32, 33, 34, 35, 36, 38, 40, 64, 66, 67, 70, 72, 74, 128, 129, 130, 131,
      133, 135, 136, 137, 139, 161, 163, 167, 169, 171, 200]
for b in bb:
    print(b, state_explode_map(b, map_list_str))
