import sys
input = sys.stdin.readline

teris1 = [[[0,1],[0,2],[0,3]],[[1,0],[2,0],[3,0]],
          [[0,1],[1,1],[1,2]],[[1,0],[1,-1],[2,-1]],
          [[0,1],[0,2],[1,2]],[[1,0],[2,0],[2,-1]],[[1,0],[1,1],[1,2]],[[0,1],[1,0],[2,0]],
          [[0,1],[0,2],[1,1]],[[1,0],[2,0],[1,-1]],[[0,1],[0,2],[-1,1]],[[1,0],[1,1],[2,0]],
          [[0,1],[1,1],[1,0]]]


def search(x,y):
    global block
    global N
    result=-(1e9)
    for teris in teris1:
        cnt=block[x][y]
        for t in teris:
            nx,ny=x+t[0],y+t[1]
            if 0<=nx<N and 0<=ny<N:
                cnt+=block[nx][ny]
            else:
                cnt=-(1e9)
        result=max(result,cnt)
    return result


number=1
while 1:
    answer=-(1e9)
    N = int(input())
    if N == 0:
        break
    else:
        block = [list(map(int,input().split())) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                re = search(i,j)
                answer = max(re,answer)
        print(f'{number}. {answer}')
        number+=1
   