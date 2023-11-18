T=int(input())


for test_case in range(1,T+1):
    result=0
    N=int(input())
    board = [list(map(int,input())) for _ in range(N)]
    count=0
    #중간까지 합
    for i in range(N//2+1):
        count+=board[i][N//2]
        for j in range(1,i+1):
            count+=board[i][N//2+j]+board[i][N//2-j]
    # 나머지 합
    for i in range(N//2+1,N):
        count+=board[i][N//2]
        if i==N-1:
            break
        for j in range(N-1-i,0,-1):
            count+=board[i][N//2+j]+board[i][N//2-j]
    print(f'#{test_case} {count}')