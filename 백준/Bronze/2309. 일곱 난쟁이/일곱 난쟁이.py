import sys
input =sys.stdin.readline

def dfs(height):
    if sum(height)==100:
        print(*height)
        return
    # elif sum(height)>100:
        

height = []
dp = []
for _ in range(9):
    n = int(input())
    height.append(n)

height.sort()
def dfs(depth,start):
    if depth==7:
        if sum(dp)==100:
            print(* dp,sep="\n")
            exit()
        else:
            return
    for i in range(start,len(height)):
        dp.append(height[i])
        dfs(depth+1,i+1)
        dp.pop()

dfs(0,0)