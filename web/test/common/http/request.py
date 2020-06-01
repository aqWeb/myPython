# -*-coding:utf-8-*-
import requests
import json
from datetime import datetime

from web.test.common.json.json_util import format

dt = datetime.now()
now = dt.strftime('%Y-%m-%d %H:%M:%S')


def get_url(url, model):
    url = "%s%s" % (url, model)
    print("url:", url)
    return url


def send_post(req_url, req, headers):
    print("请求时间:%s,入参:%s" % (now, format(req)))
    response = requests.post(req_url, data=json.dumps(req, ensure_ascii=False).encode('utf-8'), headers=headers)
    if response.status_code == 200:
        print("响应:", format(response.json()))
        return response
    else:
        try:
            print("响应:", format(response.json()))
        except:
            print("error 未知响应")
            return
        return response
