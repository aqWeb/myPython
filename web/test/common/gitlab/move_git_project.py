# encoding = utf-8
from selenium import webdriver
import os, time, subprocess

user = 'xxx'
passwd = 'xxx'

# 1.修改xxxgit地址
# yr_git = "localhost/base/common/job.git"
# 2.修改带同步的模块
# model = 'job'
# model_desc = '对接xx-XXL-JOB组件'
# 3.修改xxxgit版本
# branch = 'release/2.1.6'

local_base_dir = 'E:/localhost-proj/xx_proj/loanV2.1'
# 4.修改本地对应模块地址
# local_model_path = '/base/common'
bat_file = "C:/Users/Q/Desktop/bat/auto_xx_git.bat"


# 5.执行auto_xx_git.bat 进行同步

def sync_from_local():
    src_file = "git_version.txt"
    with open(src_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                list3 = line.split("|")
                yr_git = list3[0]
                model = list3[1]
                model_desc = list3[2]
                branch = list3[3]
                local_model_path = list3[4]
                set_bat_params = {
                    "set yr_git": yr_git,
                    "set model": model,
                    "set branch": branch,
                    "set base_dir": local_base_dir,
                    "set local_model_path": local_model_path
                }
                test_gitlab = change_gitlab(set_bat_params, user, passwd)
                test_gitlab.login_gitlab()
                test_gitlab.create_project(model, model_desc)
                execute_bat(bat_file)


class change_gitlab(object):
    def __init__(self, param,username, passwd):
        self.username = username
        self.passwd = passwd
        self.param = param
        self.driver = webdriver.Chrome()
        self.driver.get("localhost/users/sign_in")
        time.sleep(1)

    def login_gitlab(self):
        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.passwd)
        self.driver.find_element_by_name("commit").click()
        return

    def create_project(self, project_name, desc):
        self.driver.get("localhost/credit/product_source/loanV2.1" + self.param['set local_model_path'])
        self.driver.find_element_by_xpath("//*[@id='content-body']/div[2]/div[1]/div/div[2]/input").click()
        self.driver.find_element_by_xpath("//*[@id='project_path']").send_keys(project_name)
        self.driver.find_element_by_xpath("//*[@id='project_description']").send_keys(desc)
        self.driver.find_element_by_css_selector("#new_project > input.btn.btn-create.project-submit").click()
        time.sleep(2)
        xx_git_url = self.driver.find_element_by_css_selector("#project_clone").get_attribute('value')
        self.deal_local_bat_param(xx_git_url)

    def print_project(self):
        self.driver.get("localhost/credit/product_source/loanV2.1/base/common/http")
        xx_git_url = self.driver.find_element_by_css_selector("#project_clone").get_attribute('value')
        self.deal_local_bat_param(xx_git_url)

    def deal_local_bat_param(self, git_url):
        set_bat_params = self.param
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


def execute_bat(file):
    os.system('chcp 65001')
    result = subprocess.call(file)
    print(result)


sync_from_local()
# test_gitlab = change_gitlab(user, passwd)
# test_gitlab.login_gitlab()
# test_gitlab.create_project(model, model_desc)
# execute_bat(bat_file)
