mail_sender_1 = dict(
    mail_host="smtp.qiye.163.com",
    mail_user="wangchenchen@babyfs.cn",
    mail_user_pass="Shasky2017",
    mail_user_name="王晨晨"
)

mail_group_1 = {
    **mail_sender_1,
    # 接收，抄送列表。没有，给空列表
    'send_to': ['吴琴<wuqin@babyfs.cn>', '许梦梦<xumengmeng@babyfs.cn>'],
    'send_cc': ['卢金平<lujinping@babyfs.cn>', '秦涌<qinyong@babyfs.cn>', '祁奎业<qikuiye@babyfs.cn> ',
                '王晨晨<wangchenchen@babyfs.cn>']
}
print(mail_sender_1)
print(mail_group_1)
