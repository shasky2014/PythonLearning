def ppp(a, b, *args, **kwargs):
    print('a={},b={}'.format(a, b))
    pass


conf = dict(a=2, c=5, b='dsfdsf d', d=9)

ppp(2, 4)
ppp(**conf)
