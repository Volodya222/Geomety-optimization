import matplotlib.pyplot as plt
import numpy as np
import main_comsol as mc
params = {'font.family': 'Times New Roman', 'legend.fontsize': 15, 'figure.figsize': (18, 8), 'axes.labelsize': 17,
          'axes.titlesize': 20, 'xtick.labelsize': 17, 'ytick.labelsize': 17, 'figure.titlesize': 20}
plt.rcParams.update(params)

if __name__ == "__main__":
    N = 80  # размерность матрицы
    r1 = 0.3  # радиус первого круга в метрах
    d1 = 0.09  # толщина первого круга в метрах
    r2 = 5.7      # радиус второго круга в метрах
    d2 = 0.09  # толщина второго круга в метрах
    delta = 0.3  # шаг в метрах
    number_steps = 18  # количество шагов
    a = 13  # сторона квадрата в метрах
    rg = 7  # радиус земли в метрах
    k = a/N  # цена деления
    g = 2*np.pi*8.85  # константа для подсчета теоретической емкости с учетом \epsilon = 1, результа в pF

    # !!!!!Чтобы код работал корректно, нужно в main_comsol также задать значения радиуса земли и стороны квадрата !!!!!

    # геометрия цилиндрического конденатораб центры окружностей: (a/2 , -a/2)
    def create_circles(radius_2, N):
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

        mass_r2 = []  # значения r2
        mass_r2r1 = []  # значения r2/r1
        mass_rgr2 = []  # значения rg/r2
        mass_c12_theory = []  # емкости c12 теоретические
        mass_c22_theory = []  # емкости c22 теоретические
        mass_c12 = []  # емкости c12 из комсола
        mass_c22 = []  # емкости c22 из комсола

        # считаем теоертические значения
        for u in range(1, number_steps+1):
            radius2 = r1+u*delta
            mass_r2.append(radius2)
            mass_r2r1.append(radius2/r1)
            mass_rgr2.append(rg/radius2)
            c12 = g/np.log(radius2/r1)
            mass_c12_theory.append(c12)
            c22 = g/np.log(rg/radius2)
            mass_c22_theory.append(c22)

        mass_r2 = np.array(mass_r2)
        # пределы по осям для построения графиков
        x1_xmin = np.amin(mass_r2)
        x1_xmax = np.amax(mass_r2)
        mass_r2r1 = np.array(mass_r2r1)
        x2_xmin = np.amin(mass_r2r1)
        x2_xmax = np.amax(mass_r2r1)
        mass_rgr2 = np.array(mass_rgr2)
        x3_xmin = np.amin(mass_rgr2)
        x3_xmax = np.amax(mass_rgr2)
        mass_c12_theory = np.array(mass_c12_theory)
        mass_c22_theory = np.array(mass_c22_theory)
        print('list c22_theory:', mass_c22_theory)
        print('list of r2:', mass_r2)
        print('list of r2/r1:', mass_r2r1)
        print('list of rg/r2:', mass_rgr2)

        print('x1_limits:', x1_xmin, x1_xmax)
        print('x2_limits:', x2_xmin, x2_xmax)
        print('x3_limits:', x3_xmin, x3_xmax)
        print('///////////////////////////////////')
        # считаем комсоловские значения
        for p in range(1, number_steps+1):
            print('iteration:', p)
            rad2 = r1 + p * delta
            print('r2:', rad2)
            m = create_circles(rad2, N)
            vector = mc.capacitance(m, a/2)
            mass_c12.append(vector[1])
            mass_c22.append(vector[2])
            print('c12:', vector[1])
            print('c12_theory:', mass_c12_theory[p-1])
            print('c22:', vector[2])
            print('c22_theory:', mass_c22_theory[p-1])
            print('--------------------------------')

        mass_c12 = np.array(mass_c12)
        mass_c22 = np.array(mass_c22)
        print('list of c12:', mass_c12)
        print('list of c22:', mass_c22)

        fig, ax = plt.subplots(1, 3, edgecolor='black', linewidth=5, frameon=True)

        x1 = np.linspace(x1_xmin, x1_xmax, 400)
        x2 = np.linspace(x2_xmin, x2_xmax, 400)
        x3 = np.linspace(x3_xmin, x3_xmax, 400)

        # yi_jk - массив значений емкостей, i - номер плоскости, jk - индексы емкости в соответствии с матрицей
        y1_12 = np.array([g/np.log(i/r1) for i in x1])
        y1_22 = np.array([g/np.log(rg/i) for i in x1])

        y2_12 = np.array([g/np.log(i) for i in x2])
        y2_22 = np.array([g/np.log(rg/(r1*i)) for i in x2])

        y3_12 = np.array([g/np.log(i*rg/r1) for i in x3])
        y3_22 = np.array([g/np.log(i) for i in x3])

        ax[0].plot(x1, y1_12, label=r'$c_{12}^{th}(r_2)$', linestyle='solid', color='black')
        ax[0].plot(x1, y1_22, label=r'$c_{22}^{th}(r_2)$', linestyle='solid', color='gray')
        ax[0].set_xlabel(r'$r_2,~m$')
        ax[0].set_ylabel(r'$C,~pF$')
        ax[0].scatter(mass_r2, mass_c12_theory, label=r'$c_{12}~dots$', marker='o', color='red')
        ax[0].scatter(mass_r2, mass_c22_theory, label=r'$c_{22}~dots$', marker='o', color='blue')

        ax[0].scatter(mass_r2, mass_c12, label=r'$c_{12}^{model}$', marker='s', color='orange')
        ax[0].scatter(mass_r2, mass_c22, label=r'$c_{22}^{model}$', marker='8', color='green')

        ax[1].plot(x2, y2_12, label=r'$c_{12}^{th}(\frac{r_2}{r_1})$', linestyle='solid', color='black')
        ax[1].plot(x2, y2_22, label=r'$c_{22}^{th}(\frac{r_2}{r_1})$', linestyle='solid', color='gray')
        ax[1].set_xlabel(r'$\frac{r_2}{r_1}$')
        ax[1].set_ylabel(r'$C,~pF$')
        ax[1].scatter(mass_r2r1, mass_c12_theory, label=r'$c_{12}~dots$', marker='o', color='red' )
        ax[1].scatter(mass_r2r1, mass_c22_theory, label=r'$c_{22}~dots$', marker='o', color='blue' )

        ax[1].scatter(mass_r2r1, mass_c12, label=r'$c_{12}^{model}$', marker='s', color='orange')
        ax[1].scatter(mass_r2r1, mass_c22, label=r'$c_{22}^{model}$', marker='8', color='green')

        ax[2].plot(x3, y3_22, label=r'$c_{22}^{th}(\frac{r_g}{r_2})$', linestyle='solid', color='gray')
        ax[2].set_xlabel(r'$\frac{r_g}{r_2}$')
        ax[2].set_ylabel(r'$C,~pF$')

        ax[2].scatter(mass_rgr2, mass_c22_theory, label=r'$c_{22}~dots$', marker='o', color='red' )

        ax[2].scatter(mass_rgr2, mass_c22, label=r'$c_{22}^{model}$', marker='8', color='green')

        ax[0].legend()
        ax[1].legend()
        ax[2].legend()

        plt.show()



