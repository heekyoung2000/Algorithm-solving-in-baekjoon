# [Silver II] 좌표 압축 - 18870 

[문제 링크](https://www.acmicpc.net/problem/18870) 

### 성능 요약

메모리: 154804 KB, 시간: 1932 ms

### 분류

값 / 좌표 압축, 정렬

### 문제 설명

<p>수직선 위에 N개의 좌표 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.</p>

<p>X<sub>i</sub>를 좌표 압축한 결과 X'<sub>i</sub>의 값은 X<sub>i</sub> > X<sub>j</sub>를 만족하는 서로 다른 좌표의 개수와 같아야 한다.</p>

<p>X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>에 좌표 압축을 적용한 결과 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>를 출력해보자.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다.</p>

<p>둘째 줄에는 공백 한 칸으로 구분된 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>을 공백 한 칸으로 구분해서 출력한다.</p>

### 👌 문제 이해
주어진 리스트에서 각 값에 대해 그 값보다 작은 수의 개수를 차례대로 출력하는 문제 이때 중복하는 숫자는 제외

### 💡 문제 해결 방법
**알고리즘** : 정렬(딕셔너리)
**이유** : 정렬에 많은 방법이 있지만 리스트로 사용하게 되면 시간복잡도가 높아져서 시간초과가 나기 때문이다.

### 💻 코드
* 내가 쓴 코드<br>

이 방법은 시간초과가 난다.
```python
from sys import stdin as s
#s=open("input.txt","rt")
n=int(s.readline())
num_list=list(map(int,s.readline().split()))
count_list=[0*i for i in range(n)]
set_list=list(set(num_list))
for i in range(len(num_list)):
    for j in range(len(set_list)):
        if num_list[i]>set_list[j]:
            count_list[i]+=1
        else:
            continue
for i in count_list:
    print(i,end=" ")
```

* 다른 사람이 쓴 코드
```python
from sys import stdin as s
#s=open("input.txt","rt")
n=int(s.readline())
num_list=list(map(int,s.readline().split()))
set_list=sorted(set(num_list))

dic = {set_list[i]:i for i in range(len(set_list))}
for i in num_list:
    print(dic[i],end=" ")
```

### 🙄 틀린 이유와 해결책
정렬(리스트)로 풀었더니 초과가 났다. 
* 시간 복잡도 줄이기<br>

딕셔너리는 시간 복잡도가 O(1)이고 리스트는 O(n)이다. 따라서 리스트를 푸는 것 보다 시간 복잡도가 낮은 딕셔너리로 푸는 것이 좋다.

### 참고 해설
[참고](https://velog.io/@zinu/%EB%B0%B1%EC%A4%80-18870-%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95%ED%8C%8C%EC%9D%B4%EC%8D%AC)
