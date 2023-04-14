import sys
#from sys import stdin as s
from collections import deque

dq=deque()

#s=open('input.txt','rt')
n = int(sys.stdin.readline().strip())

for i in range(1,n+1):
    dq.append(i)
    
while len(dq)>1:
    first=dq.popleft()
    second=dq.popleft()
    dq.append(second)    
print(dq[0])
        