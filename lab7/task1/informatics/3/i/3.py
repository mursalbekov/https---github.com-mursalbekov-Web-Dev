import math

a = int(input())
b = int(input())

for i in range(a, b):
    x = int(math.sqrt(i))
    if x*x == i:
        print(i, end=' ')