n = int(input())
s = 1
for i in range(n+1):
    if(n%s==0):
        print(s, end=' ')
    s = s + 1