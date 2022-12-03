import geomety_test as gt
import numpy as np
import copy
from matplotlib import pyplot as plt

N = 5
x = np.random.randint(0, 2, (N,N))
x1 = gt.smooth(x)
y, count = gt.parts(x1)
rad_ground = (N-1)/2
movement_list = []
count_matrix = []

def movement(y, movement_list):
    '''
    for i in range(0, N):
        y[0, i] = 0
        y[i, 0] = 0
        y[N-1, i] = 0
        y[i, N-1] = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if np.power(i - rad_ground, 2) + np.power(j - rad_ground, 2) >= np.power(rad_ground, 2):
                y[i, j] = 0
    '''
    for i in range(count):
        count_matrix.append([])
    for k in range(count + 1):
        for i in range(0, N+1):
            for j in range(0, N+1):
                if y[i, j] == k:
                    count_matrix[k-1].append([i, j])


    return(y, count_matrix, count)

print(movement(y,movement_list))