from dingtalkchatbot.chatbot import DingtalkChatbot
from mysql import connector


def dic_list_to_markdown_table(ld):
    md = '|' + '|'.join([str(i).rjust(5) for i in list(ld[0].keys())]).strip() + '|' + '\n'
    md = md + '|' + '|'.join(['---'] * len(ld[0])) + '|' + '\n'
    for l in ld:
        md = md + '|' + '|'.join([str(i).rjust(5) for i in list(l.values())]).strip() + '|' + '\n'
    print(md)
    return md


conf = dict(host='localhost', port=3306,
            database='ads', charset='utf8',
            user='root', password='1')

conn = connector.connect(**conf)
cux = conn.cursor(dictionary=True)

cux.execute('select * from flask_calendar_data limit 10;')
result = cux.fetchall()
md_text = dic_list_to_markdown_table(result)

msg = {
    "msgtype": "text",
    "text": {
        "content": md_text
    },
    "at": {
        "isAtAll": False
    }
}
# dingtalk api
# https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq#-6
# 已移除
# robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=7c4f33bdba2de720355ee7352665d48140925a9c078c4dbea8a9c61433d9a134'
# 天气哈哈 群
robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=7ab244af7401c6dd876bd192dc4527364961a453411e0700988525c1d66799c0'
xiaoding = DingtalkChatbot(robot_url)
# xiaoding.send_markdown(title='招生时间表', text=md_text, is_at_all=False)
xiaoding.post(msg)
