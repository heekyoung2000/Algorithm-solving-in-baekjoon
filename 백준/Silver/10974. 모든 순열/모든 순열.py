N= int(input())
visited = [False]*(N+1)
s=[]

def dfs():
    if len(s)==N:
        print(*s)
        return
    for i in range(1,N+1):
        if visited[i]==False:
            visited[i]=True
            s.append(i)
            dfs()
            s.pop()
            visited[i]=False
dfs()