# -*-coding:utf-8-*-
# 'r'：读
# 'w'：写
# 'a'：追加
# 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
# 'w+' == w+r（可读可写，文件若不存在就创建）
# 'a+' ==a+r（可追加可写，文件若不存在就创建）
# 对应的，如果是二进制文件，就都加一个b就好啦：
# 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = new_str
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)
