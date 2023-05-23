# [Gold V] 수 고르기 - 2230 

[문제 링크](https://www.acmicpc.net/problem/2230) 

### 성능 요약

메모리: 39268 KB, 시간: 220 ms

### 분류

정렬, 두 포인터

### 문제 설명

<p>N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.</p>

<p>예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자. 만약 M = 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 이 중에서 차이가 가장 작은 경우는 1 4나 2 5를 골랐을 때의 3이 된다.</p>

### 입력 

 <p>첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 차례로 A[1], A[2], …, A[N]이 주어진다.</p>

### 출력 

 <p>첫째 줄에 M 이상이면서 가장 작은 차이를 출력한다. 항상 차이가 M이상인 두 수를 고를 수 있다.</p>
 
 
### 💡 문제 해결 방법
**알고리즘 : 정렬, 투포인터**<br>
**이유 : 정렬로 풀어야 좀 더 편함**<br>

투포인터로 풀었지만 정확한 개념을 알아둬야 할 것 같다.
***
### 💻코드
* 원래 작성했던 코드
```python
from sys import stdin as s
#s=open("input.txt","rt")
n,m = map(int,s.readline().split())
array=[]
result=[]
for _ in range(n):
    num=int(s.readline().strip())
    array.append(num)
array.sort()
## 투포인터 사용
i=0
j=len(array)-1
while i<len(array) and j>0:
    dif = abs(array[i]-array[j])
    if m <=dif:
        result.append(dif)
        i+=1
    else:
        j-=1
print(min(result))
```

* 해설을 참고해서 다시 작성한 코드
```python
from sys import stdin as s
s=open("input.txt","rt")

n,m = map(int,s.readline().split())
array=[]
result=[]
for _ in range(n):
    num=int(s.readline().strip())
    array.append(num)
array.sort()
## 투포인터 사용
i=0
j=0
while i<len(array) and j<len(array):
    dif = abs(array[i]-array[j])
    if m <=dif:
        result.append(dif)
        i+=1
    if m>dif:
        j+=1
print(min(result))
```

***
### 🙄 틀린이유와 해결책
투포인터를 설정할 때 left와 right를 모두 0으로 설정해서 브루트탐색법을 이용해야 하는데 left를 배열 끝점으로 설정함으로써 완전탐색을 하지 못했다. 따라서 left를 0으로 설정하였다.
