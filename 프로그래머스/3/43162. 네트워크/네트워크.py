from collections import deque
def solution(n, computers):
    answer=0
    def bfs(v,visited):
        queue=deque([v])
        while queue:
            j=queue.popleft()
            for i in range(n):
                if computers[i][j]==1 and visited[i+1]==False:
                    queue.append(i)
                    visited[i+1]=True
        return


    visited=[False for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and visited[j+1]==False:
                visited[j+1]=True
                visited[i+1]=True
                bfs(j,visited)
                answer+=1
            else:
                continue
    return answer
    
