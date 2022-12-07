import numpy as np
import copy

def intersections(count_matrix_new, number):
        count_matrix_new_copy = copy.deepcopy(count_matrix_new)

        for i in range(len(count_matrix_new[number - 1])):
            del_flag = False
            for j in range(len(count_matrix_new)):
                if j != number - 1:
                    for k in range(len(count_matrix_new[j])):
                        r1 = np.array(count_matrix_new[number - 1][i])
                        r2 = np.array(count_matrix_new[j][k])
                        if (np.abs(r1 - r2)).max() <= 1:
                            count_matrix_new_copy[number - 1].remove(count_matrix_new[number - 1][i])
                            del_flag = True
                            break
                if del_flag:
                    break

        return count_matrix_new_copy