from sys import stdin
input= stdin.readline
# 각 거리 차를 구한 리스트를 구하고 k-1개 만큼 반복하면서 가장 큰값을 빼주고 나머지 리스트의 합을 구해주면 돰!

N = int(input())
K= int(input())
sensor = list(map(int,input().split()))
sensor.sort()

dif = []
if N<=K:
    print(0)
else:
    for i in range(N-1):
        dif.append(sensor[i+1]-sensor[i])
    dif.sort()
    for _ in range(K-1):
        dif.pop()
    print(sum(dif))
    