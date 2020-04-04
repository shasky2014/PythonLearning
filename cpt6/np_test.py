import numpy as np

a = np.array([10, -0.0000001, 0.000000001, 1, np.nan, 0.01]).reshape(2, 3)
print(a)
b = a[:, 1]
print(b)
print(np.array([a, b.reshap(2, 1)]))

a[np.isnan(a)] = 0
a = np.where(a < 0.00001, np.where(a > -0.00001, 0, a), a)
# print(a)
#
# print(a[a[:, 0] == 1])
np.savetxt("save_demo.txt", a)

# np.any((a.data if issparse(a) else a) < 0)
exit(1)
# mp_data = np.array(range(12)).reshape(3, 4)
# print(mp_data)
#
# print(mp_data[:, 1:3])
# print(mp_data[:, -1])
# print(mp_data[:, 1])
#
# # map( mp_data[:,1] )
# # from sklearn.datasets import load_iris
# # iris = load_iris()
# # print(type(iris.data), type(iris.target))
# # print(iris.target)
#
# mp_data[mp_data == np.nan] = 50


# print(mp_data)
#

data = np.array([[np.nan, 1, 2, 3, 4, 'jxy_ck'],  # 数据类型为字符串型
                 [10, 15, 20, 25, np.nan, 'bind'],
                 [np.nan, 5, 8, 10, 20, 'bind']])
print(data)
print('-' * 100)

data = np.nan_to_num(data)
print(data)
print('-' * 100)
print(data[0:-1, 0:-1])

print('-' * 100)
print(data[-1, :])

print('-' * 100)

print(data[[x.find('bind') >= 0 for x in data[:, -1]], :])

s = 'bind,jxy'
print(s.find('') >= 0, s.find(''), s.find('jxy'), s.find('jxsy'))
