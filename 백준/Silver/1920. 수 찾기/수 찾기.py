# 이진탐색은 정렬이 필수
# 각 배열을 
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
