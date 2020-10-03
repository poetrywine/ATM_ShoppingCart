""""
存放公共方法
"""
import hashlib
from logging import config, getLogger
from conf import settings


# md5加密
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '一二三四五，上山打老虎!'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()


# 登入认证装饰器
def login_auth(func):
    # 不要在文件开头导入，在函数里面导入是为了避免循环导入问题
    from core import src

    def inner(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('未出示证明，无法享受美好的功能服务！')
            src.login()
    return inner


# 记录日志
config.dictConfig(settings.LOGGING_DIC)
user_logger = getLogger('用户日志')
bank_logger = getLogger('银行日志')
shop_logger = getLogger('购物日志')
admin_logger = getLogger('管理员日志')

