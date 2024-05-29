from collections import deque
def bfs(w,n,graph): #bfs 수행을 통해 연결된 노드수 구하기
    count=1 #연결된 노드 수
    visited=[False]*(n+1)
    visited[w[0]]=True
    queue = deque([w[0]])
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] or i==w[1]: #방문했거나 끊어지는 부분의 노드인 경우 패스
                continue
            count+=1
            queue.append(i)
            visited[i]=True
    return count
    
    
def solution(n, wires):
    result = 100000000
    graph = [[]*i for i in range(n+1)]

    # 양방향 간선 추가
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    #bfs로 완전탐색
    for w in wires:
        #와이어를 끊었을 때 한쪽 영역의 노드 수 구하기
        temp = bfs(w,n,graph)
        
        result = min(result,abs(n-temp-temp))
    return result