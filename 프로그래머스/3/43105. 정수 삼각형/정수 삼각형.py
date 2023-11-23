def solution(triangle):
    visited = [[0]*a for a in range(1,len(triangle)+1)]
    answer=0
    m = len(triangle)
    for i in range(1,m):
        for j in range(i+1):
            if j==0: #왼쪽 계산
                triangle[i][j] += triangle[i-1][j]
            elif j==i: #오른쪽 계산
                triangle[i][j]+= triangle[i-1][j-1]
            else: #가운데 계산
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
                
    return max(triangle[-1])