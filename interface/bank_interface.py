""""
银行相关业务的接口
"""
from db import db_handler
from lib import common


# 提现接口(手续费5%)
def withdraw_interface(username, money):
    # 1）先获取用户字典，访问数据处理层，拿到用户数据的字典
    user_dic = db_handler.select(username)

    # 该用户账号中的金额
    balance = int(user_dic.get('balance'))

    # 提现总额：本金 + 手续费（5%）
    money2 = int(money) * 1.05

    # 判断用户金额是否足够
    if balance >= money2:
        # 2）修改用户字典中的金额
        balance -= money2
        user_dic['balance'] = balance

        # 3) 记录流水
        flow = f'用户[{username}]提现金额[{money}￥]成功，手续费为：{money2-float(money)}￥！'
        user_dic['flow'].append(flow)

        # 4) 访问数据处理层，保存更新该用户数据
        db_handler.save(user_dic)

        # 记录提现日志
        common.bank_logger.info(f'{username}提现{flow}￥成功！')
        return True, flow
    # 记录提现失败日志
    common.bank_logger.error(f'{username}提现{money}￥失败,余额不足！')
    return False, '提现金额不足，请重新输入'


# 还款接口
def repay_interface(username, money):
    # 1.获取用户字典
    user_dic = db_handler.select(username)

    # 2.直接做加钱的操作
    # 因为是json文件，所以user_dic['balance'] ----> float
    user_dic['balance'] += money

    # 3.记录流水
    flow = f'用户：[{username} 还款：[{money}]成功！当前额度为：{user_dic["balance"]}'
    user_dic['flow'].append(flow)

    # 4.调用数据处理层，将修改后的数据更新
    db_handler.save(user_dic)

    # 既然还款日志
    common.bank_logger.info(f'{username}还款{flow}成功！')
    return True, flow


# 转账接口
def transfer_interface(username, to_user, money):
    """
    1.获取用户处理层传来的 当前用户
    2.获取用户处理层传来的 目标用户
    3.获取用户处理层传来的 转账金额
    :param username:
    :param to_user:
    :param money:
    :return:
    """
    # 1） 获取当前用户 字典
    username_dic = db_handler.select(username)

    # 2） 获取 目标用户 字典
    to_user_dic = db_handler.select(to_user)

    # 3） 判断 目标用户 是否存在
    if not to_user_dic:
        return False, '目标用户不存在'

    # 4） 若用户存在，判断当前用户转账金额是否足够
    if username_dic['balance'] >= money:

        # 5) 若足够，则开始给目标用户转账
        # 5.1） 给当前用户的数据做减钱操作
        username_dic['balance'] -= money
        # 5.2） 给目标用户的数据做加钱操作
        to_user_dic['balance'] += money

        # 5.3) 记录流水
        # 5.3.1) 当前用户记录流水
        username_flow = f'用户：[{username}]给用户：[{to_user}] 转账：[{money}￥]'
        username_dic['flow'].append(username_flow)
        # 5.3.2) 目标用户记录流水
        to_user_flow = f'用户：[{username}]给您转账：[{money}￥]'
        to_user_dic['flow'].append(to_user_flow)

        # 6) 保存用户数据
        # 6.1) 调用数据处理层的save功能，保存当前用户数据
        db_handler.save(username_dic)
        # 6.2) 调用数据处理层的save功能，保存目标用户数据
        db_handler.save(to_user_dic)

        # 记录日志
        common.bank_logger.info(f'用户：{username}给用户：{to_user} 转账：{money}￥成功！')
        return True, f'用户：[{username}]给用户：[{to_user}] 转账：[{money}￥]成功！'
    common.bank_logger.error(f'用户：{username}给用户：{to_user} 转账：{money}￥失败，余额不足！')
    return False, '当前用户转账金额不足'


# 查看流水接口
def check_flow_interface(username):
    # 调用数据处理层拿到该用户数据字典
    user_dic = db_handler.select(username)
    # 记录日志
    common.bank_logger.info(f'{username}查看了流水，当前流水为{user_dic.get("flow")}')
    return user_dic.get('flow')


# 付款接口
def pay_interface(username, money):
    # 调用数据处理层，拿到用户余额
    user_dic = db_handler.select(username)
    # 判断余额是否足够支付
    if user_dic['balance'] >= money:
        # 修改用户数据字典的余额
        user_dic['balance'] -= money
        # 清空购物车
        user_dic['shop_car'] = {}
        # 记录流水
        flow = f'用户[{username}],消费了[{money}￥]'
        user_dic['flow'].append(flow)
        # 更新用户数据
        db_handler.save(user_dic)
        # 记录日志
        common.bank_logger.info(f'用户{username},消费了{money}￥')
        return True
    else:
        # 记录日志
        common.bank_logger.error(f'用户{username},付款{money}￥失败')
        return False



