from collections import deque
def solution(n, computers):
    answer = 0
    connect = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    
    def bfs(node):
        q = deque()
        q.append(node)
        while q:
            N = q.popleft()
            if visited[N]==False and connect[N]!=[]:
                visited[N]=True
                for c in connect[N]:
                    q.append(c)
                    
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                connect[i+1].append(j+1)

    for a in range(1,n+1):
        if visited[a]==False:
            bfs(a)
            answer+=1
    return answer