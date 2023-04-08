n=int(input())

if n<100:
    print(n)
else:
    cnt=99
    for i in range(99,n+1):
        a=i//100
        b=i%100//10
        c=i%10
        first = b-a
        second = c-b
        if first==second:
            cnt+=1
        else:
            continue
    print(cnt)   