# [Silver I] 스타트링크 - 5014 

[문제 링크](https://www.acmicpc.net/problem/5014) 

### 성능 요약

메모리: 71248 KB, 시간: 520 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 문제 설명

<p>강호는 코딩 교육을 하는 스타트업 <a href="https://startlink.io">스타트링크</a>에 지원했다. 오늘은 강호의 면접날이다. 하지만, 늦잠을 잔 강호는 스타트링크가 있는 건물에 늦게 도착하고 말았다.</p>

<p>스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다. 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.</p>

<p>보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 강호가 탄 엘리베이터는 버튼이 2개밖에 없다. U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)</p>

<p>강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오. 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.</p>

### 입력 

 <p>첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.</p>

### 출력 

 <p>첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다. 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다.</p>
 
 
 > reference<br>
[스타트링크 파이썬 풀이](https://haejun-kim.tistory.com/m/36)

### 👌문제 이해
f= 총 건물 층수<br>
g = 스타크링크가 있는 층수<br>
s = 강호가 현재 있는 층수<br>
u - up 버튼<br>
d - down 버튼<br>
입력에 f,g,s,u,d가 주어진다고 할 때 강호가 s층에서 g층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 구하는 문제<br>
이 때 엘리베이터 버튼은 u,d만 존재하고 만약 엘리베이터를 이용해서 g층에 갈 수 없으면 "use the stairs"를 출력한다.

### 💡 문제 해결 방법
**알고리즘** : bfs<br>
**이유** :

visited 리스트를 생성하고 인덱스 값 만큼 누적합을 저장하여 g층에 도착했을 경우 누적합-1을 출력하고 도착하지 못했을 경우  "use the stairs"를 출력<br>
* 누적합-1을 해주는 이유 : 처음 시작지졈을 1로 시작하기 때문

### 💻 코드
```python
from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")

F,S,G,U,D=map(int,s.readline().split())
#f= 총 건물 층수
#g = 스타크링크가 있는 층수
#s = 강호가 현재 있는 층수
#u - up 버튼
#d - down 버튼
visited=[0 for _ in range(F+1)]

def bfs():
    queue=deque()
    queue.append(S)
    visited[S]=1
    while queue:
        v=queue.popleft()
        if v==G:
            return visited[v]-1
        else:
            for x in (v+U,v-D):
                if 0<x<=F and visited[x]==0:
                    visited[x]=visited[v]+1
                    queue.append(x)
     
    return "use the stairs"
               
print(bfs())
```

### 🤔 틀린 이유와 해결책
dfs로 풀려고 그랬는데 풀리지 않았고 어떻게 풀어야 할지도 몰랐다.
이 문제와 비슷한 유형의 문제를 많이 풀어야 겠다.


