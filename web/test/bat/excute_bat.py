# -*-coding:utf-8-*-
# https://www.jianshu.com/p/430c411160f8
import subprocess, os

# 解决中文乱码
os.system('chcp 65001')

bat_file = "C:/Users/Q/Desktop/bat/xx.bat"
# 回显结果1.
# input("...")
res1 = subprocess.call(bat_file)
print(res1)

# 回显结果2
# res2 = subprocess.run(bat_file)
# print(res2)
