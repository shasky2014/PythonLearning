#!/usr/bin/python
# coding=utf8
"""
mysql python simple interface
usage:
--------
pydb = get_db('slave')
results = pydb.exec_sql('select count(*) from orders;');
pydb.close()
"""

import os
import sys
# from hashlib import md5
from datetime import datetime
import logging

# import MySQLdb as mdb
# from MySQLdb import converters

import pymysql
from pymysql.cursors import DictCursor

from log import init_log, error_info
from globalConfig import db_conf


def get_log_file(ds=None):
    if ds:
        return os.getenv("MYDB_LOG") if os.getenv("MYDB_LOG") else \
            "/data/babyfs_data/pydb_%s_%s_%s.log" % (
                os.getlogin(), ds,
                os.path.splitext(os.path.basename(sys.argv[0]))[0])
    else:
        return os.getenv("MYDB_LOG") if os.getenv("MYDB_LOG") else \
            "/data/babyfs_data/pydb_%s_%s.log" % (
                os.getlogin(),
                os.path.splitext(os.path.basename(sys.argv[0]))[0])


log = init_log(get_log_file(),
               logtostderr=True if os.getenv("MYDB_LOGTOSTDERR") else False)
error_log = init_log(get_log_file(datetime.now().strftime('%Y-%m-%d')),
                     level=logging.WARN, logname='pydb_error_log',
                     logtostderr=True if os.getenv("MYDB_LOGTOSTDERR") else False)


def dict_value_pad(key):
    return "%(" + str(key) + ")s"


def db_error_log(sql, param=None, debug=False):
    msg = error_info()
    if param is None:
        error_msg = '%s\nsql: %s\n%s\n' % (msg, sql, 30 * '~')
    else:
        dt = param
        if len(param) > 1 and not isinstance(param, dict) and (
                isinstance(param[0], list) or isinstance(param[0], tuple)):
            dt = param[0]
        error_msg = '%s\nsql: %s\nparam:%s\n%s\n' % (msg, sql, dt, 30 * '~')
    error_log.error(error_msg)
    if debug:
        raise Exception(error_msg)
    return error_msg


