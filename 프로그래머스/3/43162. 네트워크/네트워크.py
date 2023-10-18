def solution(n, computers):
    visited=[0]*n
    answer = 0
    def dfs(i):
        visited[i]=1
        for idx,c in enumerate(computers[i]):
            if c and visited[idx]==0:
                dfs(idx)
    
    for i in range(n):
        if visited[i] ==0:
            dfs(i)
            answer+=1
    return answer


    