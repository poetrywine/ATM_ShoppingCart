""""
存放用户视图层文件
"""
from interface import user_interface
from lib import common
from interface import bank_interface
from interface import shop_interface
from interface import admin_interface
# 全局变量，记录用户是否登入（登入成功：login_user = username）
login_user = None


# 1、注册功能
def register():
    """
    用户视图层工作：
    1.接收用户输入的用户名和密码
    2.简单的逻辑判断：两次密码是否一致
    :return:
    """
    while True:
        # 1）让用户输入用户名与密码进行校验
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()
        # 可以输入自定义的金额

        # 小的逻辑处理：比如两次密码是否一致
        if password == re_password:

            # 2) 调用接口层的注册接口，将用户名与密码交给接口层来进行处理
            # （True, 用户注册成功）， （False，注册失败）
            flag, msg = user_interface.register_interface(username, password)

            # 3) 根据flag判断用户注册是否成功,用于控制break
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 2、登入功能
def login():
    """
    用户视图层工作：
    1.接受用户输入的 用户名和密码
    :return:
    """
    # 登入视图
    while True:
        # 1） 让用户输入用户名与密码
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        # 查看是否冻结
        flag1 = user_interface.check_user_lock_interface(username)
        if not flag1:
            # 2） 调用接口层，将数据传给登入接口
            # (False, '密码错误') , (False, '用户不存在，请重新输入！')
            flag, msg = user_interface.login_interface(username, password)
            if flag:
                print(msg)

                # 记录用户已登录
                global login_user
                login_user = username
                break
            else:
                print(msg)
        elif flag1 == '用户不存在':
            print(flag1)
        else:
            print('账户已被冻结，无法登录')


# 3、查看余额
@common.login_auth
def check_balance():
    """
    用户视图层工作：
    1.直接调用逻辑处理层即可
    :return:
    """
    # 1.直接调用查看余额接口，获取用户余额
    # （注意：虽然现在可以直接访问数据处理层，但是用户层不要直接去访问数据处理层，要先去逻辑接口层，然后通过逻辑接口层访问数据处理层）
    balance = user_interface.check_bal_interface(login_user)
    print(f'用户{login_user}账号余额为：{balance}')


# 4、提现功能
@common.login_auth
def withdraw():
    """
    用户视图层的工作：
    1.接收用户输入的 提现金额
    2.简单的逻辑判断：判断用户输入是否为数字，判断输入数字是否大于0
    :return:
    """
    while True:
        # 1)让用户输入提现金额
        input_money = input('请输入提现金额:').strip()

        # 2)判断用户输入的金额是否是数字
        if not input_money.isdigit():
            print('请重新输入')
            continue

        if int(input_money) > 0:
            # 3)用户提现金额，将提现的金额交付给接口层来处理
            flag, msg = bank_interface.withdraw_interface(login_user, input_money)

            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入正确的提现金额')
            continue


# 5、还款功能
@common.login_auth
def repay():
    """
    用户视图层的工作：
    1.接收用户输入的 还款金额
    :return:
    """
    while True:
        # 1) 让用户输入还款金额
        input_money = input('请输入还款金额').strip()
        # 2） 判断用户输入的是否是数字
        if not input_money.isdigit():
            print('请输入正确的金额')
            continue
        input_money = int(input_money)

        # 3) 判断用户输入的金额大于0
        if input_money > 0:
            # 4) 调用逻辑接口层
            flag, msg = bank_interface.repay_interface(login_user, input_money)
            if flag:
                print(msg)
                break
        else:
            print('输入的金额不能小于0')


