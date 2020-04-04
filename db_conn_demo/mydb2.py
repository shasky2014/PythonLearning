"""
results = db_select('select * from table')



results.get_dict() = [
    {'id'=1,'code'='a'},
    {'id'=2,'code'='b'}
]

results.get_list() = [(1,'a'),(2,'b')]

results.get_column_name() = ['id','code']
"""
