import sys
input = sys.stdin.readline

A = int(input())
T = int(input())
S = int(input())

games= []
bun = 1
degi =1
cnt=0

while True:
    num = bun # 이전회차에서 뻔 or 데기를 외친 누적 횟수
    cnt+=1 #회차
    
    for _ in range(2):
    # 처음 뻔-데기 뻔-데기 4번 반복
        games.append((bun,0))
        bun+=1
        games.append((degi,1))
        degi+=1
        
    # 삔-삔 반복부분
    for _ in range(cnt+1):
        games.append((bun,0))
        bun+=1
        
    for _ in range(cnt+1):
        games.append((degi,1))
        degi+=1
        
    if num<=T<bun:
        print(games.index((T,S))%A)
        break
   