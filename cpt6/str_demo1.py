# import re
#
# s='01234567号杀虫剂撒都睡觉大厦路口   '
# print(s[6:])
# print(s.strip())
#
#
# s1='北京（全国政治、文化、教育中心）'
#
# city_re = re.match('(.*?)（(.*?)）', s1.strip())
# if city_re:
#     print(city_re.groups())

'''
            预测成交    预测未成交
    真实成交    TP      FN
    真实未成交  FP      TN

    TP = np.sum(np.array(y_test) + y_p == 2)
    FP = np.sum(np.array(y_p) == 1) - TP
    FN = np.sum(np.array(y_test) == 1) - TP
    TN = np.sum(np.array(y_test) + y_p == 0)

    total = np.sum(y_p == y_p)
    p = TP / (TP + FP)  # 精准率：
    r = TP / (TP + FN)  # 召回率：
    c = (TP + TN) / total  # 准确率：
    f1 = 2 * TP / (total + TP - TN)
'''

TP = 2755
FP = 35716
FN = 881
TN = 141864
p = 0.07161238335369499
r = 0.7577007700770076
c = 0.7980476337630231
f1 = 0.13085710214453652

title = '{t1:<10s}\t{t2:<6s}\t{t3:<6s}\t{t4:<1s}\t{t5:<1s}\t{t6:<1s}\tf1'.format(
    t1='count', t2='预测成交', t3='预测未成交', t4='精准率', t5='召回率', t6='准确率'
)

output = '''{t1:<6s}\t{TP:<10d}\t{FN:<10d}\t{p:.2%}\t{r:.2%}\t{c:.2%}\t{f1:.2%}
{t2:<6s}\t{FP:<10d}\t{TN:<10d}'''.format(
    TP=TP, FP=FP, FN=FN, TN=TN, p=p, r=r, c=c, f1=f1, t1='真实成交', t2='真实未成交'
)
print(title)
print(output)
