"""
逻辑接口层
用户接口
"""
from db import db_handler
from lib import common


# 注册接口
def register_interface(username, password, balance=15000):
    # 2）查看用户是否存在
    # 2.1) 调用数据处理层中的select函数，会返回用户字典或None
    user_dic = db_handler.select(username)

    # 若用户存在，则return，告诉用户重新输入
    if user_dic:
        return False, '用户名已存在'

    # 3）若用户不存在，则保存用户数据
    # 做密码加密
    password = common.get_pwd_md5(password)

    # 3.1） 组织用户的数据的字典信息
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        # 用于记录用户流水
        'flow': [],
        # 用与记录用户购物车
        'shop_car': {},
        # locked：用于记录用户是否被冻结
        # False:未冻结     True：已冻结
        'locked': False
    }

    # 3.2）调用数据处理层，保存数据
    db_handler.save(user_dic)
    # 记录用户注册了的日志
    common.user_logger.info(f'{username}注册了')
    return True, f'{username} 注册成功！'


# 登入接口
def login_interface(username, password):
    # 1) 先查看当前用户数据是否存在
    # 调用数据处理层，有则拿到用户数据的字典，没有则是None
    # {用户数据字典} or None
    user_dic = db_handler.select(username)

    # 2）判断用户是否存在
    if user_dic:
        # 给用户输入的密码做一次加密
        password = common.get_pwd_md5(password)

        # 3) 校验密码是否一致
        if password == user_dic.get('password'):

            # 记录用户登入成功日志
            common.user_logger.info(f'{username},登入成功！')
            return True, f'用户：[{username}] 登入成功！'
        else:
            # 记录登录失败日志
            common.user_logger.error(f'{username}登入失败，密码错误')
            return False, '密码错误'
    return False, '用户不存在，请重新输入！'


# 查看余额接口
def check_bal_interface(username):
    # 访问数据处理层，拿到该用户数据字典，通过字典里的key值balance，拿到用户余额
    user_dic = db_handler.select(username)
    # 记录查看余额日志
    common.bank_logger.info(f'{username}查看了余额，此时余额为{user_dic["balance"]}')
    return user_dic['balance']


# 查看用户是否冻结接口
def check_user_lock_interface(username):
    user_dic = db_handler.select(username)
    if user_dic:
        return user_dic['locked']
    return '用户不存在'
