import sys
n,m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    card = sorted(card)
    num1 = card[0]+card[1]
    card[0],card[1]=num1,num1
    
print(sum(card))