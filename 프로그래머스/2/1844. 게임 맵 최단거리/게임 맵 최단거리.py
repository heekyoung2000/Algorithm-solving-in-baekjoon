from collections import deque

def solution(maps):
    answer=0
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    def bfs(x,y):
        queue=deque()
        queue.append((x,y))
        while queue:
            n_x,n_y=queue.popleft()
            for i in range(4):
                new_x=n_x+dx[i]
                new_y=n_y+dy[i]
                if new_x< 0 or new_x>=len(maps) or new_y < 0 or new_y>=len(maps[0]):
                    continue
                if maps[new_x][new_y]==0:
                    continue
                if maps[new_x][new_y]==1:
                    maps[new_x][new_y]=maps[n_x][n_y]+1
                    queue.append((new_x,new_y))
        return maps[len(maps)-1][len(maps[0])-1]


    answer= bfs(0,0)
    return -1 if answer==1 else answer
    
    
    