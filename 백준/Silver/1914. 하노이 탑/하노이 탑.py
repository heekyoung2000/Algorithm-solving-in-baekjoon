import sys
def hanoi(n,x,y):
    if n>1:
        hanoi(n-1,x,6-x-y)
    print(f'{x} {y}')
    if n>1:
        hanoi(n-1,6-x-y,y)
    
n=int(sys.stdin.readline())
print(2**n-1)  
if n<=20:
    hanoi(n,1,3)
