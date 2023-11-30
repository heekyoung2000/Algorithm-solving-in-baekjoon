import sys
N = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
request.sort()

def r(start,end):
    while start<=end:
        s=0
        mid=(start+end)//2
        for req in request:
            if req<=mid:
                s+=req
            else:
                s+=mid
        
        if s==M:
            break
        elif s<M:
            start = mid+1
            new_result=mid
        else:
            end = mid-1
    
    if s>M:
        print(new_result)
    else:
        print(mid)
        
    
start=0
end = request[-1]
r(start,end)