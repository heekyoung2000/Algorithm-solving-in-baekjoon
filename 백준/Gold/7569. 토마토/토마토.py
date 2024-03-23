import sys
from collections import deque
input = sys.stdin.readline
n,m,h = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(m) ] for _ in range(h)]


dx=[0,0,1,0,0,-1]
dy=[0,1,0,0,-1,0]
dh=[1,0,0,-1,0,0]
day=0
unripe = 0 
    
                
true_queue=deque()
false_queue = deque()
for i in range(h):
    for j in range(m):
        for z in range(n):
            if tomato[i][j][z]==1: ## 익은 토마토
                true_queue.append((i,j,z))
            elif tomato[i][j][z]==0: ## 익지 않은 토마토
                unripe+=1
            else:
                continue
if unripe==0: # 토마토가 이미 다 익은 상황
    print(0)
elif len(true_queue)==0: #익은 토마토가 없는 상황
    print(-1)
else:
    while true_queue:
        for _ in range(len(true_queue)):
            NH,NY,NX = true_queue.popleft()
            for i in range(6):
                NEWH,NEWY,NEWX = NH+dh[i],NY+dy[i], NX+dx[i]
                if 0<=NEWH<h and 0<=NEWY<m and 0<=NEWX<n and tomato[NEWH][NEWY][NEWX]==0:
                    tomato[NEWH][NEWY][NEWX]=1
                    true_queue.append((NEWH,NEWY,NEWX))
                    unripe -=1
        
            if len(true_queue)== 0 and unripe == 0:
                print(day)
            elif len(true_queue)==0 and unripe!=0:
                print(-1)
        day+=1