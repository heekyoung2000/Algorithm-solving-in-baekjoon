x=int(input())
if x>99:
    cnt=99
    for i in range(100,x+1):
        a=i//100
        b=i%100//10
        c=i%10
        if (b-a)==(c-b):
            cnt+=1
else:
    cnt=x
print(cnt)