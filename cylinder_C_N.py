import matplotlib.pyplot as plt
import numpy as np
import main_comsol as mc
import cylinder_capacitance as cc
params = {'font.family': 'Times New Roman', 'legend.fontsize': 15, 'figure.figsize': (18, 8), 'axes.labelsize': 17,
          'axes.titlesize': 20, 'xtick.labelsize': 17, 'ytick.labelsize': 17, 'figure.titlesize': 20}
plt.rcParams.update(params)

if __name__ == "__main__":
    # массив внешних радиусов
    r2 = np.array([0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.,  3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4, 5.7])
    len_r2 = np.shape(r2[0])
    # массив размеров матриц
    n = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
    len_n = np.shape(n)[0]
    # массив отношений rg/r2
    rgr2 = np.array([11.66666667,  7.77777778, 5.83333333,  4.66666667,  3.88888889,  3.33333333, 2.91666667,  2.59259259,
                    2.33333333,  2.12121212,  1.94444444,  1.79487179, 1.66666667,  1.55555556,  1.45833333,  1.37254902,
                    1.2962963,   1.22807018])
    # массив теоретических значений емкостей c22
    list_c22_theory = np.array([22.63417604,  27.10816809,  31.53013702,  36.09748384,  40.94339772, 46.18558639,
                                51.94697193,  58.36949673,  65.6276766,   73.94561295, 83.62131052,  95.06410703,
                                108.85552208, 125.85348117, 147.38150064, 175.59686289, 214.272798,   270.66352363])


    # N = 80  # размерность матрицы
    r1 = 0.3  # радиус первого круга в метрах
    d1 = 0.09  # толщина первого круга в метрах
    r2 = 5.7      # радиус второго круга в метрах
    d2 = 0.09  # толщина второго круга в метрах
    delta = 0.3  # шаг в метрах
    number_steps = 18  # количество шагов
    a = 13  # сторона квадрата в метрах
    rg = 7  # радиус земли в метрах
    # k = a/N  # цена деления
    g = 2*np.pi*8.85  # константа для подсчета теоретической емкости с учетом \epsilon = 1, результа в pF

    # !!!!!Чтобы код работал корректно, нужно в main_comsol также задать значения радиуса земли и стороны квадрата !!!!!


    # геометрия цилиндрического конденатораб центры окружностей: (a/2 , -a/2)
    def create_circles(radius_2, N):
        k = a/N
        matrix = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                x = j*k+k/2
                y = i*k+k/2
                if np.power(x-a/2, 2) + np.power(y-a/2, 2) <= np.power(r1+d1, 2):
                    matrix[i][j] = 1

                if (np.power(x-a/2, 2) + np.power(y-a/2, 2) >= np.power(radius_2, 2)) and (np.power(x-a/2, 2) + np.power(y-a/2, 2) <= np.power(radius_2+d2, 2)):
                    matrix[i][j] = 2
        return matrix


    mass_n = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])
    mass_delta_c12 = []
    mass_delta_c22 = []
    c12 = g/np.log(r2/r1)
    c22 = g/np.log(rg/r2)
    print('from theory:')
    print('r2', r2)
    print('r1', r1)
    print('rg', rg)
    print('c12_th:', c12)
    print('c22_th:', c22)

    for f in range(len(mass_n)):
        print('iteration', f+1)
        print('N = ', mass_n[f])
        m = create_circles(r2, mass_n[f])
        vector = mc.capacitance(m, a/2)
        mass_delta_c12.append(np.absolute(vector[1]-c12))
        mass_delta_c22.append(np.absolute(vector[2] - c22))
        print('delta_c12 = ', np.absolute(vector[1]-c12))
        print('delta_c22 = ', np.absolute(vector[2] - c22))
        print('------------------')

    print('mass_delta_c12:', mass_delta_c12)
    print('mass_delta_c22:', mass_delta_c22)


