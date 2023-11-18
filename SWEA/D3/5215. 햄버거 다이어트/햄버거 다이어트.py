T=int(input())

def dfs(i,count,cal_sum):
    global maxcount

    if cal_sum>L:
        return
    if maxcount<count:
        maxcount=count
    if i==N:
        return
    
    
    
    dfs(i+1,count+s[i],cal_sum+c[i])#선택하는 경우
    dfs(i+1,count,cal_sum)#선택하지 않는 경우
    
    
   
for test_case in range(1,T+1):
    result=[]
    N,L = map(int,input().split())
    s=[]
    c=[]
    for j in range(N):
        T,K = map(int,input().split())
        s.append(T)
        c.append(K)
    maxcount=0
    dfs(0,0,0)
    print(f'#{test_case} {maxcount}')