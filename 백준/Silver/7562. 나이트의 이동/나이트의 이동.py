import sys
from collections import deque
test_case = int(sys.stdin.readline().strip())

#(-2,1)(-1,2)	(1,2) (2,1)
#(-2,-1)(-1,-2)	(1,-2)(2,-1)

# 1(2,1)
# 2,1
# 2(2,1)
# 4,2

# 3(2,1)
# 6,3

# 4(-1,-2)
# 5,1

# 5(2,-1)
# 7,0
dx = [1,2,1,2,-2,-1,-2,-1]
dy = [2,1,-2,-1,-1,-2,1,2]


def bfs(x,y,count):
    q = deque()
    q.append((x,y,count))
    while q:
        x,y,count=q.popleft()
        if x==m_x and y==m_y:
            return count
        for i in range(8):
            nx = x+dx[i]
            ny= y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==False:
                q.append((nx,ny,count+1))
                visited[nx][ny]=True
                
            

for _ in range(test_case):
    l = int(sys.stdin.readline().strip())
    x,y = map(int,sys.stdin.readline().split())
    m_x,m_y = map(int,sys.stdin.readline().split())
    maped = [[0 for j in range(l)] for i in range(l)]
    visited=[[False for j in range(l)] for i in range(l)]
    
    
    if x==m_x and y==m_y:
        print(0)
    else:
        print(bfs(x,y,0))