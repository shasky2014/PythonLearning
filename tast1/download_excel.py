def download_wiki_excel(user_info, file_url, save_to_path):
    import requests

    session = requests.session()
    session.auth = (user_info['username'], user_info['password'])
    headers = {'X-Atlassian-Token': 'no-check'}

    r = session.get(file_url, headers=headers)
    print("ok")
    with open(save_to_path, "wb") as f:
        # print(r.content)
        f.write(r.content)
        print('download finished.')


if __name__ == '__main__':
    from urllib.request import quote
    from urllib import parse

    file_url = 'http://wiki.babyfs-inc.cn/download/attachments/13444063/{file_name}?api=v2'
    # print(parse.unquote(file_url))

    save_to_path = '每期见习及新批次1.xlsx'
    # print(parse.quote(save_to_path))
    # print(quote(save_to_path))

    file_url = file_url.format(file_name=save_to_path)

    print(file_url)

    user_info = dict(
        username='wangchenchen',
        password='Shasky201903'
    )

    download_wiki_excel(user_info, file_url, save_to_path)
    pass
