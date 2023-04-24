from sys import stdin as s
from collections import deque


#s=open("input.txt","rt")


def bfs(graph,start,visited,k):
    
    queue = deque()
    queue.append(start) #큐에 시작 값을 넣어줌
    while queue:
        v= queue.popleft()
        visited[start]=True #visited에 방문 값을 true로 바꿔줌
        for i in graph[v]: 
            if not visited[i]: #만약 노드에 방문하지 않았다면
                queue.append(i) #큐에 노드를 추가하고
                visited[i]=True # 방문 true로 해준다음 
                go_list[i] = go_list[v]+1 #간선의 가중치 값을 올려줌

           

n,m,k,x = map(int,s.readline().split()) #n : 도시, m은 간선, k:최단 거리, x : 출발도시
list1 =[]
graph=[[] for _ in range(n+1)]
visited = [False]*(n+1) #방문 여부를 입력해줌
go_list = [0 for _ in range(n+1)] # 간선의 가중치를 저장해줌 
#도달할 수 있는 도시 입력받고 graph 배열에 1,2,3,4 차례로 넣어주기
for i in range(m):
    a,b=map(int,s.readline().split())
    graph[a].append(b)
    graph[a].sort()
bfs(graph,x,visited,k)
    


                
count=0
for i in range(1,n+1):
    if go_list[i]==k:
        print(i)
        count+=1
if count ==0:
    print(-1)    