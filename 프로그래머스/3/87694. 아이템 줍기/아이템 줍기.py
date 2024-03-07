from collections import deque
def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    
    #map에 라인채우기
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2,r)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2: #내부
                    graph[i][j]=0
                elif graph[i][j]!=0: 
                    graph[i][j]=1 #테두리
    #bfs로 최단거리 탐색하기
    cx,cy,ix,iy=cx*2,cy*2,ix*2,iy*2
    queue=deque()
    queue.append((cx,cy))
    while queue:
        x,y=queue.popleft()
        if x==ix and y==iy:
            answer = visited[x][y]//2
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if visited[nx][ny]==1 and graph[nx][ny]==1:
                visited[nx][ny]+=visited[x][y]
                queue.append((nx,ny))
                
    
    return answer