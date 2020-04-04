import json


def fix_date(a):
    import re

    def eval_date(x):
        import datetime
        return '"{}"'.format(eval(x.group(0)))

    bold = re.compile(r'(datetime.datetime\(\d*, \d*, \d*, \d*, \d*, \d*[, \d*]*\))')
    return bold.sub(eval_date, a).replace("'", '"').replace('"{', '{').replace('}"', '}').replace('None', 'null')


a = '{\'ID\': 56618730, \'CreateTime\': datetime.datetime(2019, 5, 20, 18, 8, 43, 843436), \'ExecuteTime\': datetime.datetime(2019, 5, 20, 18, 8, 43), \'OperateType\': \'UPDATE\', \'h_mp_param_ct\': 1557101438278, \'h_station_number\': \'44206\', \'h_invite_uid\': 195664, \'h_sex\': 0, \'h_secretary_wx\': None, \'h_promoter_type\': 0, \'h_is_classic\': 1, \'h_leader_type\': 2, \'h_level_id\': 2, \'h_bank_sub_branch\': \'武汉市黄金山支行\', \'h_ct\': 1507298948662, \'h_mp_param_img_url\': \'http://i.s.babyfs.cn/pro/x/188682/80cd8bddfc5ec0ddd9b0bb7d3d36d919ec271ee2.jpg\', \'h_lead_team_id\': 513, \'h_group_id\': 16, \'h_join_date\': 0, \'h_name\': \'徐雪莉\', \'h_secretary_wx_img_url\': \'http://i.s.babyfs.cn/pro_188682/e109b8bcbdeb4edf9da49667ab035f3d.jpg\', \'h_qr_url\': \'https://m.babyfs.cn/api/m/invite/promoter?pro_id=188682\', \'h_mp_param_expire\': 1559693438278, \'h_ut\': 1558346923700, \'h_position\': 2, \'h_mini_app_img_url\': \'http://i.s.babyfs.cn/pro/y/188682/286fbef587643d106b8438b36be3569f4f0c038f.jpg\', \'h_classic_time\': 0, \'h_address\': \'杨桥湖大道2号阳光100三期1-2-1402\', \'h_del\': 0, \'h_bank_id\': \'6222023202032464165\', \'h_channel\': 0, \'h_id\': 188682, \'h_batch\': \'13批\', \'h_ver\': 0, \'h_mobile\': \'15927423412\', \'h_id_type\': 0, \'h_team_id\': 450, \'h_bank_area_code\': None, \'h_mp_param_url\': \'http://weixin.qq.com/q/02JfBMV4babP_1N-8Txs12\', \'h_conf\': \'{"encodeProId":"0ZV_ec1540dd","hasCheck":1,"proNoticeCodeUrl":"","proNoticeCodeUrlVer":0,"qrCodeUrl":"http://i.s.babyfs.cn/pro_188682/e109b8bcbdeb4edf9da49667ab035f3d.jpg","retailerCodeUrl":"http://i.s.babyfs.cn/pro/x/188682/973d73072f15174d23f4ab309653f072325ce0a0.jpg","sendStat":0}\', \'h_id_card\': \'420802198806272226\', \'h_rank\': 161, \'h_bank_type\': 0, \'h_mother_type\': 0, \'h_stat\': 1, \'h_date_range_id\': 13, \'h_extra\': None, \'h_qr_img_url\': \'http://i.s.babyfs.cn/pro/i/188682/93cc3e67c48bccfc3143d42e92824ddd33034bf0.jpg\', \'h_address_area_code\': \'420115\', \'h_leave_date\': 0, \'h_mini3\': None, \'h_start_flow_time\': None, \'h_end_flow_time\': None}'
print(a)
print(fix_date(a))
print(json.loads(fix_date(a)))

print('=' * 100)
b = dict(a=None, b="", c=" ")
print(b)
bb = json.dumps(b)
print(bb)
print(json.loads(bb))
