import datetime

from odpsInit import odpsInit
from pandas import DataFrame

o = odpsInit()

instance1 = o.execute_sql("select * from dws_channel_summary_table_part3_sale_base where ds='20190701'")

print(datetime.datetime.now(), 'ID:', instance1.id)
print(datetime.datetime.now(), 'Log view:', instance1.get_logview_address())

# instance1.open_reader()
all_result = instance1.open_reader().to_pandas()

print(all_result)
print([dict(zip(all_result.keys(), a_item)) for a_item in all_result.values])

all_result_df = DataFrame(all_result)
print(all_result_df.keys())
print(all_result_df.values)
