import sys

result =[]

def cut(x,y,n):
    color = new_list[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!= new_list[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return 
    if color==0:
        result.append(0)
    else:
        result.append(1)

new_list=[]
n=int(sys.stdin.readline())
for i in range(n):
    list1 = list(map(int,sys.stdin.readline().split()))
    new_list.append(list1)
cut(0,0,n)
print(result.count(0))
print(result.count(1))