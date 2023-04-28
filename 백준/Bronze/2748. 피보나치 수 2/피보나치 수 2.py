from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")
n=int(s.readline())

d=[0]*100
def fibo(n):
    if n==1 or n==2:
        return 1
    if d[n]!=0:
        return d[n]
    d[n]=fibo(n-1)+fibo(n-2)
    return d[n]
print(fibo(n))