def solution(sizes):
    result=max(max(x) for x in sizes)*max(min(y) for y in sizes)
    return result