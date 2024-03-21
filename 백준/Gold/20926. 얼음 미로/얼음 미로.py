import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
board=[]
W,H = map(int,input().split())
distance = [[INF]*W for _ in range(H)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for _ in range(H):
    board.append(list(input().strip()))
for i in range(H):
    for j in range(W):
        if board[i][j]=="T":
            start_x,start_y= i,j
        elif board[i][j]=="E":
            end_x,end_y=i,j
            
def move(x,y,dir):
    slide=0
    while True:
        nx,ny = x+dx[dir],y+dy[dir]
        
        # 다음 칸이 절벽
        if not (0<=nx<H and 0<=ny<W):
            return -1
        # 다음 칸이 구멍
        if board[nx][ny]=='H':
            return -1
        # 다음 칸이 바위
        if board[nx][ny]=="R":
            return [x,y,slide,dir]
        # 다음 칸이 출구
        if board[nx][ny]=="E":
            return [nx,ny,slide,dir]
        # 다음 칸이 출발점 : 사이클 방지
        if nx==start_x and ny==start_y:
            return -1
        # 다음 칸이 평범
        x,y=nx,ny
        slide += int(board[nx][ny])
            
def dijkstra(x,y):
    q=[]
    heapq.heappush(q,(0,x,y))
    distance[x][y]=0
    board[x][y]=0
    
    while q:
        dis,new_x,new_y = heapq.heappop(q)
        
        if dis>distance[new_x][new_y]:
            continue
        for i in range(4):
            result=move(new_x,new_y,i)
            if result==-1: continue
            nx,ny,addSlide,dir = result
            sumSlide = addSlide + dis
            
            if distance[nx][ny] > sumSlide:
                distance[nx][ny]=sumSlide
                heapq.heappush(q,(sumSlide,nx,ny))
            
                
dijkstra(start_x,start_y)
ans = distance[end_x][end_y]
if ans==INF:
    print(-1)
else :
    print(ans)
                    
                    
                    