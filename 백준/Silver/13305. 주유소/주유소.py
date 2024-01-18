from sys import stdin
input = stdin.readline

N = int(input())
city = list(map(int,input().split()))
price = list(map(int,input().split()))

# price 리스트에서 현재 위치가격 보다 다음 가격이 더 비싸면
# 현재 위치에서 city 가격 더하기

# 현재 위치 가격에서 다음 위치 가격중 작은 값이 있는 곳까지 탐색
start=0
move =0
result=0
while True:
    if price[start] > price[move]:
        start=move
    if move==N-1:
        break
    result+=price[start]*city[move]
    move+=1
print(result)