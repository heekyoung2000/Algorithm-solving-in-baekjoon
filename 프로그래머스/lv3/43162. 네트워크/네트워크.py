from collections import deque

def solution(n, computers):
    answer=0
    num = len(computers)
    visited = [0]*num
    for i in range(num):
        if bfs(i,num,visited,computers)==True:
            answer+=1
    return answer

def bfs(x,num,visited,computers):
    if visited[x]==True:
        return False
    queue = deque([computers[x]])
    visited[x]=1
    
    while queue:
        node=queue.popleft()
        for j in range(num):
            if j!=x and node[j]==1:
                if visited[j]==0:
                    visited[j]=1
                    queue.append(computers[j])
    return True
            