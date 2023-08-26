from sys import stdin as s
N=int(s.readline())
result= 0 
for i in range(1,N+1):
    num_list = list(map(int,str(i)))
    result = sum(num_list)+i
    if result == N:
        print(i)
        break
    if i==N:
        print(0)