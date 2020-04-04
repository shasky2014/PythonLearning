print(list(filter(lambda x: x % 2 == 0, range(1, 101))))
import random

x = list(range(1, 101))

print(x)
random.shuffle(x)
print(x)
print(list(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 0, enumerate(x)))))
print(list(map(lambda x: 2 * x[1], filter(lambda x: x[0] % 2 == 0,
                                          enumerate(x)))))
