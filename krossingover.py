import geomety_test as gt
import numpy as np
import copy
from matplotlib import pyplot as plt

N = 15
x = np.random.randint(0, 2, (N,N))
x1 = gt.smooth(x)
y, count = gt.parts(x1)
x = np.random.randint(0, 2, (N,N))
x1 = gt.smooth(x)
y_1, count_1 = gt.parts(x1)
rad_ground = N / 2
count_matrix = []
count_matrix_1 = []
zero = np.zeros_like(y)
mutation_flag = True
mutation_flag1 = True
for i in range(0, N):
    for j in range(0, N):
        if np.power(j * 2 * rad_ground / N - rad_ground, 2) + np.power(i * 2 * rad_ground / N - rad_ground,
                                                                       2) < np.power(rad_ground, 2) and \
                np.power((j + 1) * 2 * rad_ground / N - rad_ground, 2) + np.power(
            (i + 1) * 2 * rad_ground / N - rad_ground, 2) < np.power(rad_ground, 2) and \
                np.power(j * 2 * rad_ground / N - rad_ground, 2) + np.power((i + 1) * 2 * rad_ground / N - rad_ground,
                                                                            2) < np.power(rad_ground, 2) and \
                np.power((j + 1) * 2 * rad_ground / N - rad_ground, 2) + np.power(i * 2 * rad_ground / N - rad_ground,
                                                                                  2) < np.power(rad_ground, 2): \
                mutation_flag = True
        else:

            y[i, j] = 0
for i in range(0, N):
    for j in range(0, N):
        if np.power(j * 2 * rad_ground / N - rad_ground, 2) + np.power(i * 2 * rad_ground / N - rad_ground,
                                                                       2) < np.power(rad_ground, 2) and \
                np.power((j + 1) * 2 * rad_ground / N - rad_ground, 2) + np.power(
            (i + 1) * 2 * rad_ground / N - rad_ground, 2) < np.power(rad_ground, 2) and \
                np.power(j * 2 * rad_ground / N - rad_ground, 2) + np.power((i + 1) * 2 * rad_ground / N - rad_ground,
                                                                            2) < np.power(rad_ground, 2) and \
                np.power((j + 1) * 2 * rad_ground / N - rad_ground, 2) + np.power(i * 2 * rad_ground / N - rad_ground,
                                                                                  2) < np.power(rad_ground, 2): \
                mutation_flag = True
        else:

            y_1[i, j] = 0
y, count = gt.parts(y)
y_1, count_1 = gt.parts(y_1)

count_min = min(count, count_1)
# kross_number = np.random.randint(1, count_min + 1)
kross_number = 1







