def solution(board):
    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[1,1,0,-1,-1,-1,0,1]
    n=len(board)
    visited=[[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for x in range(8):
                    nx=i+dx[x]
                    ny=j+dy[x]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]!=1:
                        board[nx][ny]=2
    count=0
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                count+=1
    
    return count
# (-1,1) (0,1)  (1,1)
# (-1,0) (0,0)  (1,0)
# (-1,-1)(0,-1) (1,-1)