from mysql import connector
from pandas import DataFrame



conf = dict(host='localhost', port=3306,
            database='ads', charset='utf8',
            user='root', password='1')

conn = connector.connect(**conf)
cux = conn.cursor(dictionary=True)

affected_rows = cux.execute('select * from flask_calendar_data limit 10;')
print(affected_rows)
result = cux.fetchall()
print(result)
print('-' * 100)

result_df = DataFrame.from_records(result, columns=cux.column_names)

print(result_df)
print('-' * 100)
print('lastrowid:\t', cux.lastrowid)
print('rowcount:\t', cux.rowcount)
print('arraysize:\t', cux.arraysize)
print('description:\t', cux.description)
print('column_names:\t', cux.column_names)
