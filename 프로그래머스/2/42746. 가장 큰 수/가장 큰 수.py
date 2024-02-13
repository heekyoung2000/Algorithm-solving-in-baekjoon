def solution(numbers):
    new_arr=list(str(n) for n in numbers)
    new_arr.sort(key=lambda x:x*3,reverse=True)
    return str(int("".join(new_arr)))