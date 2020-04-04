from mysql import connector


def mysqlInit(db_conf):
    cnx = connector.connect(host=db_conf['ip'],
                            user=db_conf['user'],
                            passwd=db_conf['password'],
                            database=db_conf['database'])
    return cnx


class MyDB:
    def __init__(self, db_conf, dictionary=False):
        self.dictionary = dictionary
        self.conn = mysqlInit(db_conf)
        self.cnx = self.conn.cursor(dictionary=dictionary)

    def do_select(self, sql, dictionary=False):
        """
        返回全量查询结果，
        :param sql: sql查询语句
        :param dictionary: 默认数据结果输出格式为list
        :return : sql语句查询结果
        """
        cnx = self.conn.cursor(dictionary=dictionary)
        cnx.execute(sql)
        result = cnx.fetchall()
        cnx.close()
        return result

    def do_insert_many(self, sql, records):
        """
        批量插入数据库,1000条插入一次，避免MySQL插入时的内存异常
        :param sql: insert into table_a () values (%s,%s,%d,%s,%d)
        :param records:[(),(),()]
        :return:
        """
        cnx = self.cnx
        for i in range(0, len(records), 1000):
            cnx.executemany(sql, records[i:1000 + i])
            self.conn.commit()
        pass

    def close(self):
        self.cnx.close()
        self.conn.close()


if __name__ == '__main__':
    from .conf import local_db

    print(local_db)
    cnx1 = mysqlInit(local_db)
    print(cnx1.server_port)
