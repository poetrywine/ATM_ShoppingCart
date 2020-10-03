""""
存放配置信息
"""
import os

# 获取项目根目录路径
BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)


# 获取user_data文件夹路径
USER_DATA_PATH = os.path.join(
    BASE_PATH, 'db', 'user_data'
)


# 获取日志文件路径
LOG_ADMIN_LOG_PATH = os.path.join(
    BASE_PATH, 'log', 'admin_log', 'admin.log'
)
LOG_BANK_LOG_PATH = os.path.join(
    BASE_PATH, 'log', 'bank_log', 'bank.log'
)
LOG_SHOP_LOG_PATH = os.path.join(
    BASE_PATH, 'log', 'shop_log', 'shop.log'
)
LOG_USER_LOG_PATH = os.path.join(
    BASE_PATH, 'log', 'user_log', 'user.log'
)

"""
logging配置
"""
# 1、定义三种日志输出格式，日志中可能用到的格式化串如下
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息

# 2、强调：其中的%(name)s为getlogger时指定的名字
# standard_format=[当前时间(默认格式是 “2003-07-08 16:49:45,896”,逗号后面的是毫秒)][线程名：线程ID][task_id:logger中的名字]
# [调用日志输出函数的模块的文件名:调用日志输出函数的语句所在的代码行][文本形式的日志级别][用户输出的消息]
standard_format = '[%(asctime)s]-[%(threadName)s:%(thread)d]-[task_id:%(name)s]-[%(filename)s:%(lineno)d]' \
                  '-[%(levelname)s]-[%(message)s]'

standard_format2 = '[%(asctime)s]-[task_id:%(name)s]-[%(filename)s:%(lineno)d]' \
                  '-[%(levelname)s]-[%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

# 3、日志配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,

    # 多个日志格式
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'standard2': {
            'format': standard_format2
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},

    # 控制日志输出的位置（文件，终端），日志的接收者，不同的handler会将日志输出到不同的位置
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        # 'default': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
        #     'formatter': 'standard2',
        #     # 可以定制日志文件路径
        #     # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
        #     # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
        #     'filename': 'a1.log',  # 日志文件
        #     'maxBytes': 1024*1024*5,  # 日志大小 5M
        #     'backupCount': 500,
        #     'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        # },
        'user_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard2',
            # 可以定制日志文件路径
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
            'filename': LOG_USER_LOG_PATH,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 500,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'bank_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard2',
            # 可以定制日志文件路径
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
            'filename': LOG_BANK_LOG_PATH,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 500,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'shop_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard2',
            # 可以定制日志文件路径
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
            'filename': LOG_SHOP_LOG_PATH,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 500,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'admin_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard2',
            # 可以定制日志文件路径
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
            'filename': LOG_ADMIN_LOG_PATH,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 500,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 'other': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',  # 保存到文件
        #     'formatter': 'simple',
        #     'filename': 'a2.log',
        #     'encoding': 'utf-8',
        # },
    },

    # 负责产生不同级别日志的，日志的产生者，产生的日志会传递给handler
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '用户日志': {
            'handlers': ['user_log', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '银行日志': {
            'handlers': ['bank_log', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '购物日志': {
            'handlers': ['shop_log', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '管理员日志': {
            'handlers': ['admin_log', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        # '专门的采集': {
        #     'handlers': ['other', ],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}
