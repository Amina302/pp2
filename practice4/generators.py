#1
def square(n):
    for i in range (1,n+1):
        yield i*i
n=int(input())
for x in square(n):
    print (x,end=" ")
print("\n")

#2
def even(n):
    for i in range (0,n+1):
        if i%2==0:
            yield i
n=int(input())
print (",".join(str(x) for x in even(n)))
print("\n")

#3
def divisble(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for x in divisble(n):
    print (x,end=" ")
print("\n")

#4
def squares(a,b):
    for i in range (a,b+1):
        yield i*i
a=int(input())
b=int(input())
for v in squares(a,b):
    print(v,end=" ")
print("\n")

#5
def downtozero(n):
    while n>=0:
        yield n
        n-=1
n=int(input())
for z in downtozero(n):
    print (z,end=" ")
print("\n")