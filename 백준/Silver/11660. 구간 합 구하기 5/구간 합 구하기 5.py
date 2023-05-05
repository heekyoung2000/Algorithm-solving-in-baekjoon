from sys import stdin as s
from collections import deque

#n:표의 크기 , m은 합을 구해야 하는 횟수
#s=open("input.txt","rt")
n,m=map(int,s.readline().split())
sum_table=[]
dp_table=[[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    list1=list(map(int,s.readline().split()))
    sum_table.append(list1)


for i in range(1,n+1):
    for j in range(1,n+1):
        dp_table[i][j] = sum_table[i-1][j-1] + dp_table[i-1][j]+dp_table[i][j-1]-dp_table[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2=map(int,s.readline().split())
    result= dp_table[x2][y2]-dp_table[x1-1][y2]-dp_table[x2][y1-1]+dp_table[x1-1][y1-1]
    print(result)