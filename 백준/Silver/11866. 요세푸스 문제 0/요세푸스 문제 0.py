from collections import deque
import sys

queue=deque()
list1=[]

n,k=map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    queue.append(i)
    
while queue:
    queue.rotate(-(k-1))
    list1.append(queue.popleft())

print(f'<{", ".join(map(str,list1))}>')
  