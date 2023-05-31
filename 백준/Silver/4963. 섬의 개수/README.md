# [Silver II] 섬의 개수 - 4963 

[문제 링크](https://www.acmicpc.net/problem/4963) 

### 성능 요약

메모리: 34192 KB, 시간: 80 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 문제 설명

<p>정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/island.png" style="width: 283px; height: 141px;"></p>

<p>한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. </p>

<p>두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.</p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.</p>

<p>둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.</p>

<p>입력의 마지막 줄에는 0이 두 개 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 섬의 개수를 출력한다.</p>
 
### 👌 문제 이해<br>
가로,세로 대각선으로 연결되어 있는 사각형은 연결되어 있다고 하면, 서로 떨어져 있는 섬의 개수를 구하는 문제
<br>
### 🤔 문제 해결 방법<br>
**알고리즘**:bfs<br>
**이유** : 사각형에서 탐색 문제가 나온다? 무조건 bfs아니면 dfs이다.<br>

### 💻 코드
* BFS를 이용한 코드

```python
from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")

dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        for z in range(8):
            nx=dx[z]+x
            ny=dy[z]+y
            if 0<=nx<h and 0<=ny<w:
                if ground_list[nx][ny]==1 and visited[nx][ny]==False:
                    queue.append((nx,ny))
                    visited[nx][ny]=True

while 1:
    ground_list=[]
    w,h=map(int,s.readline().split())
    visited=[[False]*w for _ in range(h)]
    cnt=0
    if w==0 and h==0:
        break
    else:
        for _ in range(h):
            list1=list(map(int,s.readline().split()))
            ground_list.append(list1)
        for i in range(h):
            for j in range(w):
                if ground_list[i][j]==1 and visited[i][j]==False:
                    bfs(i,j)
                    cnt+=1
        print(cnt)
                

```

* DFS를 이용한 코드


### 🤔 실수한 부분& 주의할 점
가로,세로, 대각선을 탐색할 때 만약 1이 근처에 있다면 1을 기준으로 다시 탐색해주어야 하는데 그 코드를 생각하지 못했다.<br>
* 처음 작성한 코드
```python
if 0<=nx<h and 0<=ny<w:
    if visited[nx][ny]==False:
        queue.append((nx,ny))
        visited[nx][ny]=True
```

* 다시 생각하고 작성한 코드
```python
if 0<=nx<h and 0<=ny<w:
    if ground_list[nx][ny]==1 and visited[nx][ny]==False:
            queue.append((nx,ny))
            visited[nx][ny]=True
```
<br>

 * 주의할 점<br>

> 가로 : 이차원 배열에서 [✅][] 세로 : 이차원 배열에서 [][✅]


