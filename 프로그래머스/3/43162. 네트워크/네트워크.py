def solution(n, computers):
    answer = 0
    visited = [0]*n #방문 표시 리스트
    def dfs(pc):
        visited[pc]=1
        for i in range(n):
            if visited[i]==0 and computers[pc][i]:
                dfs(i)
    
    for pc in range(n):
        if visited[pc]==0:
            dfs(pc)
            answer+=1
                
    
    return answer