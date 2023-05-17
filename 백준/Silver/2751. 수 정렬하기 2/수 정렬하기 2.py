from sys import stdin as s
#이분 탐색으로 진행


#s=open("input.txt","rt")
n=int(s.readline())
num_list=[]
# def binary():
    
for _ in range(n):
    num=int(s.readline())
    num_list.append(num)
num_list.sort()
for j in num_list:
    print(j)