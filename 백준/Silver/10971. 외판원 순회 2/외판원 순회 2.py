import sys
n = int(sys.stdin.readline())
visited = [0]*n
new_list = []
result = 1e9

def dfs(node,x,cost):
    global result
    
    if x==n:
        if new_list[node][0]:
            result = min(result,cost+new_list[node][0])
        return
    for next_node in range(1,n):
        if not visited[next_node] and new_list[node][next_node]:
            visited[next_node]=True
            dfs(next_node,x+1,cost+new_list[node][next_node])
            visited[next_node]=False
            
for i in range(n):
    list1=list(map(int,sys.stdin.readline().split()))
    new_list.append(list1)
    
dfs(0,1,0)
print(result)