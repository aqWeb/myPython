# encoding = utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
import subprocess
import time
import os

user = 'xxx'
passwd = 'xxx'

# 1.修改xxxgit地址
yr_git = "localhost/base/common/sms.git"
# 2.修改xxxgit版本 参考:localhost/p/55813775801?from=docs&source=docsWeb
branch = 'release/2.1.1'
# 3.修改带同步的模块
model = 'sms'
model_desc = '验证码'

local_base_dir = 'E:/localhost-proj/xx_proj/loanV2.1'
# 4.修改本地对应模块地址
local_model_path = '/base/common'
bat_file = "C:/Users/Q/Desktop/bat/auto_xx_git.bat"
# 5.执行auto_xx_git.bat 进行同步

set_bat_params = {
    "set yr_git": yr_git,
    "set model": model,
    "set branch": branch,
    "set base_dir": local_base_dir,
    "set local_model_path": local_model_path
}


class change_gitlab(object):
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
        self.driver = webdriver.Chrome()
        self.driver.get("http://gitlab.localhost.cn/users/sign_in")
        time.sleep(1)

    def login_gitlab(self):
        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.passwd)
        self.driver.find_element_by_name("commit").click()
        return

    def create_project(self, project_name, desc):
        self.driver.get("localhost/credit/product_source/loanV2.1" + local_model_path)
        self.driver.find_element_by_xpath("//*[@id='content-body']/div[2]/div[1]/div/div[2]/input").click()
        self.driver.find_element_by_xpath("//*[@id='project_path']").send_keys(project_name)
        self.driver.find_element_by_xpath("//*[@id='project_description']").send_keys(desc)
        self.driver.find_element_by_css_selector("#new_project > input.btn.btn-create.project-submit").click()
        time.sleep(2)
        xx_git_url = self.driver.find_element_by_css_selector("#project_clone").get_attribute('value')
        self.deal_local_bat_param(xx_git_url)

    def print_project(self):
        self.driver.get("http://gitlab.localhost.cn/loanV2.1/base/common/sms")
        xx_git_url = self.driver.find_element_by_css_selector("#project_clone").get_attribute('value')
        self.deal_local_bat_param(xx_git_url)

    def deal_local_bat_param(self, git_url):
        set_bat_params['set xx_git'] = git_url
        file_data = ""
        with open(bat_file, "r", encoding="utf-8") as f:
            for line in f:
                # 遍历json替换行首相同
                for (k, v) in set_bat_params.items():
                    # print(str(k) + "=" + str(v))
                    if k in line:
                        line = k + "=" + v + "\n"
                file_data += line
        with open(bat_file, "w", encoding="utf-8") as f:
            f.write(file_data)
        print("设置git同步配置完成,执行auto_xx_git.bat 进行同步")


# test_gitlab = change_gitlab(user, passwd)
# test_gitlab.login_gitlab()
# test_gitlab.create_project(model, model_desc)
# test_gitlab.print_project()


def deal_local_bat_param(git_url):
    set_bat_params['set xx_git'] = git_url
    file_data = ""
    with open(bat_file, "r", encoding="utf-8") as f:
        for line in f:
            # 遍历json替换行首相同
            for (k, v) in set_bat_params.items():
                # print(str(k) + "=" + str(v))
                if line.startswith(k):
                    line = k + "=" + v + "\n"
                    break
            file_data += line
    with open(bat_file, "w", encoding="utf-8") as f:
        f.write(file_data)
    print("设置git同步配置完成,执行auto_xx_git.bat 进行同步")


deal_local_bat_param("localhost/base/common/sms.git")
