# 이진탐색은 정렬이 필수
# set 함수를 통해 중복 제거 - 내장 함수를 이용한 문제풀이
import sys

def exist(lista,listm):
    set(lista)
    for i in listm:
        if i in lista:
            print(1)
        else:
            print(0)
        
    


#s=open("input.txt","rt")
n=int(sys.stdin.readline())
lista= set(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
listm = list(map(int,sys.stdin.readline().split()))
exist(lista,listm)

# 이진탐색을 이용한 수찾기 - 재귀를 이용한 이진탐색
def binary_search(lista,target,start,end):
    if start > end:
        return 0
    mid = (start+end)//2
    if target==lista[mid]: #target을 lista[mid]와 비교 lista[mid]==target은 lista[mid]를 target에 비교하는 것이므로 오류
        return 1
    elif target > lista[mid]:
        return binary_search(lista,target,mid+1,end)
    else:
        return binary_search(lista,target,start,mid-1)


s=open("input.txt","rt")
n=int(s.readline())
lista= sorted(list(map(int,s.readline().split())))
m=int(s.readline())
listm = list(map(int,s.readline().split()))
for i in listm:
    print(binary_search(lista,i,0,n-1))
