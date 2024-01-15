import sys
from collections import deque
#어디가 종료지점인가?- 로봇이 내리는 지점? 아니면 내구도가 0인 칸의 개수가 개 이상이 될 때?

#1 2 3
#6 5 4



N,K = map(int,sys.stdin.readline().split())
queue= deque()
con_list = list(map(int,sys.stdin.readline().split()))
robot_list = deque([False] * (N))
for i in range(1,2*N+1):
    queue.append([i,con_list[i-1]])
result=0

while True:
    result+=1
    #1단계 수행-벨트 회전
    queue.appendleft(queue.pop())#벨트 회전
    robot_list.rotate(1) #로봇회전
    robot_list[-1]=False #내리는 위치에 로봇이 있으면 내림
    #2단계 수행- 로봇 한칸 이동 이때 이동하려는 칸에 로봇 없고, 내구도 1이상
    for i in range(N-2,-1,-1):
        if robot_list[i]==True and robot_list[i+1]==False and queue[i+1][1]>0:
            robot_list[i]=False
            robot_list[i+1]=True
            queue[i+1][1]-=1
    robot_list[-1]=False
    #3단계 수행 - 올리는 위치의 내구도 0이상
    #이때 올리는 위치가 아래로 내려가있으면 안되므로 2*N이 아닌 N
    if robot_list[0]==False and queue[0][1]>0:
        robot_list[0]=True
        queue[0][1]-=1
    #4단계 수행- 내구도가 0인 칸의 개수가 K개 이상이면 종료
    count=0
    for j in range(N*2):
        if queue[j][1]==0:
            count+=1
    if count>=K:
        break
print(result)