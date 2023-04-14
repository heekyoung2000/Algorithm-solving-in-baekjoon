import sys

def result(list1):
    cnt=1
    m=list1[-1]
    for i in range(n-1,0,-1):
        if m<list1[i-1]:
            m=list1[i-1]
            cnt+=1
    return cnt
    

#s=open('input.txt','rt')
n = int(sys.stdin.readline())
list1=[]
for i in range(n):
    num=int(sys.stdin.readline())
    list1.append(num)


print(result(list1))
