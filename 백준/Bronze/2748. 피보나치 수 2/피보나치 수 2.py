#바텀 업 방식
from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")
n=int(s.readline())
d=[0]*100
d[1]=1
d[2]=1
for i in range(3,n+1):
    d[i]= d[i-1]+d[i-2]
    
print(d[n])