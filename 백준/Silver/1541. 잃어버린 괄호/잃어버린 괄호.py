from sys import stdin as s

arr = input().split('-') #입력받은 문자열을 -로 나누기
s=0
for i in arr[0].split('+'): #처음에 분리한 문자열을 계산
    s+=int(i)
for i in arr[1:]: #분배법칙을 활용한 것으로 뒤에 있는 나머지 값들은 모두 - 해줌
    for j in i.split('+'):
        s-=int(j)

print(s)
