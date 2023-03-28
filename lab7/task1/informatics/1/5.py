import math
v = int(input())
t = int(input())
if(v * t > 109):
    print(v * t - 109)
elif(v * t < 109 and v * t > 0):
    print(v * t)
elif(v < 0):
    print((109-(-v*t)))