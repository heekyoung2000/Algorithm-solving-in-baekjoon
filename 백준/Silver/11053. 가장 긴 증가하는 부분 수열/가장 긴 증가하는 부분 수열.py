import sys

#s=open("input.txt",'rt')


def dp(list1,n):
    result=[1]*n
    for i in range(0,n):
        for j in range(0,i):
            if list1[i]>list1[j]:
                result[i] = max(result[i],result[j]+1)
    #print(result)
    print(max(result))

n=int(sys.stdin.readline())
list1=list(map(int,sys.stdin.readline().split()))
dp(list1,n)