n = int(input())
s = 1
cnt = 0
for i in range(n+1):
    if(n%s==0):
        cnt += 1
    s = s + 1
print(cnt)