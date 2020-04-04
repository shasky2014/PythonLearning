# -*- coding: utf-8 -*-
import datetime
import os
import json
import sys
import requests
from dingtalkchatbot.chatbot import DingtalkChatbot
import pandas as pd
import numpy as np

# print('hello world')
robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=9f148b51cfb68392917e6fc593b5e9f9e8dc14653f4b0d93c30b36db3b433204'
result = pd.read_csv('策略监控.csv')
result['rate'] = result['day_counts_sum'].fillna(0)/result['day_limit_sum']
x = result.to_string(na_rep='\\N',float_format='%.3f',index=False)
print(x)

exit(0)


def send_request(url):
    print(url)
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        print(r.__repr__())
        print('request failed!')
        return 0
    else:
        print(r.status_code)
        print(r.text)
        print('request success!')
        return 1


def dic_list_to_markdown_table(ld):
    md = '|'.join([str(i).rjust(5) for i in list(ld)]) + '\n'
    for l in np.array(ld):
        md = md + '\t|\t'.join([str(x) for x in l]) + '\n'
    print(md)
    return md


dic_list_to_markdown_table(result)
