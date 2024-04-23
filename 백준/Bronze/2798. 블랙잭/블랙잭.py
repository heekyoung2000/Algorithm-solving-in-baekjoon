import sys

input = sys.stdin.readline

N,M = map(int,input().split())
card = list(map(int,input().split()))

result=0
for i in range(N):
    for j in range(i+1,N):
        for z in range(j+1,N):
            if card[i]+card[j]+card[z]<=M:
                result=max(result,card[i]+card[j]+card[z])

print(result)