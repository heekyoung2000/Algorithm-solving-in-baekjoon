from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")
n=int(s.readline())

# 메모리 공간 생성
#1.타일 n개로 만들수 있는 이진 수열을 구함
# 1-1. 이때 0이 홀수 개 이거나 00이 연속되지 않았을 경우 리스트에 저장하지 않고 continue count도 하지 않음
# 1-2. 리스트에 개수를 구하고 15746d으로 나눈 나머지를 출력함
d=[0]*(1000001)

d[1]=1
d[2]=2
for i in range(3,n+1):
    d[i]=(d[i-1]+d[i-2])%15746
    
    
print(d[n])