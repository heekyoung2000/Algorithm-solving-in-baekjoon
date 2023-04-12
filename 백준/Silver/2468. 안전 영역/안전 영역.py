import sys
sys.setrecursionlimit(100000)

n=int(sys.stdin.readline())
new_list=[]
direct=[[-1,0],[0,1],[1,0],[0,-1]] #앞,뒤,위,아래

for i in range(n):
    list1 = list(map(int,sys.stdin.readline().split()))
    new_list.append(list1)            

def check(i,j,z): #앞,뒤,오른쪽,왼쪽이 잠기는지 확인 안잠길 경우 옆(뒤로)으로 이동, 잠길 경우 break #z는 높이
    global cnt
    for k in range(4):
        next_i = i + direct[k][0]
        next_j = j + direct[k][1]
        
        if(0<=next_i<n) and (0<=next_j<n) and not water_table[next_i][next_j] and new_list[next_i][next_j] > z:
            water_table[next_i][next_j]=True
            check(next_i,next_j,z)
        

ans = 1
for z in range(max(map(max,new_list))):
    water_table = [[False]*n for _ in range(n)]
    cnt=0
    for i in range(0,n):
        for j in range(0,n):
            if new_list[i][j]>z and not water_table[i][j]:
                cnt+=1
                water_table[i][j]=True
                check(i,j,z)
    ans = max(ans,cnt)

print(ans)