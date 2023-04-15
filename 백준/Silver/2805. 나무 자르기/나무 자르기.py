import sys

def binary_search(list,start,end,m):
    while start<=end:
        result=0
        mid=(start+end)//2
        for i in list:
            if i>mid:
                result+=(i-mid)
            else:
                result+=0
            if result>m:
                break
        if result<m:
            end=mid-1
        elif result>=m:
            start=mid+1
            

    print(end)
        

#s=open("input.txt","rt")
n,m=map(int,sys.stdin.readline().split())
height_list=sorted(list(map(int,sys.stdin.readline().split())))
binary_search(height_list,0,max(height_list),m)