# [Gold V] 적록색약 - 10026 

[문제 링크](https://www.acmicpc.net/problem/10026) 

### 성능 요약

메모리: 34200 KB, 시간: 84 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 문제 설명

<p>적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.</p>

<p>크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)</p>

<p>예를 들어, 그림이 아래와 같은 경우에</p>

<pre>RRRBB
GGBBB
BBBRR
BBRRR
RRRRR</pre>

<p>적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)</p>

<p>그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)</p>

<p>둘째 줄부터 N개 줄에는 그림이 주어진다.</p>

### 출력 

 <p>적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.</p>

### 👌문제 이해
적록색약이 아닌 사람이 본 구역과 적록색약인 사람이 본 구역의 수를 차례로 출력하는 문제

### 💡 문제 해결 방법
**알고리즘** : bfs<br>
**이유** : 

적록색약이 봤을 떄 구역의 개수를 잘 설정해야 한다. 만약 g를 볼경우 r을 보는 경우와 같은 경우로 count해야 한다.<br>


### 💻 코드

* 내가 작성한 코드<br>
```python
from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

n=int(s.readline())
color_list=[]
visited=[[0 for _ in range(n)] for i in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
count=0  
cnt=0 
def bfs(x,y):
    queue=deque()
    if visited[x][y]==0:
        queue.append((x,y))
        orgin_color=color_list[x][y]
    while queue:
        nx,ny=queue.popleft()
        visited[nx][ny]=1
        for i in range(4):
            new_x=nx+dx[i]
            new_y=ny+dy[i]
            if 0<=new_x<n and 0<=new_y<n and color_list[new_x][new_y]==orgin_color and visited[new_x][new_y]==0:
                queue.append((new_x,new_y))
                    
    return

color_list = [list(s.readline().strip()) for _ in range(n)]

count=0  
cnt=0        
for a in range(n):
    for b in range(n):
        if visited[a][b]==0:
            bfs(a,b)
            count+=1
            
visited=[[0 for _ in range(n)] for i in range(n)]

for w in range(n):
    for v in range(n):
        if color_list[w][v]=="G":
            color_list[w][v]="R"
           
for q in range(n):
    for s in range(n):
       if visited[q][s]==0:
            bfs(q,s)
            cnt+=1

print(count, cnt)

```
* 다른 사람이 작성한 코드
```python
from collections import deque

def BFS(x,y):
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                q.append((nx,ny))


N = int(input())
a = [list(input()) for _ in range(N)]
q = deque()

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            BFS(i,j)
            cnt1 += 1

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt2 += 1

print(cnt1, cnt2)
```


### 🤔 틀린이유와 해결책
솔직히 계속 bounderror랑 시간초과 오류가 났는데 아직까지도 왜 그런지 이유를 모르겠다. 다른 사람들의 코드를 봐도 똑같이 짠 것 같은데 왜 내코드만 시간초과가 나는지 모르겠다ㅜㅜ 정답을 알려줘...
