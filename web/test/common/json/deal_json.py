# -*-coding:utf-8-*-
json_params = {
    "set model": "framework",
    "set branch": "xx",
    "set xx_git": "xxx",
    "set base_dir": "xxx",
    "set model_path": "/base/common"
}

# 追加元素
json_params['end'] = 'end'
# 遍历json
for k, v in json_params.items():
    print(str(k) + "=" + str(v))

print(json_params['set xx_git'])
