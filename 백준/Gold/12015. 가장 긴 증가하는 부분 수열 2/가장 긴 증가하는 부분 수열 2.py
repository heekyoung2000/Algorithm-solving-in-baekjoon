from sys import stdin as s
#이분탐색 해야함

#s=open("input.txt","rt")

n=int(s.readline())
array_list=list(map(int,s.readline().split()))

LIS = [array_list[0]]

def findPlace(num):
    start =0 
    end = len(LIS)-1
    
    while start<=end:
        mid=(start+end)//2
        if LIS[mid]==num:
            return mid
        elif LIS[mid]<num:
            start=mid+1
        else:
            end=mid-1
    return start
        
for i in array_list:
    if LIS[-1]<i:
        LIS.append(i)
    else:
        idx= findPlace(i)
        LIS[idx]=i
print(len(LIS))
