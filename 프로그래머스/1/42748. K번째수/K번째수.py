def solution(array, commands):
    return list(sorted(array[x[0]-1:x[1]])[x[2]-1] for x in commands)