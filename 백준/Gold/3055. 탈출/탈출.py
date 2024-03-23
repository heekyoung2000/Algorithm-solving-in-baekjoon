import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
roadmap = [list(input().strip()) for _ in range(R)]

water = deque()
q = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(R):
    for j in range(C):
        if roadmap[i][j] == "S":
            q.append((i, j))
        elif roadmap[i][j] == "D":
            end_x, end_y = i, j
        elif roadmap[i][j] == "*":
            water.append((i, j))


def water_bfs():
    num = len(water)
    for _ in range(num):
        w_x, w_y = water.popleft()
        for i in range(4):
            wx, wy = w_x + dx[i], w_y + dy[i]
            if 0 <= wx < R and 0 <= wy < C and roadmap[wx][wy] == ".":
                roadmap[wx][wy] = "*"
                water.append((wx, wy))


def bfs():
    time = 0
    while q:
        water_bfs()
        size = len(q)
        for _ in range(size): #동시에 이동하기 위해서는 반복문 사용해줘야함
            x, y = q.popleft()
            if x == end_x and y == end_y:
                return time
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and (roadmap[nx][ny] == "." or roadmap[nx][ny] == "D"):
                    roadmap[nx][ny] = "S"
                    q.append((nx, ny))
        time += 1 #시간마다 이동하므로 반복문이 끝난 후에 time +=1 동작
    return "KAKTUS"


result = bfs()
print(result)


