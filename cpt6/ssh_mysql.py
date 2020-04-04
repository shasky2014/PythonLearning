from sshtunnel import SSHTunnelForwarder

from utils.mysqlInit import mysqlInit
from utils.odpsInit import odpsInit

server = SSHTunnelForwarder(
    ssh_address_or_host=('10.10.10.11', 22),  # 指定ssh登录的跳转机的address
    ssh_username='root',  # 跳转机的用户
    ssh_password='root@test',  # 跳转机的密码
    remote_bind_address=('10.10.10.11', 3306)
)

server.start()

db_conf = {
    'ip': '10.10.10.11',
    'post': '3306',
    'user': 'root',
    'password': 'babyfs@Mysql',
    'database': 'stat'
}


ds = '20190319'
# from odps
odps = odpsInit()
sql_1 = '''
select * from dim_date where ds='{ds}' limit 1000;
'''.format(ds=ds)


# insert into mysql
sql_2 = 'replace INTO dim_date_odps VALUES({})'.format(','.join(['%s']*15))
cnx = mysqlInit(db_conf)
cursor = cnx.cursor()
print(cnx,cursor)

_instance = odps.execute_sql(sql_1)
with _instance.open_reader() as reader:
    data_deliver1=[]
    for r in reader:
        # print(r) 读取odps数据
        data_deliver1.append(r.values())

    # insert into mysql
    cursor.execute(sql_2, tuple(data_deliver1))
    cnx.commit()
    cursor.close()
server.close()
