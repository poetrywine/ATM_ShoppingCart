# 项目说明书
## 项目：ATM + 购物车
# 项目需求：
    模拟实现一个ATM + 购物商城程序
    
    1.额度 15000或自定义      -----》注册功能
    2.实现购物商城，买东西加入 购物车，调用信用卡接口结账       ---》购物功能、支付功能
    3.可以提现，手续费5%    ---》提现功能
    4.支持多账户登录       ---》登录功能
    5.支持账户间转账       ---》转账功能
    6.记录日常消费      ---》记录流水功能
    7.提供还款接口      ---》还款功能
    8.ATM记录操作日志     ---》记录日志功能
    9.提供管理接口，包括添加账户、用户额度，冻结账户等。。。---->管理员功能
    10.用户认证用装饰器     ---》登入认证装饰器
# 本项目说明：
    - 管理员为root,密码为root
    - 内置用户有lili, 密码为lili

## “用户视图层”展示给用户选择的功能
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
    

# 一个项目是如何从无到有的
## 一、需求分析
    1.拿到项目，会先在客户那里一起讨论需求，
    商量项目的功能是否能实现，周期与价格，得到一个需求文档。
    2.最后在公司内部需要开一次会议，最终会得到一个开发文档，
    交给不同岗位的程序员开发
        - python：后端，爬虫
        
        - 不同岗位：
            -UI界面设计：
                - 设计软件的布局，会根据软件的外观切成一张张图片。
                
            -前端：
                - 拿到UI交给他的图片，然后去搭建网站页面。
                - 设计一些页面中，那些位置需要接受数据，需要进行数据交互。
                
            -后端：
                - 直接写核心的业务逻辑，调度数据库进行数据的增删查改。
            -测试：
                - 会给代码进行全面测试，比如压力测试，界面测试（CF卡箱子）。
            -运维：
                - 部署项目。
## 二、程序的框架设计
### 三层架构
####1、用户视图层（/sore/src.py）
    - 用于与用户交互
        - 接收用户输入的内容
        - 打印输出内容给用户
####2、逻辑接口层(/interface)
    - 核心业务逻辑，相当于用户视图与数据处理层的桥梁
        - 接收用户视图层传递过来的参数并进行逻辑处理
        - 返回结果给用户视图层
####3、数据处理层(/db/db_handler.py)
    - 接受接口层传递过来的参数，做数据的
        - 保存    save()
        - 查看    select()
        - 更新
        - 删除
### 分层设计的好处
    1）思路清晰
    2）不会出现写一半代码时推翻重写
    3）扩展性强
    4）方便自己或以后自己的同事更好维护
     
### 三层架构设计的好处
    1）把每个功能都分成三部分，逻辑清晰
    2）如果用户更换不同的用户界面或不同的数据存储机制都不会影响接口层的核心逻辑代码，扩展性强
    3）可以在接口层，准确的记录日志与流水。



##三、项目搭建
    - ATM   项目根目录
        - readme.py 项目的说明书
        
        - start.py  项目启动文件
        
        - conf  配置文件
            -settings.py
        
        - lib   公共方法文件
            - common.py
            
        - core（用户视图层）  存放用户视图层代码文件
            - src.py
            
        - interface（逻辑接口层）  存放核心业务逻辑代码
            - user_interface.py     用户相关的接口
            - bank_interface.py     银行相关的接口
            - shop_interface.py     购物相关的接口
            
        - db（数据处理层）    存放数据与数据处理层代码
            - db_handler.py     数据处理层代码
            - user_data         用户数据
            
        - log   存放日志文件


    


## 三 分任务开发
## 四 测试
## 五 上线


#统计代码
file---->settings---->plugins
