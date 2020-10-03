"""
管理员逻辑接口
"""
from db import db_handler
from lib import common


# 添加账户接口
def add_user_interface(username, password):
    user_dic = db_handler.select(username)
    if user_dic:
        # 记录日志
        common.admin_logger.error(f'管理员root，添加账户{username}失败，用户已存在')
        return False, '用户已存在'
    else:
        password = common.get_pwd_md5(password)
        user_dic = {
            'username': username,
            'password': password,
            'balance': 15000,
            # 用于记录用户流水
            'flow': [],
            # 用与记录用户购物车
            'shop_car': {},
            # locked：用于记录用户是否被冻结
            # False:未冻结     True：已冻结
            'locked': False
        }
        db_handler.save(user_dic)
        # 记录日志
        common.admin_logger.info(f'管理员root，添加了账户{username}')
        return True, '添加成功'


# 管理额度接口
def manage_balance_interface(username, balance):
    user_dic = db_handler.select(username)
    if user_dic:
        user_dic['balance'] = int(balance)
        # 记录流水
        flow = f'管理员root，把账户额度改为了{balance}'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        # 记录日志
        common.admin_logger.info(f'管理员root把{username}额度改为{balance}￥')
        return True, '更改成功'
    else:
        # 记录日志
        common.admin_logger.error(f'管理员root更改{username}额度失败，用户不存在')
        return False, '用户不存在，更改失败'


# 冻结账户接口
def close_user_interface(username):
    user_dic = db_handler.select(username)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)
        # 记录日志
        common.admin_logger.info(f'管理员root冻结{username}成功！')
        return True, '冻结成功'
    # 记录日志
    common.admin_logger.error(f'管理员root冻结{username}失败，用户不存在！')
    return False, '用户不存在'


# 解除冻结接口
def open_user_interface(username):
    user_dic = db_handler.select(username)
    if user_dic:
        user_dic['locked'] = False
        db_handler.save(user_dic)
        # 记录日志
        common.admin_logger.info(f'管理员root解除{username}冻结成功！')
        return True, '解除冻结成功'
    # 记录日志
    common.admin_logger.error(f'管理员root解除{username}冻结失败，用户不存在！')
    return False, '用户不存在'
