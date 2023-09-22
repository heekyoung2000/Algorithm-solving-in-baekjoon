from collections import deque
def solution(maps):
    answer = 0

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0:  continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))    # 재귀

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer    # 상대 팀 진영에 도착할 수 없을 때 -1
# from collections import deque

# def solution(maps):
#     dx=[0,1,0,-1]
#     dy=[1,0,-1,0]
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[0] * n] * m
#     def bfs(x,y):
#         q = deque()
#         q.append((x,y))
#         while q:
#             nx,ny=q.popleft()
#             visited[nx][ny]=1
#             for a in range(4):
#                 new_x = nx+dx[a]
#                 new_y = ny+dy[a]
#                 if 0<=new_x<m and 0<=new_y<n and maps[new_x][new_y]==1:
#                     maps[new_x][new_y]=maps[nx][ny]+1
#                     q.append((new_x,new_y))
                        
#     bfs(0,0)     
#     answer = maps[n-1][m-1]
#     if answer ==1:
#         answer=-1
#     return answer