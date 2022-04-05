def solution(m, n, puddles):
    _max = max(m,n)+1
    matrix = [[0 for j in range(_max)] for i in range(_max)]
    matrix[1][1] = 1

    for j in range(1,n+1):
        for i in range(1,m+1):
            if [i,j] not in puddles:
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1]
            # for s in matrix:
            #     print(s)
            # print()

    return matrix[m][j]%1000000007

print(solution(4,3,[[2, 2]]))

