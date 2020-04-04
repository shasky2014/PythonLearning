#!/usr/local/bin/python3
import argparse
import math
import os
import sys

version = '0.0.1'
"""
> split -help
split: illegal option -- h
usage: split [file] [-l line_count] [-x pattern]
"""


def split_by_line(file, n=5000, x=2):
    open_file = open(file, mode='r')
    os.path
    file_con = open_file.readlines()
    # print(file_con.__sizeof__())
    for i in range(math.ceil(len(file_con) / n)):
        # print(i, 0 + i * n, (1 + i) * n)
        out_name = ('{}_{:0>' + str(x) + 'd}.{}').format(file.split('.')[0], 1 + i, file.split('.')[-1])
        print(out_name)
        f = open(out_name, 'w')
        f.writelines(file_con[i * n:(1 + i) * n])
        # print(file_con[i * n:(1 + i) * n].__sizeof__())
        f.close()
    pass


def split_by_byte():
    pass


if __name__ == '__main__':
    # action = 'help', default = SUPPRESS,
    # help = _('show this help message and exit')
    # print(sys.argv)
    # file_name = sys.argv[1]
    # file_split(file_name)

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help='file you want split')
    parser.add_argument('-l', '--line_count', help='split by line count')
    parser.add_argument('-b', '--byte_count', help='split by byte count')
    # parser.add_argument("prefix", help='outer file prefix')
    # parser.add_argument("postfix", help='outer file postfix')
    args = parser.parse_args()
    if args.line_count:
        print(sys.argv)
        split_by_line(args.file, n=int(args.line_count))
    # if args.byte_count:
    #     print(args.byte_count)
