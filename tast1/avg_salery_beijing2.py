from matplotlib import pyplot as plt

years = ['1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
         '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
salaries = [2877, 3402, 4523, 6540, 8144, 9579, 11019, 12285, 13778, 15726, 18092, 20728, 24045, 28348, 32808, 36097,
            39867, 44715, 48444, 50415, 56061, 62677, 69521, 77560, 85038, 92477, 101599, 94258]

plt.figure(dpi=200)
p1 = plt.bar(years, [x / 12 for x in salaries], width=0.35)
plt.title("beijing avg salaries")
plt.xlabel("year")
plt.ylabel("salaries by month")
plt.tick_params(axis='x', labelsize=9, rotation=50)
plt.savefig('BeiJing avg salary.jpg', dpi=200, bbox_inches='tight')
plt.show()
