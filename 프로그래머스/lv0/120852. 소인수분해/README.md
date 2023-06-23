# [level 0] 소인수분해 - 120852 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120852) 

### 성능 요약

메모리: 71 MB, 시간: 2.17 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 <code>n</code>이 매개변수로 주어질 때 <code>n</code>의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>n</code> ≤ 10,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>12</td>
<td>[2, 3]</td>
</tr>
<tr>
<td>17</td>
<td>[17]</td>
</tr>
<tr>
<td>420</td>
<td>[2, 3, 5, 7]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>12를 소인수분해하면 2 * 2 * 3 입니다. 따라서 [2, 3]을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>17은 소수입니다. 따라서 [17]을 return 해야 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>420을 소인수분해하면 2 * 2 * 3 * 5 * 7 입니다. 따라서 [2, 3, 5, 7]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

### 🤔 문제 해결 방법
* 소인수분해: while문을 통해 돌면서 만약 2부터 시작하는 i값이 n과 나누었을 때 나머지가 0이면 list에 추가하고 n을 i로 나누어 준다. 그후 계속 반복한다.

### 💻 다른 사람 코드

``java

import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer = new int[n];
        List<Integer> result = new ArrayList<>();
        int i=2;

        while(n>=2){
            if(n%i==0){
                result.add(i);
                n=n/i;
            }
            else{
                i++;
            }
        }
        
        answer = result.stream().distinct().mapToInt(Integer::intValue).toArray();
        
        return answer;
        
    }
}

```

### 🙄 틀린 이유와 해결할 점
뭔가 자바는 리스트로 받는 것도 그냥 받는 게 아니라 arraylist로 받아 줘야 해서 꼭 선언을 해줘야 한다. 또한 프로그래머스 에서는 결과값을 int[]으로 출력될 수 있도록 했으므로 변경해주어야 한다는 점이 어려웠다.
* 알아 두어야 할 함수(?)
1. ```List<Integer> result = new ArrayList<>();``` 이 코드는 list를 선언할 때 사용되는 코드
2. ```list.stream().distinct().mapToInt(Integer::intValue).toArray();``` 이 코드는 스트림 개념이라고 하는데 스트림을 intstream으로 변경하는 과정이라고 한다... 이 개념은 아직 잘 모르겠으므로 다시 볼 것
