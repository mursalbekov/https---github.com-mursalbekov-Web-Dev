n = int(input())
s = 2
for i in range(n+1):
    if(i%s==0):
        print(s)
    else:
        s = s + 1