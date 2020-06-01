# -*-coding:utf-8-*-
from web.test.common.file.read_property import get_propety
from web.test.common.http.request import send_post, get_url
from datetime import datetime
import os

from web.test.get_header import get_header

dt = datetime.now()
today = dt.strftime('%Y%m%d')
transDateTime = dt.strftime('%Y-%m-%d %H:%M:%S')

print("当前路径 -> %s" % os.getcwd())
serialNo = dt.strftime('%Y%m%d%H%M%S%f')

channel = get_propety("channel")
tenantId = get_propety("tenantId")
token = get_propety("token")
url = "http://localhost:8080"

header = get_header()

model = "/api/v1/bankcard/queryBankCardList"
url = get_url(url, model)

data = {}

send_post(url, data, header)
