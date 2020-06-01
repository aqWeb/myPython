# -*-coding:utf-8-*-
# 重发jenkins
import time
from selenium import webdriver
from time import sleep

jar_list = [
    "biz",
    "biz-impl",
    "dal",
    "dal-impl",
    "common",
    "controller",
    "core",
    "core-impl",
    "facade",
    "test",
    "web"
]

json = {
    "api-web": ["com.hsjry.jcxlf.channel.",
                ["biz", "dal", "controller", "common",
                 "web"]],
    "credit": ["com.hsjry.jcxlf.business.",
               ["biz", "biz-impl", "dal", "dal-impl", "common", "controller", "core", "core-impl", "facade", "test",
                "web"]]
}

model = "credit"
package = json[model][0]
model_package = json[model][1]
repository = "loan2.0_snapshot"

base_url = "https://nexus.xxx.com/#browse/browse:loan2.0_snapshot"
package = package.replace(".", "%2F")

version = "2.1.7-SNAPSHOT"

driver = webdriver.Chrome()
driver.get(base_url)
driver.refresh()
sleep(2)
#  login
driver.find_element_by_id("nx-header-signin-1143-btnInnerEl").click()
driver.find_element_by_name("username").send_keys("loan")
driver.find_element_by_name("password").send_keys("loan")
# login button
driver.find_element_by_link_text("Sign in").click()


# def _del():
#     #  del button
#     driver.find_element_by_xpath("//*[@id='nx-button-1237-btnEl']").click()
#     # no button
#     driver.find_element_by_xpath("//*[@id='button-1007-btnEl']").click()


# for i in model_package:
#     jar = "hsjry-project-{}-{}".format(model, i)
#     jar_url = "{}/#browse/browse:{}:{}{}%2F{}".format(base_url, repository, package, jar, version)
#     print(jar)
#     driver.get(jar_url)
    # _del()
