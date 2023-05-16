#no: 원반의 갯수, x: 처음 시작하는 고리, y: 목표하는 고리
def move(no, x,y):
    if no>1:
        move(no-1,x,6-x-y)
    print(f'{x} {y}')
    if no>1:
        move(no-1,6-x-y,y)
    
no = int(input())
print(2**no-1) #원반의 총 개수
if no<=20:
    move(no,1,3)