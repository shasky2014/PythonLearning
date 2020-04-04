from odps import ODPS

o = ODPS(access_id='xxxxx',
         secret_access_key='xxxxxx',
         project='babyfs_data',
         endpoint='http://service.odps.aliyun.com/api')

sql = '''
SELECT plan_id,count(id) group_count
FROM mysql_t_group_dim
where ds='${bdp.system.bizdate}'
group by plan_id
order by group_count desc 
limit 10
'''

import datetime

ds = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d')
print(ds)

sql = sql.replace('${bdp.system.bizdate}', ds)

instance_id = o.execute_sql(sql)

reader = instance_id.open_reader()
print(reader.count)
print(reader._schema)

# 按行处理
for row in reader:
    # print(row.values)
    print(dict(zip(('plan','groupcount'),row.values) ))

# 全部处理
result_df = reader.to_pandas()

print(result_df)


import data_plot2
data_plot2.data_plot(result_df)
