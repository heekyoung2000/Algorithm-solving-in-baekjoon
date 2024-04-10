import sys
input = sys.stdin.readline

N = int(input())

i=0
result=0
result_list=[]
while i<N-1:
    i+=1
    result=N*i+i
    result_list.append(result)
print(sum(result_list))