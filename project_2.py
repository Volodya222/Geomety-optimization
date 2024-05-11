import numpy as np
import matplotlib.pyplot as plt
import numba
import time

size = 300

def create_circles(n):
    size: int = 300
    # радиус ноги
    r = 0.1
    # внешний радиус
    rad = 0.3
    # сторона квадрата, в котором генерируется и земля, и детали
    a = 2 * rad
    # цена деления
    k: float = a / size
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            x = (j - 1) * k + k / 2
            y = (i - 1) * k + k / 2
            if np.power(x - 0.5 * a, 2) + np.power(y - 0.8 * a, 2) <= np.power(r, 2):
                matrix[i][j] = 1
            elif np.power(x - 0.5 * a, 2) + np.power(y - 0.5 * a, 2) >= np.power(rad, 2):
                matrix[i][j] = 0
            else:
                matrix[i][j] = -1
    for g in range(int(size / 2 - 0.06 * size), int(size / 2 + 0.06 * size)):
        for f in range(int(size / 2 - 0.06 * size), int(size / 2 + 0.06 * size)):
            matrix[g][f] = 2

    return matrix


def create_plates(n):
    size: int = 300
    # радиус ноги
    r = 0.1
    # внешний радиус
    rad = 0.3
    # сторона квадрата, в котором генерируется и земля, и детали
    a = 2 * rad
    # цена деления
    k: float = a / size
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            x = (j - 1) * k + k / 2
            y = (i - 1) * k + k / 2
            if np.power(x - a / 2, 2) + np.power(y - a / 2, 2) >= np.power(rad, 2):
                matrix[i][j] = -1
            # x = (j-1) * k + k / 2
            # y = (i-1) * k + k / 2
            elif int(size / 3) <= i <= int(size * 11 / 30) and int(size / 3) <= j <= int(size / 3 * 2):
                matrix[i][j] = 2
            elif int(size / 3 * 2) <= i <= int(size * 0.7) and int(size / 3) <= j <= int(size / 3 * 2):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix




