import sys

def distance(list1):
    start=0
    end=n-1
    target = abs(list1[start]+list1[end])
    target_left=start
    target_right=end
    while start<end:
        if abs(list1[start]+list1[end])<target:
            target_left= start
            target_right=end
            target=abs(list1[start]+list1[end])
        if list1[start]+list1[end]<0:
            start+=1
        else:
            end-=1
    print(f'{list1[target_left]} {list1[target_right]}')
            
            
            
#s=open("input.txt","rt")
n=int(sys.stdin.readline())
list1=sorted(list(map(int,sys.stdin.readline().split())))
distance(list1)