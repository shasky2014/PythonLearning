a = list(range(1, 244))
print(a)

b = [a[i:(i + 20)] for i in range(0, len(a), 20)]
print(b)
print(a[240:240 + 20])
print(a[240:260])

l = [-10260, -30200, -23600, -28900, -29900, -39800, -39800, -35900, -49900, -15000, -12000, -29900, -20000, -22000,
     -41300, -48900, -39900, -20000, -10000, -29900, -13519, -30580, -20000, -30800, -30200, -40200, -40200, -41300,
     -39600, -58900, -29900, -10000, -20000, -19900
     ]

print(sum(l) / 100)
