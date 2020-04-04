import json

from utils.mailUtils import mail_send

svg_html = open('ssss.svg').read()

# print(svg_html)
mail_html = """
<html>
<body>
<p>This is an HTML paragraph</p>
<p>1:</p>

<p>
<object data="cid:0" width="300" height="100" type="image/svg+xml" codebase="http://www.adobe.com/svg/viewer/install/" />
</p>
<p>2:</p>

<p>
<iframe src="cid:0" width="300" height="100"></iframe>
</p>
<p>3:</p>
<p>
<embed src="cid:0" width="300" height="100" type="image/svg+xml" pluginspage="http://www.adobe.com/svg/viewer/install/" />
</p>
<p>4:</p>
<p><img src="cid:1"></p>

</body>
</html>
""".format(svg_html)

print(mail_html)

# exit(0)
mail_body = {'type': '分销数据',
             'data': {
                 'text': mail_html,
                 'title': 'title 测试111'
             },
             'file': ['ssss.svg', 'banner-a.jpg']
             }
mail_group = {
    'mail_host': "smtp.qiye.163.com",  # 设置服务器
    # 发送者信息，登录验证
    'mail_user': "wangchenchen@babyfs.cn",  # 用send_from
    'mail_user_name': "王晨晨",  # 用send_from
    'mail_user_pass': "Shasky2017",  # wangchenchen口令
    # 接收，抄送列表。没有，给空列表
    'send_to': ['王晨晨<wangchenchen@babyfs.cn>'],
    'send_cc': ['王晨晨<wangchenchen@babyfs.cn>', '王晨晨<249398363@qq.com>']
}

mail_group1 = {
    'mail_host': "smtp.qq.com",  # 设置服务器
    # 发送者信息，登录验证
    'mail_user': "249398363@qq.com",  # 用send_from
    'mail_user_name': "王晨晨",  # 用send_from
    'mail_user_pass': "yimazaixian",  # wangchenchen口令
    # 接收，抄送列表。没有，给空列表
    'send_to': ['王晨晨<249398363@qq.com>'],
    'send_cc': ['王晨晨<249398363@qq.com>']
}
mail_send(json.dumps(mail_body), mail_group)
