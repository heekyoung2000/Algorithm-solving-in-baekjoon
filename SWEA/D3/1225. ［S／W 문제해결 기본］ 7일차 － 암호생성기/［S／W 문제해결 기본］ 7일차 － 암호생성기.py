T=10

for i in range(1,T+1):
    test_case = int(input())
    num_list = list(map(int,input().split()))
    while num_list[-1]!=0:
        for i in range(1,6):
            new_number = num_list[0]-i
            if new_number<=0:
                new_number=0
            num_list.remove(num_list[0])
            num_list.append(new_number)
            if num_list[-1]==0:
                break  
    print(f'#{test_case}',end=" ")
    for num in num_list:
        print(num,end=" ")
    print()