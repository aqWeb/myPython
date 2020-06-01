# -*-coding:utf-8-*-
import os

file = "git_version.txt"
file_data = ""
with open(file, "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("#"):
            continue
        else:
            list3 = line.split("|")
            print(list3[1])
