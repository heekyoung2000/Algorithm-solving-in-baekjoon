from sys import stdin as s
import sys
sys.setrecursionlimit(1000000)

def dfs(x,num):
    global ans,new_R,new_G,new_B
    # 종료조건
    if num >=2: # 물감을 섞어야 하므로 최소 2개 이상의 물감 필요
        ans = min(ans,abs(new_R//num-R)+abs(new_B//num-B)+abs(new_G//num-G))
    for i in range(x+1,n):
        new_R,new_G,new_B = new_R+arr[i][0], new_G+arr[i][1], new_B + arr[i][2]
        if num<7:
            dfs(i,num+1)
        new_R,new_G,new_B = new_R-arr[i][0], new_G-arr[i][1],new_B-arr[i][2]
            
    

n=int(s.readline())
arr = [[*map(int,s.readline().split())] for i in range(n)]
R,G,B = map(int,s.readline().split())
new_R,new_G,new_B = 0,0,0
ans = 99999999
dfs(-1,0)
print(ans)