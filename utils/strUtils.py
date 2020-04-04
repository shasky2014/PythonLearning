import os
import re

from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE


def illegal_char_rm(str):
    '''
    :param str:
    :return:  str removed the ILLEGAL_CHARACTERS_RE
    '''
    return ILLEGAL_CHARACTERS_RE.sub('', str)


def url_reset(url):
    """
    :param url: 微信提供的头像链接
    :return url: 替换结尾的图片尺寸参数,使用/132为标准尺寸
    """
    import re
    replace_reg = re.compile(r'/\d+$')
    url = replace_reg.sub('/132', url)
    return url


def mkdir(path):
    # 去除首位空格
    path = str_clean(path)
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def str_clean(a):
    if isinstance(a, str):
        b = a.strip('"\'').strip()
        if b == '':
            return None
        else:
            return b
    else:
        return a


def get_int(a='27期'):
    mo = re.search(r'\d+', a)
    if mo:
        return mo.group()
    else:
        return 0


def get_file_name(path):
    """
    :param path: 文件路径
    :return: 文件名, 文件类型

    :Example:
    >>> file_path = '/Users/admin/Documents/工作文件夹/项目/2019/2.18-3.10班长完课率.xlsx'
    >>> f_name,f_type,root_path = get_file_name(file_path)
    >>> print(f_name, f_type,root_path)
    2.18-3.10班长完课率 xlsx /Users/admin/Documents/工作文件夹/项目/2019
    """
    matcher = re.match('(.*?).xlsx', path.split('/')[-1])
    _name = matcher.group(1)
    _root_path = '/'.join(path.split('/')[0:-1])
    return _name, path.split('.')[-1], _root_path


if __name__ == '__main__':
    # print(str_clean(1))
    # print(str_clean("'ssss\t"))
    # print(str_clean("\""))
    # print(str_clean("{\"}"))
    print(get_int('sss28sss'))
    # mkdir('/Users/admin/test')
    file_path = '/Users/admin/Documents/工作文件夹/项目/2019/2.18-3.10班长完课率.xlsx'
    f_name, f_type, root_path = get_file_name(file_path)
    print(f_name, f_type, root_path)
