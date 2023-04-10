def move(no, x,y):
    if no>1:
        move(no-1,x,6-x-y)
    print(f'{x} {y}')
    if no>1:
        move(no-1,6-x-y,y)
    
no = int(input())
print(2**no-1)
if no<=20:
    move(no,1,3)