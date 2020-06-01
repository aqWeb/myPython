# -*-coding:utf-8-*-
# 重发jenkins
import time
from selenium import webdriver
from time import sleep

nowTime = time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))

list = [
    "1.acctcenter",
    "2.acctdayend",
    "3.api-web",
    "4.asset",
    "5.cc",
    "6.convert",
    "7.credit",
    "8.flow",
    "9.gateway",
    "10.job-admin",
    "11.kylin-query",
    "12.market",
    "13.mortgage-pweb",
    "14.mortgage-router",
    "15.platform",
    "16.react",
    "17.router",
    "18.router-web",
    "19.user"
]

user = "tangaq"
password = "tangaq123"
env = "JCCFDC-DEV"
batch = [
    3, 5
]


def _build(i):
    model = list[i - 1].split(".")[1]
    url = "https://jenkins-dev.xxx.com/job/%s/job/LOAN/job/%s" % (env, model)

    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_element_by_name("j_username").send_keys(user)
    driver.find_element_by_name("j_password").send_keys(password)
    driver.find_element_by_name("Submit").click()
    sleep(1)
    driver.find_element_by_link_text("Rebuild Last").click()
    driver.find_element_by_id("yui-gen1-button").click()


for c in batch:
    _build(c)
