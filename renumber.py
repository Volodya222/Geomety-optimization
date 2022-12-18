import numpy as np
import copy
import geomety_test as gt

N = 5
x = np.random.randint(0, 2, (N,N))
x1 = gt.smooth(x)
y, count = gt.parts(x1)
# y_1 = [[1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3], [4,4,4,4,4], [5,5,5,5,5]]

# y_2 = np.array(y_1)
# print(y_2)


def renumber(y, N):

    a, count = gt.parts(y)
    count_matrix = []
    for i in range(count):
        count_matrix.append([])
    for k in range(1, count + 1):
        for i in range(0, N):
            for j in range(0, N):
                if y[i, j] == k:
                    count_matrix[k-1].append([i, j])
    print(count_matrix)
    flag_number = y[(N-1) // 2, (N-1) // 2]
    if (flag_number != 0) and (flag_number != 1):
        count_matrix[0], count_matrix[flag_number - 1] = count_matrix[flag_number - 1], count_matrix[0]
    for i in range(len(count_matrix)):
        for j in range(len(count_matrix[i])):
            n, k = count_matrix[i][j]
            y[n, k] = i + 1
    return y


