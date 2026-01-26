a=int(input())
n=list(map(int,input().split()))
m=0
for i in range (a):
    if (n[i]>m):
        m=n[i]

print (m)