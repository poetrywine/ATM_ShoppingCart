"""
数据处理层
    - 专门用来处理数据的
"""
import json
import os
from conf import settings


# 查看数据
def select(username):
    # 1) 接收接口层传过来的username用户名，拼接用户json文件路径
    user_path = os.path.join(
        # 字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式.
        settings.USER_DATA_PATH, f'{username}.json'
    )

    # 2) 校验用户json文件是否存在
    if os.path.exists(user_path):

        # 3） 打开数据，并返回给接口层
        with open(user_path, 'rt', encoding='utf_8') as f:
            user_dic = json.load(f)
            return user_dic

    # 3) 不return，默认return None


# 保存数据（添加新数据或者更新数据）
def save(user_dic):
    # 1) 拼接用户的数据字典
    username = user_dic.get('username')

    # 根据用户的名字，拼接 用户名.json 文件路径
    user_path = os.path.join(
        # 字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式.
        settings.USER_DATA_PATH, f'{username}.json'
    )

    # 2) 保存用户数据
    with open(user_path, 'wt', encoding='utf-8') as f:
        # ensure_ascii=False让文件中的中文数据显示成中文汉字
        json.dump(user_dic, f, ensure_ascii=False)
