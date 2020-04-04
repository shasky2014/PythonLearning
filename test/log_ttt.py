from utils.logUtils import my_logger

app_main_logger = my_logger('my_app_main')


def app_main_sub(n):
    print(n)
    print(n**n)
    app_main_logger.critical('a critical level log in app_main_sub:arg={}'.format(n))
    app_main_logger.error('an error level log in app_main_sub:arg={}'.format(n))
    app_main_logger.warning('a warning level log in app_main_sub:arg={}'.format(n))
    app_main_logger.info('an info level log in app_main_sub:arg={}'.format(n))
    app_main_logger.debug('a debug level log in app_main_sub:arg={}'.format(n))


def app_main():
    # CRITICAL = 50
    # FATAL = CRITICAL
    # ERROR = 40
    # WARNING = 30
    # WARN = WARNING
    # INFO = 20
    # DEBUG = 10
    # NOTSET = 0
    # 初始化获得一个日志捕获器，name=my_app_main
    app_main_logger.critical('a critical level log')
    app_main_logger.error('an error level log')
    app_main_logger.warning('a warning level log')
    app_main_logger.info('an info level log')
    app_main_logger.debug('a debug level log')
    app_main_sub(1)
    app_main_sub(2)

    pass


if __name__ == '__main__':
    # print(time.time())
    # filename = '/Users/admin/PycharmProjects/MLP/utils/requirements.txt'
    # baseFilename = os.path.abspath(filename)
    # print(os.stat(baseFilename)[ST_MTIME])

    app_main()
