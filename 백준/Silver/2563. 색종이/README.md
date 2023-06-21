# [Silver V] 색종이 - 2563 

[문제 링크](https://www.acmicpc.net/problem/2563) 

### 성능 요약

메모리: 14212 KB, 시간: 124 ms

### 분류

구현

### 문제 설명

<p>가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6000c956-1b07-4913-83c3-72eda18fa1d1/-/preview/" style="width: 268px; height: 215px;"></p>

<p>예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.</p>

### 입력 

 <p>첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다</p>

### 출력 

 <p>첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.</p>


### 👌 문제 이해
가로,세로 크기가 100인 정사각형 모양의 흰색 도화지가 있다. 도화지에서 벗어나지 않게 색종이를 붙이려고 할때, 첫째줄에 색종이 수가 주어지고 둘째줄부터 한줄에 하나씩 색종이를 붙인 위치가 주어진다. 이때 색종이가 붙은 영역의 넓이를 출력

### 💡 문제 해결 방법<br>
**알고리즘**: 구현<br>
**이유** : 

### 💻 코드
* 다른 사람 풀이
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int total = 0;
        int n = Integer.parseInt(br.readLine()); // 색종이 개수
        boolean[][] arr= new boolean[101][101]; // 도화지

        for(int i =0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            for(int j = a; j<a+10; j++){
                for(int k = b; k< b+10; k++){
                    if(!arr[j][k]){
                        arr[j][k]=true;
                        total++;
                    }
                }
            }
        }
        System.out.println(total);


    }
}
```

### 🤔 틀린 이유와 해결책<br>
이 문제를 봤을 때 어떻게 풀지 생각이 바로 떠오르지 않았다. 푸는 방법은 색종이 가로 1, 세로 1일때는 넓이가 1이므로 색종이의 길이는 최대 10까지 이므로 가로 10 세로 10 만큼 탐색하면서 색종이가 붙어 있는 면적이면 total 결과값에서 1씩 더한다.
