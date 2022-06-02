# -*- coding: UTF-8 -*-


# -*- coding: UTF-8 -*-


import logging


class Logger:

    def getlog(self):

        # 创建日志器
        logger = logging.getLogger("logger")
        # 设置日志器的等级,默认是warning及以上
        logger.setLevel(logging.INFO)
        # 创建控制台处理器
        sh = logging.StreamHandler()
        # 创建格式器
        # 日志包含那些内容：时间 文件名 行 日志等级 事件描述
        formater = logging.Formatter(fmt="%(asctime)s [%(filename)s:%(lineno)d] [%(levelname)s] :%(message)s ",
                          datefmt="%Y/%m/%d %X")
        # 一个日志器可以有多个处理器，并且每个处理器可以有各自的格式器一级过滤器
        logger.addHandler(sh)
        sh.setFormatter(formater)
        # logger.critical("这是一个严重的错误")
        # logger.error("这是一个error错误")
        return logger

