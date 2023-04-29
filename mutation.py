import geomety_test as gt
import numpy as np
import copy
from matplotlib import pyplot as plt
import ground
import  fix_det as fd


N = 15
x = np.random.randint(0, 2, (N,N))
x1 = gt.smooth(x)
y, count = gt.parts(x1)
rad_ground = N / 2
ground_flag = False
y = ground.ground_test(y, rad_ground, N)
y, count = gt.parts(y)




def mutation(y, N):
    rad_ground = N / 2
    a, count = gt.parts(y)
    count_matrix = []
    mutation_number = np.random.randint(1, count+1)
    mutation_flag = True
    # mutation_number = 1
    number_list = []
    neighbors_list = []

    '''
    for i in range(0, N):
        y[0, i] = 0
        y[i, 0] = 0
        y[N-1, i] = 0
        y[i, N-1] = 0
    '''

    for i in range(1, N-1):
        for j in range(1, N-1):
            if y[i, j] == mutation_number:
                if y[i + 1, j] == 0 or y[i, j+1] == 0 or y[i-1, j] == 0 or y[i, j-1] == 0:
                    number_list.append([i, j])
                if y[i+1, j] == 0:
                    neighbors_list.append([i+1, j])
                if y[i-1, j] == 0:
                    neighbors_list.append([i-1, j])
                if y[i, j+1] == 0:
                    neighbors_list.append([i, j+1])
                if y[i, j-1] == 0:
                    neighbors_list.append([i, j-1])
    pixels_fate = np.random.randint(0, 2)
    # pixels_fate = 0
    positions_for_delete = []
    k = 0
    y_1 = copy.copy(y)
    if pixels_fate == 0:
        flag = np.ones(len(number_list))
        if len(number_list) >= 1:
            if len(number_list) == 1:
                number_list[0] = 0
            else:
                del_numbers = np.random.randint(1, len(number_list) + 1)
                if del_numbers == len(number_list):
                    positions_for_delete = copy.copy(number_list)
                else:
                    while k < del_numbers:
                        a = np.random.randint(0, len(number_list))
                        t = number_list[a]
                        if flag[a] != 0:
                            positions_for_delete.append(t)
                            flag[a] = 0
                            k += 1
        for i in range(0, len(positions_for_delete)):
             y_1[positions_for_delete[i][0], positions_for_delete[i][1]] = 0
    else:
        flag = np.ones(len(neighbors_list))
        if len(neighbors_list) >= 1:
            if len(neighbors_list) == 1:
                neighbors_list[0] = 0
            else:
                del_numbers = np.random.randint(1, len(neighbors_list) + 1)
                if del_numbers == len(neighbors_list):
                    positions_for_delete = copy.copy(neighbors_list)
                else:
                    while k < del_numbers:
                        a = np.random.randint(0, len(neighbors_list))
                        t = neighbors_list[a]
                        if flag[a] != 0:
                            positions_for_delete.append(t)
                            flag[a] = 0
                            k += 1
        for i in range(0, len(positions_for_delete)):
             y_1[positions_for_delete[i][0], positions_for_delete[i][1]] = mutation_number

    y_1 = ground.ground_test(y_1, rad_ground, N)
    for i in range(count):
        count_matrix.append([])
    for k in range(1, count + 1):
        for i in range(0, N):
            for j in range(0, N):
                if y[i, j] == k:
                    count_matrix[k-1].append([i, j])

    zero_matrix = np.zeros_like(y)
    zero_matrix, count_new = gt.parts(y_1)

    if count_new == count:
        mutation_flag = True
    else:
        mutation_flag = False

    if mutation_flag == True:
        pass
    else:
        count_matrix_new_copy = fd.intersections(count_matrix, mutation_number)
        for i in range(len(count_matrix_new_copy)):
            for j in range(len(count_matrix_new_copy[i])):
                n, k = count_matrix_new_copy[i][j]
                y_1[n, k] = i + 1
    zero_matrix, count_new = gt.parts(y_1)
    if count_new == count:
        mutation_flag = True
    else:
        mutation_flag = False
    if (y == y_1).all():
        mutation_flag = False
    return y, y_1, mutation_flag
# print(mutation(y))

