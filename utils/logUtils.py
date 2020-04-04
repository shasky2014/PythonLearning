"""
simple log func
@author:
@version:  0.1
"""

import os
import time
import logging
import traceback
import inspect
from logging.handlers import TimedRotatingFileHandler
from stat import ST_MTIME
from io import StringIO


def init_log(logtofile="test.log", level=logging.DEBUG, logtostderr=False, logname="pplog"):
    """
    @logname: log file name
    @level:   logging.DEBUG/INFO/WARN/ERROR/CRITICAL
    @logtostderr: boolean
    """

    logger = logging.getLogger(logname)
    logger.setLevel(level)
    formatter = logging.Formatter('[%(asctime)s] [%(filename)s:%(lineno)d:%(funcName)s] %(levelname)s: %(message)s')
    if logtofile:
        fh = logging.handlers.RotatingFileHandler(logtofile, maxBytes=5 * 1024 * 1024, backupCount=5)
        fh.setFormatter(formatter)
        fh.setLevel(level)
        logger.addHandler(fh)
    if logtostderr:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger


def init_log_complex(logtofile="test.log", level=logging.DEBUG, logtostderr=False, logname="pplog"):
    """
    @logname: log file name
    @level:   logging.DEBUG/INFO/WARN/ERROR/CRITICAL
    @logtostderr: boolean
    """

    logger = logging.getLogger(logname)
    logger.setLevel(level)
    formatter = logging.Formatter('[%(asctime)s] [%(filename)s:%(lineno)d:%(funcName)s] %(levelname)s: \n%(message)s')
    if logtofile:
        fh = logging.handlers.TimedRotatingFileHandler(logtofile, when="d",
                                                       interval=1, backupCount=60)
        # fh = logging.handlers.RotatingFileHandler(logtofile, maxBytes=5*1024*1024, backupCount=5)
        fh.setFormatter(formatter)
        fh.setLevel(level)
        logger.addHandler(fh)
    if logtostderr:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger


def error_info():
    """
    自定义错误信息
    :return:
    """
    stack = inspect.stack()
    stack_len = len(stack)
    msgs = []
    if stack_len > 0:
        bottom_stack = stack[stack_len - 1]
        frame, script_path, line, module_name, codes, _ = bottom_stack
        fp = StringIO()
        traceback.print_exc(file=fp)
        message = fp.getvalue()
        msgs = ['Scripts:' + script_path, 'Line number:' + str(line), 'Module_name:' + module_name]
        msgs.append(message)
    msg = '\n'.join(msgs)
    return msg


def my_logger(logger_name, log_path='log_test.log'):
    logger = logging.getLogger(logger_name)
    # logger.handlers.clear()
    # print(logger.handlers)
    logger.setLevel(logging.INFO)

    console_handle = TimedRotatingFileHandler(log_path, when="d", interval=1, backupCount=60)
    formatter = logging.Formatter(
        '[%(asctime)s] [%(name)s] %(levelname)s: %(message)s '
    )
    formatter = logging.Formatter('[%(asctime)s] [%(name)s %(filename)s:%(lineno)d:%(funcName)s] %(levelname)s: %(message)s')

    console_handle.setFormatter(formatter)
    logger.addHandler(console_handle)

    return logger

