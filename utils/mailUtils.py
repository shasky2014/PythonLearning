# coding=utf-8
import datetime
import json
import smtplib
import traceback
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from time import sleep


def _format_addr(s):
    """
    :param s: ['王晨晨<wangchenchen@babyfs.cn>', '王晨晨<wangchenchen@babyfs.cn>']
    :return: ?utf-8?b?546L5pmo5pmo?= <wangchenchen@babyfs.cn>,=?utf-8?b?546L5pmo5pmo?= <wangchenchen@babyfs.cn>
    """
    return ','.join([formataddr(parseaddr(x)) for x in s])


def mail_send(mail_body, mail_group):
    """
    :param mail_body:
    :param mail_group:
    :return:
    """
    # 从mail_body 创建邮件主体
    mb_json = json.loads(mail_body)
    message = MIMEMultipart()

    # 添加邮件的文本内容
    text = mb_json['data']['text']
    textApart = MIMEText(text, 'html', 'utf-8')
    message.attach(textApart)

    # 是否有附件
    for file in mb_json['file']:
        # 创建附件
        fileApart = MIMEApplication(open(file, 'rb').read())
        fileApart.add_header('Content-Disposition', 'attachment', filename=file.split('/')[-1])
        # 添加附件到email
        message.attach(fileApart)

    # 邮件title
    title = mb_json['data']['title']
    message['Subject'] = Header(title, 'utf-8')

    # 邮件抄送、收、发列表
    send_to = _format_addr(mail_group['send_to'])
    send_Cc = _format_addr(mail_group['send_cc'])
    message['To'] = send_to
    message['Cc'] = send_Cc

    mail_user_name = mail_group['mail_user_name']
    mail_user = mail_group['mail_user']
    message['From'] = formataddr((mail_user_name, mail_user))  # '王晨晨<wangchenchen@babyfs.cn>'

    print(mail_user, send_to)
    print(message.as_string())
    mail_host = mail_group['mail_host']  # 设置服务器
    mail_user_pass = mail_group['mail_user_pass']  # 口令

    # 发送尝试次数
    for i in [1, 2, 3]:
        try:
            # 链接登录发送，与网络相关的内容可能都会失败，都需要重启链接
            smtpObj = smtplib.SMTP_SSL(mail_host)
            smtpObj.login(mail_user, mail_user_pass)
            print(','.join([send_to, send_Cc]))
            smtpObj.sendmail(mail_user,
                             mail_group['send_to'] + mail_group['send_cc'] + [mail_group['mail_user']],
                             message.as_string())
            print(datetime.datetime.now(), "邮件发送成功")
            break
        except:
            if i == 3:
                print(datetime.datetime.now(), '第{}次发送失败,返回错误信息'.format(i))
                sleep(0.1)
                raise
            else:
                print(datetime.datetime.now(), '第{}次发送失败，{}秒后重试发送。'.format(i, 30))
                traceback.print_exc()
                sleep(30)
                continue


if __name__ == '__main__':
    mail_body = {'type': '分销数据',
                 'data': {
                     'text': '测试111',
                     'title': 'title 测试111'
                 },
                 'file': []
                 }
    mail_group = {
        'mail_host': "smtp.qiye.163.com",  # 设置服务器
        # 发送者信息，登录验证
        'mail_user': "wangchenchen@babyfs.cn",  # 用send_from
        'mail_user_name': "王晨晨",  # 用send_from
        'mail_user_pass': "Shasky2017",  # wangchenchen口令
        # 接收，抄送列表。没有，给空列表
        'send_to': ['王晨晨<wangchenchen@babyfs.cn>'],
        'send_cc': ['王晨晨<wangchenchen@babyfs.cn>']
    }

    mail_send(json.dumps(mail_body), mail_group)
    # my_addr = '王晨晨<wangchenchen@babyfs.cn>'
    # print(_format_addr(my_addr))
