T=int(input())

def dfs(i,result):
    global count
    if i==N:
        if result==K:
            count+=1
        return
    if result==K:
        count+=1
        return
    if result>K:
        return
    dfs(i+1,result+A[i])#선택하는 조건
    dfs(i+1, result) #선택하지 않는 조건
    
for test_case in range(1,T+1):
    N,K=map(int,input().split())
    A = list(map(int,input().split()))
    count=0
    dfs(0,0)
    print(f'#{test_case} {count}')