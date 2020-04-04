# -*- coding: utf-8 -*-
import os
import sys
import requests
from dingtalkchatbot.chatbot import DingtalkChatbot
from mysql import connector

lib_path = os.path.abspath(os.path.join('../pylib'))
print(lib_path)
sys.path.append(lib_path)


# from utils import mysqlInit,conf
# from utils.conf import sys_rds_db
#

def get_today_record_info():
    sql = '''
	SELECT t.level_id, l.`name`,
        count(1) as pro_cn,
        count(case when start_flow_time< unix_timestamp(date_format(DATE_SUB(curdate(), INTERVAL -1 DAY), '%Y%m%d')) * 1000
   	and end_flow_time> unix_timestamp(date_format(DATE_SUB(curdate(), INTERVAL -1 DAY), '%Y%m%d')) * 1000 then 1 else null end) as record_pro_cn
  	from `babyfs_v2`.`t_promoter` t
  	left join `babyfs_v2`.`t_promoter_level` l on t.`level_id`= l.`id`
 	WHERE 1= 1
   	and stat= 1
 	group by t.level_id,l.`name`
    '''
    conf = dict(host='localhost', port=3306,
                database='ads', charset='utf8',
                user='root', password='1')

    conn = connector.connect(**conf)
    cux = conn.cursor(dictionary=True)
    cux.execute(sql)

    result = cux.fetchall()
    print('result:', result)
    return result


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
    md = '|'.join([str(i).rjust(5) for i in list(ld[0].keys())]) + '\n\n'
    md = md + '|'.join(['---'] * len(ld[0])) + '\n\n'
    for l in ld:
        md = md + '|'.join([str(i).rjust(5) for i in list(l.values())]) + '\n\n'
    print(md)
    return md


def low_rate_warning(warning_rate, crm_url, robot_url):
    r = get_today_record_info()
    r_with_openflag = []
    for i in r:
        open_flag = 0
        i['record_rate'] = round(i['record_pro_cn'] * 1.0 / i['pro_cn'], 2)
        if i['record_rate'] <= warning_rate.get(i['name'], -1):
            # print(crm_url+str(i['level_id']))
            open_flag = send_request(crm_url + str(i['level_id']))
        i['open_flag'] = open_flag
        r_with_openflag.append(i)

    # Text消息@所有人
    # xiaoding.send_text(msg=str(r), is_at_all=True)
    if r_with_openflag:
        xiaoding = DingtalkChatbot(robot_url)
        markd = dic_list_to_markdown_table(r_with_openflag)
        # xiaoding.send_markdown(title='推广人签到率告警', text=markd,is_at_all=True)
        xiaoding.send_text(msg=str(markd), is_at_all=True)


if __name__ == '__main__':
    ## 告警阈值
    # warning_rate = 0.8
    warning_rate = {'47期分配优先级D': 0.7,
                    '48期优先级A': 0.7,
                    '48期优先级B': 0.7,
                    '48期优先级C': 0.7,
                    '48期优先级D': 0.7,
                    '48期优先级E': 0.7,
                    'B': 0.7,
                    'C': 0,
                    'D': 0,
                    'E': 0,
                    '非精品先锋兼职承接': 1.0,
                    '全职账号回收': 1.0,
                    '西安全职100': 1.0,
                    '西安全职200': 1.0,
                    '西安全职250': 1.0,
                    '新模式测试': 0}
    # 正式op
    # crm_url = 'https://op.babyfs.cn/op/activity/sync_bi_data?code=1111&level_id='
    # 测试op
    crm_url = 'http://op.lpt.babyfs.cn/op/activity/sync_bi_data?code=1111&level_id='
    # 正式
    # robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=08aca349233848d7e52343c11b84a72b7bd940c847eaf20e7587d2b612d5e2c1'
    # 测试
    robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=7afc64300b2f3dedae6e2771d5685d11dc0a274f6dbe24304cfee15606f263b1'

    low_rate_warning(warning_rate, crm_url, robot_url)

    pass
