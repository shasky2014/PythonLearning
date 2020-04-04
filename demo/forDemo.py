a = [0, 1, 2, 3, 4, 5, 6, 7]

print()

for i, ai in enumerate(a):
    if i == 5:
        continue
    print('====', i, ai)
