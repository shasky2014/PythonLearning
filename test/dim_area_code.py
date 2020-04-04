import json
import requests

json_url = 'https://s0.babyfs.cn/op/f/1/area/area.min.json'

res = requests.get(json_url, timeout=5)
out_data = json.loads(res.text)

# print(res.text)
# print(out_data)

out_table = []
for c in out_data:
    # print(c)
    for ns in c['ns']:
        if 'ns' in ns:
            for sub_ns in ns['ns']:
                out_table.append([c['c'], c['n'], ns['c'], ns['n'], sub_ns['c'], sub_ns['n']])
                # print(c['c'], c['n'], ns['c'], ns['n'], sub_ns['c'], sub_ns['n'])
        else:
            out_table.append([c['c'], c['n'],c['c'], c['n'], ns['c'], ns['n']])
            # print(c['c'], c['n'],c['c'], c['n'], ns['c'], ns['n'])

print(len(out_table))