def krossingover(y,y_1):
    mutation_flag = True
    mutation_flag1 = True
    count_min = min(count, count_1)
    # kross_number = np.random.randint(1, count_min + 1)
    kross_number = 1
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
    for k in range(1, count + 1):
        for i in range(0, N):
            for j in range(0, N):
                if y[i, j] == k:
                    count_matrix[k-1].append([i, j])
    for i in range(count_1):
        count_matrix_1.append([])
    for k in range(1, count_1 + 1):
        for i in range(0, N):
            for j in range(0, N):
                if y_1[i, j] == k:
                    count_matrix_1[k-1].append([i, j])
    # y_new = copy.deepcopy(y)
    # y_new1 = copy.deepcopy(y_1)
    count_matrix_new = copy.deepcopy(count_matrix)
    count_matrix_new1= copy.deepcopy(count_matrix_1)
    count_matrix_new[kross_number - 1] = copy.deepcopy(count_matrix_1[kross_number - 1])
    count_matrix_new1[kross_number - 1] = copy.deepcopy(count_matrix[kross_number - 1])
    y_new = np.zeros_like(y)

    y_new1 = np.zeros_like(y)


    '''
    for i in range(0, len(count_matrix[kross_number-1])):
        y_new1[count_matrix[kross_number-1][i][0], count_matrix[kross_number-1][i][1]] = kross_number
        y_new[count_matrix[kross_number - 1][i][0], count_matrix[kross_number - 1][i][1]] = 0
    for i in range(0, len(count_matrix_1[kross_number-1])):
        y_new[count_matrix_1[kross_number-1][i][0], count_matrix_1[kross_number-1][i][1]] = kross_number
        y_new1[count_matrix_1[kross_number - 1][i][0], count_matrix_1[kross_number - 1][i][1]] = 0
    
    for i in range(len(count_matrix_new)):
        for j in range(len(count_matrix_new[i])):
            n, k = count_matrix_new[i][j]
            y_new[n, k] = i + 1

    for i in range(len(count_matrix_new1)):
        for j in range(len(count_matrix_new1[i])):
            n, k = count_matrix_new1[i][j]
            y_new1[n, k] = i + 1
    '''
    zero_matrix = np.zeros_like(y)
    zero_matrix, count_new = gt.parts(y_new)
    zero_matrix1 = np.zeros_like(y)
    zero_matrix1, count_new1 = gt.parts(y_new1)
    if count_new == count:
        mutation_flag
    else:
        mutation_flag = False
    if count_new1 == count_1:
        mutation_flag1
    else:
        mutation_flag1 = False

    count_matrix_new_copy = copy.deepcopy(count_matrix_new)
    if mutation_flag == False:

                    for i in range(len(count_matrix_new[kross_number - 1])):
                        del_flag = False
                        for j in range(len(count_matrix_new)):
                            if j != kross_number - 1:
                                for k in range(len(count_matrix_new[j])):
                                    r1 = np.array(count_matrix_new[kross_number - 1][i])
                                    r2 = np.array(count_matrix_new[j][k])
                                    if (np.abs(r1 - r2)).max() <= 1:
                                        # print(count_matrix_new_copy[kross_number - 1])
                                        # print(count_matrix_new[kross_number - 1][i])
                                        count_matrix_new_copy[kross_number - 1].remove(count_matrix_new[kross_number - 1][i])
                                        del_flag = True
                                        break
                            if del_flag:
                                break
    count_matrix_new_copy1 = copy.deepcopy(count_matrix_new1)
    if mutation_flag1 == False:
        for i in range(len(count_matrix_new1[kross_number - 1])):
            del_flag = False
            for j in range(len(count_matrix_new1)):
                if j != kross_number - 1:
                    for k in range(len(count_matrix_new1[j])):
                        r1 = np.array(count_matrix_new1[kross_number - 1][i])
                        r2 = np.array(count_matrix_new1[j][k])
                        if (np.abs(r1 - r2)).max() <= 1:
                            # print(count_matrix_new_copy1[kross_number - 1])
                            # print(count_matrix_new1[kross_number - 1][i])
                            count_matrix_new_copy1[kross_number - 1].remove(count_matrix_new1[kross_number - 1][i])
                            del_flag = True
                            break
                if del_flag:
                    break
    for i in range(len(count_matrix_new_copy)):
        for j in range(len(count_matrix_new_copy[i])):
            n, k = count_matrix_new_copy[i][j]
            y_new[n, k] = i + 1

    for i in range(len(count_matrix_new_copy1)):
        for j in range(len(count_matrix_new_copy1[i])):
            n, k = count_matrix_new_copy1[i][j]
            y_new1[n, k] = i + 1
    
    # return(y_new, y_new1)
    return(y, y_new, count_matrix, count, y_1, y_new1, count_matrix_1, count_1, mutation_flag, mutation_flag1, count_new, count_new1)

y, y_new, count_matrix, count, y_1, y_new1, count_matrix_1, count_1, mutation_flag, mutation_flag1, count_new, count_new1 = krossingover(y, y_1)
'''
plt.imshow(y)
plt.show()
plt.imshow(y_1)
plt.show()
plt.imshow(y_new)
plt.show()
plt.imshow(y_new1)
plt.show()
'''
ang = np.linspace(0, 2*np.pi)
xs = np.cos(ang) * rad_ground + rad_ground - rad_ground / N
ys = np.sin(ang) * rad_ground + rad_ground - rad_ground / N
fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(y)
axs[1, 0].imshow(y_1)
axs[0, 1].imshow(y_new)
axs[1, 1].imshow(y_new1)
axs[0, 0].plot(xs, ys)
axs[1, 0].plot(xs, ys)
axs[0, 1].plot(xs, ys)
axs[1, 1].plot(xs, ys)
plt.show()
# print(krossingover(y, y_1))
print(mutation_flag)
print(mutation_flag1)
print(count, count_1, count_new, count_new1)