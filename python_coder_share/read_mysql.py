import mysql.connector

# 链接
conn = mysql.connector.connect(host='localhost',
                               user='root',
                               passwd='1',
                               database='order_settle'
                               )
# 游标
cursor_1 = conn.cursor()
print(cursor_1)

query = ("SELECT DATE_FORMAT( order_time, '%Y-%m' ) as aa , count( 1 ) as cc "
         "FROM excel_order_detail "
         "GROUP BY DATE_FORMAT( order_time, '%Y-%m' ); "
         )

query = '''
SELECT DATE_FORMAT( order_time, '%Y-%m' ) as aa , count( 1 ) as cc
FROM excel_order_detail
GROUP BY DATE_FORMAT( order_time, '%Y-%m' );
'''

cursor_1.execute(query)

select_result = cursor_1.fetchall()
print(select_result)
for x in select_result:
    print(x)
print('-' * 100)


# exit(0)
def read_mysql(db_conf, sql):
    conn = mysql.connector.connect(**db_conf)
    cursor_1 = conn.cursor()
    cursor_1.execute(sql)
    return cursor_1.fetchall()


if __name__ == '__main__':
    db_cnf = dict(host='localhost',
                  user='root',
                  passwd='1',
                  database='order_settle')
    query_sql = '''
        SELECT DATE_FORMAT( order_time, '%Y-%m' ) as aa , count( 1 ) as cc
        FROM excel_order_detail
        GROUP BY DATE_FORMAT( order_time, '%Y-%m' );
        '''
    select_data = read_mysql(db_cnf, query_sql)
    print(select_data)
    pass
