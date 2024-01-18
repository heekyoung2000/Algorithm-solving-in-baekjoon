from sys import stdin
input = stdin.readline
# 인출하는 시간이 짧은 순으로 배열을 정렬하고 누적합 구하기

N =int(input())
time = list(map(int,input().split()))

time.sort()
#[1,2,3,3,4]
#[1,3,6,9,13]
for i in range(N-1):
    time[i+1]+=time[i]
print(sum(time))