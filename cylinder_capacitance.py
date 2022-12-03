import matplotlib.pyplot as plt
import numpy as np
import main_comsol as mc
N = 100  # размерность матрицы
r1 = 0.5  # радиус первого круга
d1 = 0.1  # толщина первого круга
r2 = 4.5  # радиус второго круга
d2 = 0.1  # # толщина второго круга
a = 10  # сторона квадрата
k = a/N  # цена деления
matrix = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        x = j*k+k/2
        y = i*k+k/2
        if (np.power(x-a/2, 2) + np.power(y-a/2, 2) >= np.power(r1, 2)) and (np.power(x-a/2, 2) + np.power(y-a/2, 2) <= np.power(r1+d1, 2)):
            matrix[i][j] = 1

        if (np.power(x-a/2, 2) + np.power(y-a/2, 2) >= np.power(r2, 2)) and (np.power(x-a/2, 2)+ np.power(y-a/2, 2) <= np.power(r2+d2, 2)):
            matrix[i][j] = 2
vector = mc.capacitance(matrix, 3*a)
print(vector)
plt.imshow(matrix)
plt.colorbar()
plt.show()