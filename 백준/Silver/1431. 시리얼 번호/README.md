# [Silver III] 시리얼 번호 - 1431 

[문제 링크](https://www.acmicpc.net/problem/1431) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

정렬

### 문제 설명

<p>다솜이는 기타를 많이 가지고 있다. 그리고 각각의 기타는 모두 다른 시리얼 번호를 가지고 있다. 다솜이는 기타를 빨리 찾아서 빨리 사람들에게 연주해주기 위해서 기타를 시리얼 번호 순서대로 정렬하고자 한다.</p>

<p>모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.</p>

<p>시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.</p>

<ol>
	<li>A와 B의 길이가 다르면, 짧은 것이 먼저 온다.</li>
	<li>만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)</li>
	<li>만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.</li>
</ol>

<p>시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 기타의 개수 N이 주어진다. N은 50보다 작거나 같다. 둘째 줄부터 N개의 줄에 시리얼 번호가 하나씩 주어진다. 시리얼 번호의 길이는 최대 50이고, 알파벳 대문자 또는 숫자로만 이루어져 있다. 시리얼 번호는 중복되지 않는다.</p>

### 출력 

 <p>첫째 줄부터 차례대로 N개의 줄에 한줄에 하나씩 시리얼 번호를 정렬한 결과를 출력한다.</p>

### 👌 문제 이해
리스트로 입력 받아 정렬 하는데 주어진 조건대로 정렬하는 문제
1. 짧은 길이 순으로 정렬
2. 서로 길이가 같다면, 입력받은 문자중 숫자인것만 더한 합이 가장 작은 순으로 정렬
3. 1,2번이 똑같으면 사전 순으로 정렬

### 💡 문제 해결 방법
**알고리즘** : 정렬<br>
**이유** : python의 내장함수인 sort()함수를 이용하면 간편하게 풀 수 있음<br>

### 💻 코드
* 내가 작성한 코드
```python
from sys import stdin as s

#s=open("input.txt","rt")
num_list=['0','1','2','3','4','5','6','7','8','9']

N= int(s.readline())
siral_list=[]
for _ in range(N):
    count=0
    siral = s.readline().strip()
    for i in siral:
        if i in num_list:
            count+=int(i)
    num=len(siral)
    siral_list.append((num,siral,count))
siral_list.sort() #1. 비교하는 시리얼 번호 a,b가 길이가 다를때, 짧은 것이 먼저옴
for i in range(len(siral_list)):
    print(sorted(siral_list,key=lambda x : x[2])[i][1]) # 숫자인것만 더했을 때 더 작은 값을 먼저 놓는다.
```

* 해설을 참고해서 다시 작성한 코드

```python
from sys import stdin as s

#s=open("input.txt","rt")
#num_list=['0','1','2','3','4','5','6','7','8','9']
N= int(s.readline())
siral_list=[]
for _ in range(N):
    count=0
    siral = s.readline().strip()
    for i in siral:
        if i.isdigit():
            count+=int(i)
    num=len(siral)
    siral_list.append((num,siral,count))
#1. 비교하는 시리얼 번호 a,b가 길이가 다를때, 짧은 것이 먼저옴
siral_list.sort(key=lambda x : (x[0],x[2],x))# 숫자인것만 더했을 때 더 작은 값을 먼저 놓는다.
for i in range(len(siral_list)):
     print(siral_list[i][1])
```

### 🙄 틀린 이유와 해결책
정렬을 해줄때 lambda를 정확하게 이용하지 못하고 각 조건마다 정렬을 시도해 주었기 때문에 틀렸다. 이런 경우에 lambda를 이용해서 조건의 우선순위 순으로 정렬해주면 해결할 수 있다. <br>
```siral_list.sort(key=lambda x : (x[0],x[2],x))```

### lambda 개념 참고 사이트
[lambda 개념](https://velog.io/@sloools/Python3-%EC%A0%95%EB%A0%AC-%EB%9E%8C%EB%8B%A4-keylambda)

### 해설 참고 사이트
[시리얼 번호](https://velog.io/@sugenius77/%EB%B0%B1%EC%A4%80Python-1431%EB%B2%88-%EC%8B%9C%EB%A6%AC%EC%96%BC-%EB%B2%88%ED%98%B8)
