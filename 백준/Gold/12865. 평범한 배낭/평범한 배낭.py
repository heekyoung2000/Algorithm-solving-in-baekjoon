from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")
n,k=map(int,s.readline().split())

table=[[0 for i in range(k+1)] for _ in range(n+1)]

stuff = [[0,0]]
for i in range(n):
    w,v = map(int,s.readline().split())
    stuff.append([w,v])

for i in range(1,n+1):
    for j in range(1,k+1):
        weight=stuff[i][0]
        value = stuff[i][1]
        if j<weight:
            table[i][j]=table[i-1][j]
        else:
            table[i][j]=max(table[i-1][j],table[i-1][j-weight]+value)
            
print(table[n][k])