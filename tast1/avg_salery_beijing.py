years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
salaries = [50415, 56061, 62677, 69521, 77560, 85038, 92477, 101599, 94258]
print(len(years), len(salaries), dict(zip(years, salaries)))
print(dict(zip(years, salaries)))

data_list = [1, 2012, 62677, 2, 2011, 56061, 3, 2010, 50415, 4, 2009, 48444, 5, 2008, 44715, 6, 2007, 39867, 7, 2006,
             36097,
             8, 2005, 32808, 9, 2004, 28348, 10, 2003, 24045, 11, 2002, 20728, 12, 2001, 18092, 13, 2000, 15726, 14,
             1999,
             13778, 15, 1998, 12285, 16, 1997, 11019, 17, 1996, 9579, 18, 1995, 8144, 19, 1994, 6540, 20, 1993, 4523,
             21,
             1992, 3402, 22, 1991, 2877]
import numpy as np

data_np = np.array(data_list).reshape((int(len(data_list) / 3), 3))

print(data_np[3:, 1])
print(data_np[3:, 2])

years = years + list(map(str, list(data_np[3:, 1])))
salaries = salaries + list(data_np[3:, 2])

print(years)
print(salaries)
data_np = np.array([years, salaries]).T
# print(data_np)

# print(data_np.sort(axis=0,  order=0))

import pandas as pd

data_df = pd.DataFrame(data_np).sort_values(0, axis=0, ascending=True)


# print( np.array(data_df.sort_values(0, axis=0, ascending=True)))
def subss(x):
    return x[-2:]


years = list(np.array(data_df)[:, 0])
salaries = list(map(int, np.array(data_df)[:, 1]))
print(years)
print(salaries)

# exit(1)
import pygal

this_bar = pygal.Bar()

years = ['1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
         '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
salaries = [2877, 3402, 4523, 6540, 8144, 9579, 11019, 12285, 13778, 15726, 18092, 20728, 24045, 28348, 32808, 36097,
            39867, 44715, 48444, 50415, 56061, 62677, 69521, 77560, 85038, 92477, 101599, 94258]

this_bar.x_labels = [x[-2:] for x in years]
# this_bar.add('year', values=salaries)
this_bar.add('month', values=[x / 12 for x in salaries])
this_bar.title = 'BeiJing avg salary'
this_bar.render_in_browser()
this_bar.render_to_png('BeiJing avg salary.png')