y, y_1, mutation_flag  = mutation(y, N)
'''
print(mutation_flag)
plt.imshow(y)
plt.show()
plt.imshow(y_1)
plt.show()


fig, axs = plt.subplots(1, 2)
axs[0].imshow(y)
axs[1].imshow(y_1)
plt.show()
'''
def weak_mutation(y, N):
    rad_ground = N / 2
    a, count = gt.parts(y)
    count_matrix = []
    mutation_number = np.random.randint(1, count+1)
    mutation_flag = True
    # mutation_number = 1
    number_list = []
    neighbors_list = []

    '''
    for i in range(0, N):
        y[0, i] = 0
        y[i, 0] = 0
        y[N-1, i] = 0
        y[i, N-1] = 0
    '''

    for i in range(1, N-1):
        for j in range(1, N-1):
            if y[i, j] == mutation_number:
                if y[i + 1, j] == 0 or y[i, j+1] == 0 or y[i-1, j] == 0 or y[i, j-1] == 0:
                    number_list.append([i, j])
                if y[i+1, j] == 0:
                    neighbors_list.append([i+1, j])
                if y[i-1, j] == 0:
                    neighbors_list.append([i-1, j])
                if y[i, j+1] == 0:
                    neighbors_list.append([i, j+1])
                if y[i, j-1] == 0:
                    neighbors_list.append([i, j-1])
    pixels_fate = np.random.randint(0, 2)
    # pixels_fate = 0
    positions_for_delete = []
    k = 0
    y_1 = copy.copy(y)
    if pixels_fate == 0:
        flag = np.ones(len(number_list))
        if len(number_list) >= 1:
            if len(number_list) == 1:
                number_list[0] = 0
            else:
                del_numbers = np.random.randint(0, max((len(number_list) + 1) // 4, 1))
                if del_numbers == len(number_list):
                    positions_for_delete = copy.copy(number_list)
                else:
                    while k < del_numbers:
                        a = np.random.randint(0, len(number_list))
                        t = number_list[a]
                        if flag[a] != 0:
                            positions_for_delete.append(t)
                            flag[a] = 0
                            k += 1
        for i in range(0, len(positions_for_delete)):
             y_1[positions_for_delete[i][0], positions_for_delete[i][1]] = 0
    else:
        flag = np.ones(len(neighbors_list))
        if len(neighbors_list) >= 1:
            if len(neighbors_list) == 1:
                neighbors_list[0] = 0
            else:
                del_numbers = np.random.randint(0, max((len(number_list) + 1) // 4, 1))
                if del_numbers == len(neighbors_list):
                    positions_for_delete = copy.copy(neighbors_list)
                else:
                    while k < del_numbers:
                        a = np.random.randint(0, len(neighbors_list))
                        t = neighbors_list[a]
                        if flag[a] != 0:
                            positions_for_delete.append(t)
                            flag[a] = 0
                            k += 1
        for i in range(0, len(positions_for_delete)):
             y_1[positions_for_delete[i][0], positions_for_delete[i][1]] = mutation_number

    y_1 = ground.ground_test(y_1, rad_ground, N)
    for i in range(count):
        count_matrix.append([])
    for k in range(1, count + 1):
        for i in range(0, N):
            for j in range(0, N):
                if y[i, j] == k:
                    count_matrix[k-1].append([i, j])

    zero_matrix = np.zeros_like(y)
    zero_matrix, count_new = gt.parts(y_1)

    if count_new == count:
        mutation_flag = True
    else:
        mutation_flag = False

    if mutation_flag == True:
        pass
    else:
        count_matrix_new_copy = fd.intersections(count_matrix, mutation_number)
        for i in range(len(count_matrix_new_copy)):
            for j in range(len(count_matrix_new_copy[i])):
                n, k = count_matrix_new_copy[i][j]
                y_1[n, k] = i + 1
    zero_matrix, count_new = gt.parts(y_1)
    if count_new == count:
        mutation_flag = True
    else:
        mutation_flag = False
    if (y == y_1).all():
        mutation_flag = False
    return y, y_1, mutation_flag
# print(mutation(y))

y, y_1, mutation_flag  = mutation(y, N)






