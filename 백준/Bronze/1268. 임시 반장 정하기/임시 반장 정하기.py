import sys
input = sys.stdin.readline

N = int(input())
student_list = [list(map(int, input().split())) for _ in range(N)]

m = -1
result = -1

# 각 학생이 같은 반이었던 적이 있는지를 체크하기 위한 리스트
visited = [0] * (N + 1)

for i in range(N):
    visited = [0] * (N + 1)  # visited 리스트 초기화
    for j in range(5):  # 각 학생의 5개의 반 번호에 대해서
        for k in range(N):  # 모든 학생들과 비교
            if k != i and student_list[i][j] == student_list[k][j]:  # 같은 반 번호를 가졌다면
                visited[k] = 1  # 해당 학생의 visited를 1로 설정
    if m < visited.count(1):  # 같은 반이었던 적이 있는 학생의 수를 세고 비교
        m = visited.count(1)
        result = i

print(result + 1)  # 1부터 시작하는 학생 번호로 출력
