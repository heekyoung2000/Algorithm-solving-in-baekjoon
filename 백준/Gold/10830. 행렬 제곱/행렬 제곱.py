import sys

n,b=map(int,sys.stdin.readline().split())
list1=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def mul(U,list2):
    n=len(U)
    answer = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            result=0
            for i in range(n):
                result+= U[row][i]*list2[i][col]
            answer[row][col]=result%1000
    return answer

def pow(list1,b):
    if b==1:
        for x in range(len(list1)):
            for y in range(len(list1)):
                list1[x][y]%=1000
        return list1
    

    tmp = pow(list1,b//2)
    if b%2!=0:
        return mul(mul(tmp,tmp),list1)
    else:
        return mul(tmp,tmp)
    
    
for i in pow(list1,b):
    print(*i)