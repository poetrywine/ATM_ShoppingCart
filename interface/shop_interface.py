""""
购物商城接口
"""
from db import db_handler
from lib import common


# 购物接口
def shopping_interface(username, shop_car_dic=None, flag=False):
    from interface import bank_interface
    # 接受用户层传入的购物车字典
    if shop_car_dic:
        # 保存用户购物车数据
        user_dic = db_handler.select(username)
        user_dic['shop_car'] = shop_car_dic
        db_handler.save(user_dic)
    else:
        # 拿到用户购物车数据，返回给用户视图层
        user_dic = db_handler.select(username)
        return user_dic['shop_car']
    # 判断是否付款
    if flag:
        # shop_car_dic = {'商品名称': [价格，数量]}
        money = 0
        for key in shop_car_dic:
            price, count = shop_car_dic[key]
            res = price * count
            money += res
        flag2 = bank_interface.pay_interface(username, money)
        if flag2:
            # 记录支付成功日志
            common.bank_logger.info(f'{username}支付{money}成功！')
            return True, '支付成功'
        else:
            # 记录支付失败日志
            common.bank_logger.error(f'{username}支付{money}失败，余额不足！')
            return False, '支付失败，余额不足！'


# 查看购物车接口
def check_shop_car_interface(username):
    # 调用数据处理层
    user_dic = db_handler.select(username)
    # 记录日志
    common.shop_logger.info(f'{username}查看了购物车')
    return user_dic['shop_car']
