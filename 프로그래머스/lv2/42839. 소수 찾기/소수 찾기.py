from itertools import permutations


def solution(numbers):
    new_numbers = [i for i in numbers]
    per_list=[]
    int_list=[]
    result=[]
    for i in range(1,len(new_numbers)+1):
        per_list+=list(permutations(new_numbers,i))
        int_list = [int(("").join(p)) for p in per_list]
    print(int_list)
    for num in int_list:
        if num<2:
            continue
        check=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                check=False
                break
        if check:
            result.append(num)
    return len(set(result))
