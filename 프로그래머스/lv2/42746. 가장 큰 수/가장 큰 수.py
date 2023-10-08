def solution(numbers):
    answer = 0
    numbers.sort(key = lambda x : str(x)*3, reverse = True)
    answer = str(int(''.join(map(str,numbers))))
    return answer 