# 6、转账功能
@common.login_auth
def transfer():
    """
    用户视图层的工作：
    1.接收用户输入的 转账金额
    2.接收用户输入的 转账目标用户
    :return:
    """
    while True:
        # 1) 让用户输入转账金额与转账目标用户
        to_user = input('请输入转账目标用户').strip()
        money = input('请输入转账金额').strip()

        # 2） 判断用户输入的金额是否是数字或大于0
        if not money.isdigit():
            print('请输入正确的金额')
            continue
        money = int(money)

        if money > 0:
            # 3） 调用转账接口
            flag, msg = bank_interface.transfer_interface(login_user, to_user, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入正确的金额')


# 7、查看流水
@common.login_auth
def check_flow():
    # 直接调用查看流水接口
    flow_list = bank_interface.check_flow_interface(login_user)
    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print('当前用户没有流水！')


# 8、购物功能
@common.login_auth
def shopping():
    # 商城物品列表
    shop_list = [
        ['凤爪', 5],
        ['方便面', 4],
        ['可乐', 2],
        ['矿泉水', 1],
        ['辣条', 3],
        ['炸鸡', 20],
    ]
    # 调用逻辑接口层，得到用户购物车
    shop_car = shop_interface.shopping_interface(login_user)
    # shop_car = {}  # {'商品名称': [价格，数量]}
    while True:
        # 打印商城物品
        # 1) 打印商品信息，让用户选择
        # 枚举：enumerate(可迭代对象) ---> (可迭代对象的索引，索引对应的值)
        # 枚举：enumerate(可迭代对象) ---> (0, ['凤爪'， 5])
        for index, shop in enumerate(shop_list):
            shop_name, shop_price = shop
            print(f'商品编号：{index}\t', f'商品名称：{shop_name}\t', f'商品单价：{shop_price}')

        # 让用户选择物品，加入购物车
        choice = input('输入商品序号(付款输入y or n)：')

        # 付款
        if choice == 'y':
            print('付款')
            flag, msg = shop_interface.shopping_interface(login_user, shop_car, flag=True)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        # 退出购物，不付款
        if choice == 'n':
            print('结束购物')
            shop_interface.shopping_interface(login_user, shop_car)
            break

        # 判断用户输入的序号是否是数字
        if not choice.isdigit():
            print('请重新输入')
            continue

        # 判断用户输入的序号是否存在
        choice = int(choice)
        if choice in range(len(shop_list)):
            # 加入购物车
            # shop_car = {'商品名称': [价格，数量]}
            # shop_list[choice][0]:商品名称
            if shop_list[choice][0] in shop_car:
                shop_car[shop_list[choice][0]][1] += 1
                print(shop_car)
            else:
                shop_car[shop_list[choice][0]] = [shop_list[choice][1], 1]
                print(shop_car)
        else:
            print('请重新输入')
            continue


# 9、查看购物车
@common.login_auth
def check_shop_car():
    # 调用逻辑接口层，得到购物车
    shop_car = shop_interface.check_shop_car_interface(login_user)
    money = 0
    for key in shop_car:
        price, count = shop_car[key]
        res = price * count
        money += res
        print('商品:[%s] 价格:[%s元] [数量:%s]' % (key, price, count))
    print('总价：%s' % money)


# 10、管理员功能
@common.login_auth
def admin():
    # 判断用户是否为root（管理员账号：root    密码：root）
    if login_user == 'root':
        print("""
        1、添加账户
        2、管理用户额度
        3、冻结账户
        4、解除冻结
        """)
        while True:
            choice = input('输入序号：')
            if choice.isdigit() and int(choice) in range(1, 5):
                if choice == '1':
                    username = input('输入用户名')
                    password = input('输入密码')
                    re_password = input('确认密码')
                    if password == re_password:
                        flag, msg = admin_interface.add_user_interface(username, password)
                        if flag:
                            print(msg)
                            break
                        else:
                            print(msg)
                            continue
                if choice == '2':
                    username = input('用户名')
                    balance = input('更该的金额为：')
                    flag, msg = admin_interface.manage_balance_interface(username, balance)
                    if flag:
                        print(msg)
                        break
                    else:
                        print(msg)
                if choice == '3':
                    username = input('冻结账户的用户名：')
                    flag, msg = admin_interface.close_user_interface(username)
                    if flag:
                        print(msg)
                        break
                    else:
                        print(msg)
                if choice == '4':
                    username = input('解冻账户的用户名：')
                    flag, msg = admin_interface.open_user_interface(username)
                    if flag:
                        print(msg)
                        break
                    else:
                        print(msg)
            else:
                print('请重新输入')
                continue
    else:
        print('您不是管理员，没有权限操作')


# 创建函数功能字典
fun_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}


# 视图层主程序
def run():
    while True:
        print("""
            1、注册功能
            2、登入功能
            3、查看余额
            4、提现功能
            5、还款功能
            6、转账功能
            7、查看流水
            8、购物功能
            9、查看购物车
            10、管理员功能
        """)

        # 让用户选择功能编号
        choice = input('请输入功能编号：').strip()

        # 判断功能编号是否存在
        if choice not in fun_dic:
            print('请输入正确的功能编号！')
            continue

        # 调用用户选择的功能函数
        fun_dic.get(choice)()
