import re

file_path = '/Users/admin/Documents/工作文件夹/项目/2019/2.18-3.10班长完课率.xlsx'
print(file_path)
match = re.match('(.*?).xlsx', file_path.split('/')[-1])
name = ''
if match:
    name = match.group(1)
print(name)


def get_file_name(path):
    import re
    matcher = re.match('(.*?).xlsx', file_path.split('/')[-1])
    f_name = matcher.group(1)
    return f_name, path.split('.')[-1]


print(get_file_name(file_path))
