import sys
num=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

if num!=1:
    print(min(arr)*max(arr))
else:
    print(arr[0]**2)