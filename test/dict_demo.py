a = {}
a.setdefault(46, dict())
print(a)
print(a[46])
a[46]['zsq'] = []
print(a)
print(a[46])
a[46]['xsq'] = []
print(a)
print(a[46])

a = {
    46: {
        'zsq': [],
        'xsq': [],
        'jxy': []
    },
    47: {
        'zsq': [],
        'xsq': [],
        'jxy': []
    }
}

print(a)