def solver(geometry: np.ndarray):
    # размер матрицы
    size: int = 100
    # внешний радиус
    rad = 0.3
    # сторона квадрата, в котором генерируется и земля, и детали
    a = 2*rad
    # цена деления
    k: float = a/size

    # функция, генерирующая 2 круг

    # генерирует 2 пластины

    m = np.copy(geometry)

    # m = create_circles(size)

    # точка отсчета времени
    time_start = time.time()

    # Здаем вид границ
    fixed_bool = m != 0

    # устанавливаем потенциалы на детали(работает, проверил)
    # матрица, когда на первой детали 1в
    fixed1 = np.select([m == -1, m == 0, m == 1, m > 1], [0, -1, 1, 0])
    # матрица, когда на второй детали 1в
    fixed0 = np.select([m == -1, m == 0, m == 1, m > 1], [0, -1, 0, 1])

    # эта штука решает уравнения Лапласа
    @numba.jit("f8[:,:](f8[:,:], b1[:,:])", nopython=True, fastmath=True, parallel=True, cache=True, nogil=True)
    def compute_potential(potential_func: np.ndarray, fixed_bool_func: np.ndarray) -> np.ndarray:
        for i_f in range(1, len(potential_func[0])-1):
            for j_f in range(1, len(potential_func[0])-1):
                # условие ниже проверяет, что пересчитываются только квадраты, соответствующие пустому пространству

                if not(fixed_bool_func[j_f][i_f]):
                    potential_func[j_f][i_f] = 1/4 * (potential_func[j_f+1][i_f] + potential_func[j_f-1][i_f] +
                                                      potential_func[j_f][i_f+1] + potential_func[j_f][i_f-1])
        return potential_func

    # параметр точности
    epsilon: float = 1e-8

    # это уже полное решение уравнения Лапласа
    def laplace(f: np.ndarray) -> np.ndarray:
        # potential -- это итоговый потенциал в каждой клетке матрицы
        potential = np.zeros((size, size))
        # potential[0, :] = lower_y
        # potential[-1, :] = upper_y
        # potential[:, 0] = lower_x
        # potential[:, -1] = upper_x

        # тут задаются начальные значения потенциалов на деталях и земле(либо матрицей из ф-ии case1, либо матрицей из
        # ф-ии case0)

        potential[fixed_bool] = f[fixed_bool]
        # массивы ошибок и кол-ва итераций
        # array_error, array_iter = np.array([]), np.array([])

        while True:
            # массив предыдущего значения потенциалов
            v_previous = np.copy(potential)
            potential = compute_potential(potential, fixed_bool)
            # евклидова норма
            err = np.sqrt(np.sum((v_previous-potential)**2)/size**2)
            # массив ошибок
            # array_error = np.append(array_error, err)
            # массив итераций
            # array_iter = np.append(array_iter, n_i)

            if err < epsilon:
                break
            # else:
            #     n_i = n_i + 1
            #     print('Номер итерации:' + str(n_i))
            #     print('Текущая ошибка:' + str(err))
            #     # , array_iter, array_error
        return potential

    # решенные уравнения Лапласа для случаев, когда на 1 детали 1в и когда на второй детали 1в соответственно
    # potential1, array_iter1, array_error1 = laplace(fixed1)
    # potential0, array_iter0, array_error0 = laplace(fixed0)


    potential1 = laplace(fixed1)
    potential0 = laplace(fixed0)
    # np.savetxt("array_potential_1200.csv", potential, delimiter=" ,")
    # np.savetxt ("array_iter_error.csv", array_error, delimiter=" ,")

    # просто выводим картинки
    # fig, ax = plt.subplots(1, 2, figsize=(18, 6), frameon=True, edgecolor='black', linewidth=4)
    # plt.style.use(['science', 'notebook'])
    # fig.suptitle('Matrix size='+str(size)+','+' '+'time='+str(round(time_end, 1)), fontsize=20)
    #
    # clr_plot = ax[0].contourf(xv, yv, potential1, 50)
    # ax[0].set_xlabel(r'$x/r_{leg}$')
    # ax[0].set_ylabel('$y/r_{leg}$')
    # fig.colorbar(clr_plot, label='$V/V_0$', ax=ax[0])
    # ax[0].set_title('Potential1')
    # ax[1].set_title(r'error(amount of iter), $\epsilon=$'+str(epsilon), fontsize=20)
    # ax[1].set_xlabel('amount of iter', fontsize=16)
    # ax[1].set_ylabel(r'$||(V_{current}-V_{previous})||_{2}$', fontsize=16, bbox=dict(facecolor='white'))
    # ax[1].scatter(array_iter1, array_error1, color='red')
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()
    #
    # fig, ax = plt.subplots(1, 2, figsize=(18, 6), frameon=True, edgecolor='black', linewidth=4)
    # plt.style.use(['science', 'notebook'])
    # fig.suptitle('Matrix size='+str(size)+','+' '+'time='+str(round(time_end, 1)), fontsize=20)
    #
    # clr_plot = ax[0].contourf(xv, yv, potential0, 50)
    # ax[0].set_xlabel(r'$x/r_{leg}$')
    # ax[0].set_ylabel('$y/r_{leg}$')
    # fig.colorbar(clr_plot, label='$V/V_0$', ax=ax[0])
    # ax[0].set_title('Potential0')
    # ax[1].set_title(r'error(amount of iter), $\epsilon=$'+str(epsilon), fontsize=20)
    # ax[1].set_xlabel('amount of iter', fontsize=16)
    # ax[1].set_ylabel(r'$||(V_{current}-V_{previous})||_{2}$', fontsize=16, bbox=dict(facecolor='white'))
    # ax[1].scatter(array_iter0, array_error0, color='red')
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()

    # считаем заряд

    # цикл, определяющий границу деталей и земли
    # fixed_ch = np.copy(fixed_bool)
    fixed_ch_copy = np.copy(fixed_bool)
    for i in range(size):
        for j in range(size):
            if fixed_bool[j][i]:
                # на самой границе матрицы вызникают проблемы с условием првоерки, поэтому проще сразу сказать, что это
                # точно не граница, на которой будет скапливаться заряд
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    fixed_ch_copy[j][i] = False
                else:
                    if (fixed_bool[j + 1][i]) and (fixed_bool[j - 1][i]) and (fixed_bool[j][i + 1]) and (fixed_bool[j][i - 1]):
                        fixed_ch_copy[j][i] = False
    # просто рисуем границу
    # plt.imshow(fixed_ch_copy)
    # plt.show()

    # эта штука уже считает заряд
    @numba.jit(nopython=True, fastmath=True)
    def compute_charge(flag: bool)-> float:
        # q1 -- заряд на детали с потенцилалом 1в
        # q0 -- с потенциалом 0v
        # q_g -- заряд на земле
        q1 = 0
        q0 = 0
        q_g = 0
        # flag == True соответсвует case1, flag == Flase, соответствует case0
        for i in range(size):
            for j in range(size):
                if fixed_ch_copy[j][i]:
                    if flag:
                        # т.е. тут 1-ой детали соответствует 1в. Если на исходнйо матрице m(она приходит на вход) m[i][j]==1
                        # , то это q1, если >1(соответсвует 2-о1 детали), то это q2
                        if m[j][i] == 1:
                            q1 += k*(potential1[j+1][i]+potential1[j-1][i]+potential1[j][i+1]+potential1[j][i-1]-(4*potential1[j][i]))

                        elif m[j][i] > 1:
                            q0 += k * (potential1[j + 1][i] + potential1[j - 1][i] + potential1[j][i + 1] + potential1[j][i - 1] - (
                                    4 * potential1[j][i]))
                        elif m[j][i] == -1:
                            q_g += k * (potential1[j + 1][i] + potential1[j - 1][i] + potential1[j][i + 1] + potential1[j][i - 1] - (
                                    4 * potential1[j][i]))
                    elif not flag:
                        # тут наоборот: на детали 1 0 в, а на детали 2(что в исходнйо матрице m соответствует m[i][j]>1) 1в
                        if m[j][i] == 1:
                            q0 += k*(potential0[j+1][i]+potential0[j-1][i]+potential0[j][i+1]+potential0[j][i-1]-(4*potential0[j][i]))

                        elif m[j][i] > 1:
                            q1 += k * (potential0[j + 1][i] + potential0[j - 1][i] + potential0[j][i + 1] + potential0[j][i - 1] - (
                                    4 * potential0[j][i]))
                        elif m[j][i] == -1:
                            q_g += k * (potential0[j + 1][i] + potential0[j - 1][i] + potential0[j][i + 1] + potential0[j][i - 1] - (
                                    4 * potential0[j][i]))
        # тут я просто забыл, что напряженность E -- это  минус grad(phi)
        q1 = q1 * (-1)
        q0 = q0 * (-1)
        q_g = q_g * (-1)
        return q1, q0, q_g

    q1_1, q0_1, q_g_1 = compute_charge(True)
    q1_0, q0_0, q_g_0 = compute_charge(False)

    # Максвелловские емкости
    c11 = q1_1
    c22 = q1_0

    c12 = q0_0
    c21 = q0_1

    c11_mutual = (c11 + c12) * (8.854188 / k)
    c12_mutual = -c12 * (8.854188 / k)
    c21_mutual = -c21 * (8.854188 / k)
    c22_mutual = (c21 + c22) * (8.854188 / k)
    time_end = time.time() - time_start
    # print('--------------------------------------------------------------')
    # print('TIME:', str(time_end))
    # print('--------------------------------------------------------------')
    # # переводим в частичные емкости (не единицу длины)
    # второй множитель -- нормировка, ответ в pF
    # print('c11_mutual:'+str(c11_mutual))
    # print('c12_mutual:'+str(c12_mutual))
    # print('c21_mutual:'+str(c21_mutual))
    # print('c22_mutual:'+str(c22_mutual))
    return c11_mutual, c12_mutual, c21_mutual, c22_mutual


# solver(create_plates(size))

