from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

# bfs로 풀기..?

def bfs(i):
    queue = deque([number_list[i]])
    while queue:
        v=queue.popleft()
        visited[v]=True
        n=number_list[v]
        if not visited[n]:
            queue.append(number_list[n])
            visited[n]=True
        
    

t=int(s.readline())
for _ in range(t):
    n=int(s.readline())
    visited =[False]*(n+1)
    visited[0]=True
    number_list=[0]
    cnt=0
    num_list=list(map(int,s.readline().split()))
    for i in num_list:
        number_list.append(i)
    for i in range(1,len(number_list)):
        if visited[i]==False:
            bfs(i)
            cnt+=1
    print(cnt)