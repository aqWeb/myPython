# -*-coding:utf-8-*-
import time
from datetime import datetime

from web.test.common.file.read_property import get_propety

dt = datetime.now()
today = dt.strftime('%Y%m%d')
transDateTime = dt.strftime('%Y-%m-%d %H:%M:%S')

serialNo = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
channel = get_propety("channel")
tenantId = get_propety("tenantId")
token = get_propety("token")


def get_header():
    head = {
        "Content-Type": "application/json",
        "channelNo": "06",
        "requestSerialNo": serialNo,
        "requestTime": serialNo,
        "tenantId": tenantId,
        "token": token,
        "Rpc-Hsjry-Request": "ask=934&answer=921&serialNo=%s&idemSerialNo=%s&serviceScene=11&transDateTime=%s&tenantId=%s&channelNo=%s" % (
            serialNo, serialNo, transDateTime, tenantId, channel),
        "Rpc-Hsjry-User-Request": "authId=admin&token=%s&operatorId=admin&organId=000ORG00000000006&&operatorName=admin" %(token)
    }
    return head
