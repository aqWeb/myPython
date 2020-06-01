# -*-coding:utf-8-*-
import json


def format(data):
    return json.dumps(data, ensure_ascii=False, indent=4, separators=(', ', ': '))
