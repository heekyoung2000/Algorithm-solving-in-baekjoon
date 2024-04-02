import sys
from collections import deque
input = sys.stdin.readline

#1. 동서남북에 0의 개수 구하고 높이에서 제거하기
#2. 제거한 후 덩어리가 총 몇개인지 확인하기
#2-1. 만약 2개 이상이면 while문을 종료하고 년도 출력하기
#2-2. 2개 미만이면 year 증가 시키고 다시 반복

N,M = map(int,input().split())
#N은 세로 M은 가로
ice = [(list(map(int,input().split()))) for _ in range(N)]

#동서남북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

##1. 동서남북에 0의 개수 구하고 높이에서 제거하기
def find(ice):
    new_ice = [[0]*(M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j]!=0:
                count=0
                for z in range(4):
                    new_i,new_j=i+dx[z],j+dy[z]
                    if ice[new_i][new_j]==0:
                        count+=1
                result=ice[i][j]-count
                if result<0: result=0
                new_ice[i][j]=result
    return new_ice


def check(i,j,visited):
    ice_q=deque()
    ice_q.append([i,j])
    while ice_q:
        di,dj = ice_q.popleft()
        for z in range(4):
            new_i,new_j=di+dx[z],dj+dy[z]
            if  0 <= new_i < N and 0 <= new_j < M and visited[new_i][new_j]==False and ice[new_i][new_j]!=0:
                visited[new_i][new_j]=True
                ice_q.append([new_i,new_j])

    

    
for year in range(1,900000):
    ice = find(ice)
    ## 빙산 덩어리 개수 카운트
    visited=[[False]*(M+1) for _ in range(N)]
    result=0
    for i in range(N):
        for j in range(M):
            if visited[i][j]==0 and ice[i][j]!=0:
                check(i,j,visited)
                result+=1
    if result>=2:
        print(year)
        break
    elif result==0:
        print(0)
        break
