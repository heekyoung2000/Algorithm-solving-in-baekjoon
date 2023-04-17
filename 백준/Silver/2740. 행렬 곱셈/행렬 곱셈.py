import sys

n,m = map(int,sys.stdin.readline().split())
list1 = [list(map(int,sys.stdin.readline().split()))for _ in range(n)]

m,k = map(int,sys.stdin.readline().split())
list2 = [list(map(int,sys.stdin.readline().split()))for _ in range(m)]


def mul(list1,list2):
    answer = [[0]*k for _ in range(n)]
    for row in range(n):
        for col in range(k):
            result=0
            for i in range(m):
                result+= list1[row][i] * list2[i][col]
            answer[row][col]=result
    return answer



for a in mul(list1,list2):
    print(*a)
        