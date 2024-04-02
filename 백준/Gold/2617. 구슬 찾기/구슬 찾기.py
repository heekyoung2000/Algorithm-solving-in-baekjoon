import sys
input = sys.stdin.readline

N,M = map(int,input().split())
heavy_list = [[] for _ in range(N+1)]
light_list = [[] for _ in range(N+1)]

## 1.대소관계 정리
for _ in range(M):
    a,b = map(int,input().split())
    heavy_list[b].append(a)
    light_list[a].append(b)


## 2.연결된 구슬 개수 구하기
def DFS(list,root):
    count=0
    for node in list[root]:
        if visited[node]==False:
            visited[node]=True
            count+=1
            count+=DFS(list,node)
    return count


## 3. 중간값이 가능한지 검증
mid=(N+1)//2
result=0
for i in range(1,N+1):
    visited=[False]*(N+1)
    if DFS(heavy_list,i)>=mid:
        result+=1
    if DFS(light_list,i)>=mid:
        result+=1
print(result)
