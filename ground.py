import geomety_test as gt
import numpy as np

def ground_test(y, rad_ground, N):
    for i in range(0, N):
        for j in range(0, N):
            if np.power(j * 2 * rad_ground / N - rad_ground, 2) + np.power(i * 2 * rad_ground / N - rad_ground,
                                                                           2) < np.power(rad_ground, 2) and \
                    np.power((j + 1) * 2 * rad_ground / N - rad_ground, 2) + np.power(
                (i + 1) * 2 * rad_ground / N - rad_ground, 2) < np.power(rad_ground, 2) and \
                    np.power(j * 2 * rad_ground / N - rad_ground, 2) + np.power(
                (i + 1) * 2 * rad_ground / N - rad_ground,
                2) < np.power(rad_ground, 2) and \
                    np.power((j + 1) * 2 * rad_ground / N - rad_ground, 2) + np.power(
                i * 2 * rad_ground / N - rad_ground,
                2) < np.power(rad_ground, 2): \
                    mutation_flag = True
            else:

                y[i, j] = 0
    return y