class mydb:
    """ simple db class """

    def __init__(self, host, user, passwd, dbname, port=3306,
                 coding='utf8', debug=False):
        self.debug = debug

        # self.conn.set_character_set(coding)
        print('host=%s, port=%s,database=%s, charset=%s,user=%s, password=%s)' % (host, port, dbname, 'utf8', user,
                                                                                  passwd))
        self.conn = pymysql.connect(host=host, port=port,
                                    database=dbname, charset='utf8',
                                    user=user, password=passwd)

    # host = 'rr-bp1exjjx399egn15f.mysql.rds.aliyuncs.com', port = 3306, database = 'babyfs_v2', charset = 'utf8', user = 'babyfs_v2_root', password = 'd#hpqD59qiHj')
    def set_debug_mode(self, debug=True):
        self.debug = debug

    def exec_sql(self, sqlstr, params=None, resultFormat='dict',
                 needCommit=False, returnAffectedRows=False, withColumns=False):
        """
        执行sql,执行方式有如下几种：

        pydb=get_db()
        sql='select * from user_tel_sale'
        pydb.exec_sql(sql)

        sql2="insert into user_tel_sale (userhp,userType) values (%s,%s)"

        param=(1,1)
        sql3=sql2 % param
        pydb.exec_sql(sql3)

        param=(2,2)
         pydb.exec_sql(sql2,param)

        param=[(3,3),(4,4)]
        pydb.exec_sql(sql2,param)

        :param sqlstr: sql string
        :type slqstr: str
        :param params:
        :type params: tuple or list
        :return:
        """
        cursorType = pymysql.cursors.Cursor
        if resultFormat == 'dict':
            cursorType = pymysql.cursors.DictCursor
        curor = self.conn.cursor(cursorType)
        flag = True
        affected_rows = 0
        columns = []
        try:
            if params:
                if isinstance(params, tuple):
                    affected_rows = curor.execute(sqlstr, params)
                elif isinstance(params, list) and isinstance(params[0], tuple):
                    flag = False
                    affected_rows = curor.executemany(sqlstr, params)
                    # print params
            else:
                # print sqlstr
                affected_rows = curor.execute(sqlstr)
            if needCommit:
                self.conn.commit()
            result = []
            if flag:
                if resultFormat != 'dict':
                    columns = [d[0] for d in curor.description]
                result = curor.fetchall()[:]
        except pymysql.Error as e:
            result = []
            log.error('%s\nsql: %s' % (e, sqlstr))
            db_error_log(sqlstr, params, self.debug)
        except:
            result = []
            log.error('unknown failure: %s,\nsql: %s' % (sys.exc_info()[0], sqlstr))
            db_error_log(sqlstr, params, self.debug)
        curor.close()

        if returnAffectedRows:
            if not withColumns:
                return affected_rows
            else:
                return affected_rows, columns
        else:
            if not withColumns:
                return result
            else:
                return result, columns

    def insert(self, table_name, param_dict, on_duplicate_ignore=True):
        """
        利用字典方式传参，完成数据插入,使用方式如下：
        pydb=get_db()
        paramDict={'userhp':5,'userType':5}
        pydb.insert('user_tel_sale',paramDict)

        paramDict={'userhp':5,'userType':555}
        pydb.insert('user_tel_sale',paramDict,False)

        :param table_name: 表名称
        :type table_name: str
        :param param_dict: 参数列表
        :type param_dict: dict
        :param on_duplicate_ignore: 遇到重复键是否ignore
        :type on_duplicate_ignore: bool
        :return: affected_rows
        """
        if not param_dict:
            return
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        ignore = ''
        if on_duplicate_ignore:
            ignore = ' ignore '
        parts = ['insert', ignore, 'into', table_name]
        keys = param_dict.keys()
        fields = '(' + ','.join('`' + str(key) + '`' for key in keys) + ') values'
        symbols = '(' + ','.join(dict_value_pad(key) for key in keys) + ')'
        parts.append(fields)
        parts.append(symbols)
        affected_rows = 0
        if not on_duplicate_ignore:
            update_part = "on duplicate key update "
            update_part += ','.join('`' + str(key) + '`' + "=" + dict_value_pad(key) for key in keys)
            parts.append(update_part)
        sql = ' '.join(parts)
        try:
            affected_rows = cursor.execute(sql, param_dict)
        except:
            log.info('failed sql: %s' % sql)
            db_error_log(sql, param_dict, self.debug)
        cursor.close()
        return affected_rows

    def get_last_insert_id(self):
        """
        get last inserted id
        :return:
        """
        return self.conn.insert_id()

    def insert_many(self, table_name, param_list, on_duplicate_ignore=True):
        """
        批量插入，利用字典方式传参，完成数据插入,使用方式如下：
        pydb=get_db()
        paramDict=[{'userhp':6,'userType':6},{'userhp':7,'userType':7},{'userhp':8,'userType':8}]
        pydb.insert_many('user_tel_sale',paramDict)

        paramDict=[{'userhp':6,'userType':66},{'userhp':7,'userType':777},{'userhp':8,'userType':8}]
        pydb.insert_many('user_tel_sale',paramDict,False)


        :param table_name: 表名称
        :type table_name: str
        :param param_list: 参数列表
        :type param_list: list of dict
        :param on_duplicate_ignore: 遇到重复键是否ignore
        :type on_duplicate_ignore: bool
        :return:
        """
        if not param_list:
            return

        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        ignore = ''
        if on_duplicate_ignore:
            ignore = ' ignore '
        parts = ['insert', ignore, 'into', table_name]
        affected_rows = 0
        if on_duplicate_ignore:
            newParamList = self.formatData(param_list, True)
            keys = newParamList[0][0].keys()
            fields = '(' + ','.join('`' + key + '`' for key in keys) + ') values'
            symbols = '(' + ','.join(dict_value_pad(key) for key in keys) + ')'
            parts.append(fields)
            parts.append(symbols)
            sql = ' '.join(parts)
            for pList in newParamList:
                try:
                    affected_rows += cursor.executemany(sql, pList)
                    # affected_rows = self.conn.affected_rows()
                    # if self.db_flag == 'master':
                    self.conn.commit()
                except:
                    log.info('failed sql: %s' % sql)
                    db_error_log(sql, newParamList, self.debug)
            cursor.close()
        else:
            for param_dict in param_list:
                affected_rows += self.insert(table_name, param_dict, False)
        return affected_rows

    def select(self, table, fields, resultFormat='dict'):
        f = ['`' + item + '`' for item in fields]
        sql_parts = ['select', ','.join(f), 'from', table]
        sql = ' '.join(sql_parts)
        return self.exec_sql(sql, resultFormat=resultFormat)

    def formatData(self, param_list, segment=False, segment_size=20000):
        """
        数据词典对齐

        :param param_list:
        :return:
        """
        allKeys = set()
        for valueDict in param_list:
            for key in valueDict:
                allKeys.add(key)
        result = []
        for valueDict in param_list:
            tmp = {}
            for key in allKeys:
                tmp[key] = valueDict.get(key, None)
            result.append(tmp)

        if not segment:
            return result
        else:
            r = []
            total = len(result)
            segment_num = len(result) / segment_size + 1
            for i in range(segment_num):
                start_index = i * segment_size
                end_index = min(i * segment_size + segment_size, total)
                tmp = result[start_index:end_index]
                r.append(tmp)
            return r

    def commit(self):
        self.conn.commit()

    def escape(self, str_cont):
        """ escape  """
        return self.conn.escape_string(str_cont)

    def close(self):
        """ close the db """
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def get_connection(self):
        return self.conn


def get_db(db_flag='slave', dbname=None, host='', user_flag=None):
    """
    :param db_flag: db标签,可选'babyfs_v2','online','stat'等
    :type db_flag: str
    :param dbname: default schema
    :type dbname: str
    :param host: host ip for db
    :type host: str
    :param user_flag: 用户标签 1:有写权限  2：只读
    :return: database connection instance

    suggested usage:
    with get_db() as db:
        db.exec_sql('select * from a')

    """
    online_flag = True

    dc = db_conf(db_flag if online_flag else None, user_flag)

    log.debug('dbhost: %s' % dc['host'])
    db_name = dc['db_name'] if not dbname else dbname
    port = dc.get('port', 3306)
    db_host = dc.get('host', host)
    print(db_host, dc['user'], dc['password'], db_name)

    return mydb(db_host, dc['user'], dc['password'], db_name, port=port)


def test():
    import time

    pydb = get_db('babyfs_v2')
    sql = 'select * from t_promoter limit 2'
    r = pydb.exec_sql(sql)
    print(r)
    # time.sleep(10)
    pydb.close()


if __name__ == "__main__":
    # pydb = get_db('master')
    #
    # sql = 'select count(*) from orders;'
    # log.info(sql)
    # results = pydb.exec_sql(sql)
    # for r in results:
    # print r
    # pydb.close()
    test()
