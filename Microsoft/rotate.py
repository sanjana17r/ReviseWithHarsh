def rotate(matrix): 
    #code here
    matrix.reverse()
    n = len(matrix)-1
    for i in range(len(matrix)):
        for j in range(len(matrix)-i):
            k = matrix[n-j][n-i]
            matrix[n-j][n-i] = matrix[i][j]
            matrix[i][j] = k
