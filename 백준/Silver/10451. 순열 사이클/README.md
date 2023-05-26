# [Silver III] 순열 사이클 - 10451 

[문제 링크](https://www.acmicpc.net/problem/10451) 

### 성능 요약

메모리: 34144 KB, 시간: 440 ms

### 분류

순열 사이클 분할

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images2/permut.png" style="float:right; height:134px; width:264px"></p>

<p>1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 예를 들어, 8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-mo class="mjx-s3"><mjx-c class="mjx-c28 TEX-S3"></mjx-c></mjx-mo><mjx-mtable style="min-width: 11em;"><mjx-table><mjx-itable><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr></mjx-itable></mjx-table></mjx-mtable><mjx-mo class="mjx-s3"><mjx-c class="mjx-c29 TEX-S3"></mjx-c></mjx-mo></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">(</mo><mtable columnspacing="1em" rowspacing="4pt"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>7</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>7</mn></mtd><mtd><mn>8</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>6</mn></mtd></mtr></mtable><mo data-mjx-texclass="CLOSE">)</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(\begin{pmatrix} 1 & 2 &3&4&5&6&7&8 \\  3& 2&7&8&1&4&5&6 \end{pmatrix}\)</span></mjx-container> 와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다.</p>

<p>순열을 배열을 이용해 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-mo class="mjx-s3"><mjx-c class="mjx-c28 TEX-S3"></mjx-c></mjx-mo><mjx-mtable style="min-width: 9.325em;"><mjx-table><mjx-itable><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-bottom: 0.2em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-top: 0.2em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D70B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D70B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-right: 0.5em; padding-top: 0.2em;"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-top: 0.2em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D70B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr></mjx-itable></mjx-table></mjx-mtable><mjx-mo class="mjx-s3"><mjx-c class="mjx-c29 TEX-S3"></mjx-c></mjx-mo></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">(</mo><mtable columnspacing="1em" rowspacing="4pt"><mtr><mtd><mn>1</mn></mtd><mtd><mo>…</mo></mtd><mtd><mi>i</mi></mtd><mtd><mo>…</mo></mtd><mtd><mi>n</mi></mtd></mtr><mtr><mtd><msub><mi>π</mi><mn>1</mn></msub></mtd><mtd><mo>…</mo></mtd><mtd><msub><mi>π</mi><mi>i</mi></msub></mtd><mtd><mo>…</mo></mtd><mtd><msub><mi>π</mi><mi>n</mi></msub></mtd></mtr></mtable><mo data-mjx-texclass="CLOSE">)</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(\begin{pmatrix} 1 & \dots & i & \dots &n \\  \pi_1& \dots& \pi_i & \dots & \pi_n \end{pmatrix}\)</span></mjx-container> 로 나타냈다면, i에서 π<sub>i</sub>로 간선을 이어 그래프로 만들 수 있다.</p>

<p>Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.</p>

<p>N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.</p>

### 출력 

 <p>각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.</p>
 
### 💡 문제 해결 방법
**알고리즘** : bfs<br>
**이유** : dfs로도 풀수 있는데 가장 익숙한 bfs로 풀었다. 다음에는 좀 더 코드 길이가 짧고 좋은 알고리즘으로 풀어보자<br>

- visited 함수를 생성해서 방문했을 시 true로 바꾸어 주고 방문하지 않은 노드를 찾다가 방문한 노드를 재방문 했을 시 멈추고 cnt+=1을 해준다.

### 💻코드
* 내가 작성한 코드(bfs)<br>
사실 이 코드도 다른 사람의 해설을 참고해서 작성한 코드이다..


```python
from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

def bfs(i):
    queue = deque([number_list[i]])
    while queue:
        v=queue.popleft()
        visited[v]=True
        n=number_list[v]
        if not visited[n]:
            queue.append(number_list[n])
            visited[n]=True

t=int(s.readline())
for _ in range(t):
    n=int(s.readline())
    visited =[False]*(n+1)
    visited[0]=True
    number_list=[0]
    cnt=0
    num_list=list(map(int,s.readline().split()))
    for i in num_list:
        number_list.append(i)
    for i in range(1,len(number_list)):
        if visited[i]==False:
            bfs(i)
            cnt+=1
    print(cnt)
```

* dfs로 작성한 다른사람의 풀이

```python
import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

def dfs(x): #DFS 함수 정의
    visited[x] = True #방문 체크
    number = numbers[x] #다음 방문 장소
    if not visited[number]: #방문하지 않았다면
        dfs(number) #재귀

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문여부확인용
    result = 0
    
    for i in range(1, N+1):
        if not visited[i]: #방문하지 않았다면
            dfs(i) #DFS실행
            result += 1 #결과값 += 1
    print(result)
```
### 🤔 틀린 이유와 해결 책
*일단 제일 큰 문제는 너무 졸려서 머리가 안돌아 갔다는 것이다... 사실 이건 변명*<br>
한 사이클을 탐색 완료 했을 때 그 다음 사이클을 탐색하는 방법을 생각하지 못하고 다시 처음부터 탐색을 시작하는 코드로 작성했다. 특히 해설을 참고해서 작성했을 때는 ```visited =true```를 처음 부터 설정해주는 바람에 답이 다르게 출력되었다. 잘 생각하고 코드를 작성하자...<br>
```visited =true```가 while 문 안에 들어가야 하는데 밖에 작성해주어서 틀렸다...
```python
 while queue:
        v=queue.popleft()
        visited[v]=True
```
#### 참고한 사이트<br>
[순열 사이클](https://wookcode.tistory.com/164)
[순열 사이클- dfs](https://claude-u.tistory.com/434)

