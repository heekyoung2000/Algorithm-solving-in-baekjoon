# [Gold V] 보물섬 - 2589 

[문제 링크](https://www.acmicpc.net/problem/2589) 

### 성능 요약

메모리: 120984 KB, 시간: 872 ms

### 분류

너비 우선 탐색, 브루트포스 알고리즘, 그래프 이론, 그래프 탐색

### 문제 설명

<p>보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images/c1bYIsKpI6m317EAx.jpg" style="width: 238px; height: 144px; "></p>

<p>예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images/XqDkWCRUWbzZ.jpg" style="width: 238px; height: 144px; "></p>

<p>보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.</p>

### 출력 

 <p>첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.</p>

>reference : [보물섬 파이썬 풀이](https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-2589-%EB%B3%B4%EB%AC%BC%EC%84%AC)


### 👌문제 이해
보물섬이 가로와 세로 길이 입력을 통해 주어지는데, 이때 "L"은 육지 "w"은 바다이다. 한칸 이동하는데 한시간이 걸리며, 보물 2개가 묻혀있는데 최단거리로 이동하는데 2개를 찾는데 걸리는 시간이 가장 긴시간이 걸리는 육지 2곳에 묻혀있다. 

### 💡 문제 해결 방법
**알고리즘** : bfs<br>
**이유** : 

* 처음 생각했던 풀이<br>
각 땅 중에서 방문하지 않은 땅을 탐색해서 최장 시간을 구하고 구역별로 리스트에 저장후 min함수를 통해 최소값을 찾는다.

* 정답 풀이<br>
모든 땅을 탐색(bfs)를 돌려서 최장 거리로 구하고 그중 최단 시간을 출력한다.


### 💻 코드

* 내가 작성한 코드<br>
```python
from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

w,h = map(int,s.readline().split())

present_list= [list(s.readline().strip()) for _ in range(w)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]


def bfs(x,y):
    cnt=0
    queue=deque()
    queue.append((x,y))
    visited = [[0]*(h) for _ in range(w)]
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
        for z in range(4):
            nx=dx[z]+x
            ny=dy[z]+y
            if 0<=nx<w and 0<=ny<h and visited[nx][ny]==0:
                if present_list[nx][ny]=="L":
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    cnt=max(cnt,visited[nx][ny])        
    return cnt-1
    

result=0
for i in range(w):
    for j in range(h):
        if present_list[i][j]=="L":
            result=max(result,bfs(i,j))
print(result)

```
* 다른 사람이 작성한 코드(python으로 통과함!!)
```python
from collections import deque

n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]

dq = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    max_val = -2147000000
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                max_val = visited[nx][ny]
                dq.append([nx, ny])
    return max_val-1

res = -2147000000

for i in range(n):
    for j in range(m):
        visited = [[0]*m for _ in range(n)]
        if board[i][j] == 'L':
            # python3 최적화
            if 0<=i-1<n and 0<=i+1<n:
                if board[i-1][j] == 'L' and board[i+1][j] == 'L': continue
            if 0<=j-1<m and 0<=j+1<m:
                if board[i][j-1] == 'L' and board[i][j-1] == 'L': continue

            visited[i][j] = 1
            dq.append([i,j])
            res = max(BFS(), res)

print(res)
```


### 🤔 틀린이유와 해결책
이러한 유형의 문제를 풀어보지 못해서 못푼걸까..? 기존 bfs 방식과 똑같았지만 방문한 노드만 bfs를 도는 것이 아니라 한칸한칸 bfs를 도는 것이 포인트 였다. 또한 python3로 돌리면 시간초과가 떠서 pypy3으로 해서 통과했다. python3으로 통과한 다른 사람의 코드를 보고 다시 공부해보자.
