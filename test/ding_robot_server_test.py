import requests

url = 'https://oapi.dingtalk.com/robot/send?access_token=f8d7f8d8b50cef84627b06ab4324fa97fa3e6911270d1448aab334e875a90a75'
text_json = {
    "msgtype": "text",
    "text": {
        "content": "我就是我,  @13051321230 是不一样的烟火"
    },
    "at": {
        "atMobiles": [
            "13051321230"
        ],
        "isAtAll": False
    }
}

resp = requests.post(url, json=text_json, headers={'content-type': 'application/json'})
print(resp.json())
