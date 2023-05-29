# [Silver II] 결혼식 - 5567 

[문제 링크](https://www.acmicpc.net/problem/5567) 

### 성능 요약

메모리: 34128 KB, 시간: 72 ms

### 분류

그래프 이론, 그래프 탐색

### 문제 설명

<p>상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.</p>

<p>상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다. 둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다. 다음 줄부터 m개 줄에는 친구 관계 a<sub>i</sub> b<sub>i</sub>가 주어진다. (1 ≤ a<sub>i</sub> < b<sub>i</sub> ≤ n) a<sub>i</sub>와 b<sub>i</sub>가 친구라는 뜻이며, b<sub>i</sub>와 a<sub>i</sub>도 친구관계이다. </p>

### 출력 

 <p>첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.</p>

### 👌 문제 이해
상근이가 친구들을 결혼식에 초대하려고 하는데 상근이의 친구와 친구의 친구까지 초대하려고 할때 결혼식에 초대하는 동기의 수를 출력하는 문제

### 💡 문제 해결 방법<br>
**알고리즘** : bfs<br>
**이유** : 깊이 탐색이 아니라 너비 탐색을 해야한다고 생각했기 때문<br>
사실 dfs로 풀어도 상관 없음

### 💻 코드
* 내가 작성한 코드<br>
이게 무슨 개똥같은 코드야
```python
from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

n=int(s.readline())
m=int(s.readline())
friend_list=[[] for _ in range(n+1)]

def bfs(start):
    num=0
    queue=deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for j in friend_list[v]:
            if visited[j]==0:
                num+=len(friend_list[j])
                visited[j]=1
    
    return num
    
count=0
visited = [0]*(n+1)
visited[1]=1
for i in range(m):
    a,b=map(int,s.readline().split())
    friend_list[a].append(b)
count+=bfs(1)
for s in friend_list[1]:
    count+=bfs(s)

print(count)
```
* 다른 코드 보고 다시 작성한 코드
```python
from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

n=int(s.readline())
m=int(s.readline())
friend_list=[[] for _ in range(n+1)]

count=0
visited = [0]*(n+1)
visited[1]=1
for i in range(m):
    a,b=map(int,s.readline().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

for s in friend_list[1]:
    if not visited[s]:
        visited[s]=1
        count+=1
    for j in friend_list[s]:
        if not visited[j]:
            visited[j]=1
            count+=1

print(count)
```

### 🤔 틀린 이유와 해결책
bfs로 풀어야 한다는 것은 알았지만 친구의 친구를 찾아주는 과정에서 이미 방문한 노드를 다시 count를 해주어서 틀렸다. 해결책은 상근이의 친구와 친구의 친구를 count해주는 코드를 따로 작성했다.
