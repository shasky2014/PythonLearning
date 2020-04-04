import json
import pymysql

conf = dict(host='localhost', port=3306,
            database='ads', charset='utf8',
            user='root', password='1')

conn = pymysql.connect(**conf)

cux = conn.cursor()

affected_rows = cux.execute('select * from flask_calendar_data limit 10;')
print(affected_rows)
result = cux.fetchall()
print(result)
print(cux.description)
column_names = [x[0] for x in cux.description]
print([dict(zip(column_names, x)) for x in result])
print(json.dumps([dict(zip(column_names, x)) for x in result], ensure_ascii=False))

from pandas import DataFrame

result_df = DataFrame.from_records(data=list(result),
                                   columns=column_names)
print(result_df)

print('-' * 100)
print(cux.lastrowid)
print(cux.rowcount)
print(cux.arraysize)
print(cux.max_stmt_length)
print(cux.rownumber)
