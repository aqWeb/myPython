# -*-coding:utf-8-*-
import os
# 获取根路径
root_path = os.path.abspath(os.path.dirname(__file__)).split('web')[0]
config_file = root_path + "/web/test/config/config"
spilt = "="


def get_propety(propety):
    result = None
    with open(config_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            if line.startswith(propety):
                lists = line.split(spilt)
                result = lists[1].strip("\n")
                return result
        if result is None:
            print("未找到%s配置" % propety)


def get_propetyByFile(localFile, propety):
    result = None
    with open(localFile, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            if line.startswith(propety):
                lists = line.split(spilt)
                result = lists[1].strip("\n")
                return result
        if result is None:
            print("未找到%s配置" % propety)
