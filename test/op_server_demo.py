from flask import Flask, request
import json, sys

app = Flask(__name__)


@app.route('/internal/util/bi_data_center', methods=['GET'])
def api_test():
    # 解析request请求的参数
    out = json.dumps(request.args,separators=(',',':'))
    print(out)
    # post_data = json.loads(request.data)
    # print(post_data)
    # source = post_data['source']
    # user_info= post_data['user_info']
    return out


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)
        ip = sys.argv[1]
        port = sys.argv[2]
        print('use host:{ip},port:{port}'.format(ip=ip, port=port))
    else:
        ip = '10.10.20.233'
        port = '5000'
        print('default host:{ip},port:{port}'.format(ip=ip, port=port))

    app.debug = True
    app.run(
        host=ip,
        port=port
    )
