import math

# x = number of companies interviewed with onsite
# y = number of offers received
x = 50
y = 50
value = 100 * math.log1p(x) * y / x
print(value)
