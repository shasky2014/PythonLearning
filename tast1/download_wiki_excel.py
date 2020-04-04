# from urllib import request

url = 'http://wiki.babyfs-inc.cn/download/attachments/13444063/%E6%96%B0%E5%85%B5%E8%90%A5%E9%A1%BE%E9%97%AE%E5%90%8D%E5%8D%95.xlsx?api=v2'
file_path = '新兵营顾问名单.xlsx'

# import urllib3
# urllib3

# request.urlretrieve(url, file_path)


# import requests
# # url="http://hjwachhy.site/game/only_v1.1.1.apk"
# # path="only.apk"
#
# r=requests.get(url)
# print("ok")
# with open(file_path,"wb") as f:
#     f.write(r.content)
# f.close()
import requests


def main():
    # Change the following to work with your Confluence instance including any context path
    base_url = 'http://wiki.babyfs-inc.cn/'
    username = 'wangchenchen'
    password = 'Shasky201903'
    # End change block

    session = requests.session()

    session.auth = (username, password)

    headers = {'X-Atlassian-Token': 'no-check'}
    print(url)
    print(headers)

    r = session.get(url, headers=headers)
    print("ok")
    with open(file_path, "wb") as f:
        print(r.content)
        f.write(r.content)


main()

user_info = dict(
    username='wangchenchen',
    password='Shasky201903'
)


def download_wiki_excel(user_info,file_url,save_to_path):
    import requests

    session = requests.session()
    session.auth = (user_info['username'], user_info['password'])
    headers = {'X-Atlassian-Token': 'no-check'}

    r = session.get(file_url, headers=headers)
    print("ok")
    with open(save_to_path, "wb") as f:
        print(r.content)
        f.write(r.content)
