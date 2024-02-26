def solution(n, wires):
    answer = 100
    test = [[wires[i] for i in range(len(wires)) if i != j] for j in range(len(wires))] # 전선 하나씩 끊어보기
    
    for wire in test:
        graph = [[] for _ in range(n)] # 인접 리스트 생성
        visited = [False] * n
        for w in wire:
            graph[w[0]-1].append(w[1]-1) # 노드 양방향으로
            graph[w[1]-1].append(w[0]-1) # 연결 추가
        m = dfs(graph, visited, 0, 1) # 연결된 송전탑 수
        answer = min(answer, abs(n-2*m)) # 일부m과 (전체n - 일부m)으로 나눠짐. |(n-m) - m| = |n - 2*m|
    return answer

def dfs(graph, visited, start, n):
    visited[start] = True # 방문 처리
    for i in graph[start]:
        if not visited[i]:
            n = dfs(graph, visited, i, n+1) # n증가
    return n