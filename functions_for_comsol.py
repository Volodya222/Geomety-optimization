import numpy as np


# очищает геометрию модели
def remove_details(model, geometry):
    node_local = model/'geometry'/geometry
    list_of_details = node_local.children()
    for i in range(0, len(list_of_details)-1):
        # detail_i - название объекта в геометрии
        detail_i = str(list_of_details[i]).partition('/')[2][str(list_of_details[i]).partition('/')[2].find('/')+1:]
        if detail_i != 'circle_ground':
            node_local_local = node_local/detail_i
            node_local_local.remove()
    return


# генерирует детали
def creating_details(matrix, size: int, a, model, geometry, physic, terminal_other, initial_values, terminal_leg):
    # a - сторона квадрата
    k = a/size    # цена деления
    list_terminal_leg = []
    list_terminal_other = []
    node = model/'geometry'/geometry
    node_other = model/'physics'/physic/terminal_other
    node_values = model/'physics'/physic/initial_values
    node_leg = model/'physics'/physic/terminal_leg
    for i in range(0, size):
        for j in range(0, size):
            if matrix[i, j] != 0:
                name_for_square = 's_'+str(i)+'_'+str(j)    # имя блока
                node.create('Square', name=name_for_square)
                node_local = node/name_for_square
                node_local.property('size', k)
                node_local.property('selresult', 'on')
                node_local.property('selresultshow', 'all')
                node_local.property('color', '5')
                node_local.property('base', 'center')
                node_local.property('x', j*k+k/2)
                node_local.property('y', -i*k-k/2)
                model.build(geometry)

    # list_terminal = np.delete(node_values.selection(), 0)
    list_terminal = node_values.selection()
    c = 0
    for j in range(0, size):
        for i in range(size-1, -1, -1):
            if matrix[i, j] != 0:
                if matrix[i, j] == 1:
                    list_terminal_leg.append(list_terminal[c])
                    c = c+1
                if matrix[i, j] > 1:
                    list_terminal_other.append(list_terminal[c])
                    c = c + 1
    list_terminal_leg = np.array(list_terminal_leg)
    list_terminal_other = np.array(list_terminal_other)
    node_other.select(list_terminal_other)
    node_leg.select(list_terminal_leg)
    return


# смена радиуса земли
def change_radius_out(model, geometry, circle_ground, r):
    node_local = model/'geometry'/geometry/circle_ground
    node_local.property('r', r)
    node_local.property('x', r)
    node_local.property('y', -r)
    model.save()
    return


# смена радиуса земли для цилиндра
def change_radius_out_cylinder(model, geometry, circle_ground, o, r):
    node_local = model/'geometry'/geometry/circle_ground
    node_local.property('r', r)
    node_local.property('x', o/2)
    node_local.property('y', -o/2)
    model.save()
    return


# считает емкости(частичные)
def evaluate_matrix(model, dataset):
    c11 = model.evaluate('es.C11', 'pF', dataset=dataset)
    c21 = model.evaluate('es.C21', 'pF', dataset=dataset)
    c22 = model.evaluate('es.C22', 'pF', dataset='Study 1//Solution 1')
    c11_new = c11 + c21
    c21_new = (-1)*c21
    c22_new = c22 + c21
    answer = np.array([c11_new, c21_new, c22_new])
    return answer

# if __name__ == "__main__":
#     # размер квадратной матрицы
#     N = 7
#     # matrix - матрица, count - кол-во деталей
#     matrix0, count = gt.parts(gt.smooth(np.random.randint(0, 2, (N, N))))
#     radius1 = 0.1
#     geometry1 = 'geometry_test'
#     circle_ground1 = 'circle_ground'
#     ground1 = 'ground'
#     terminal_leg1 = 'terminal_leg'
#     terminal_other1 = 'terminal_other'
#     initial_values1 = 'Initial Values 1'
#     physics1 = 'Electrostatics'
#     client = mph.start()
#     model1 = client.load("test.mph")
#     remove_details(model1, geometry1)
#     model1.build(geometry1)
#     model1.save()
#
#
#     creating_details(matrix0, N, radius1*2, model1, geometry1, physics1, terminal_other1, initial_values1, terminal_leg1)
#     change_radius_out(model1, geometry1, circle_ground1, 0.2)
#     model1.build(geometry1)
#     model1.save()
#     model1.solve('Study 1')
#     m = evaluate_matrix(model1, 'Study 1//Parametric Solutions 2')
#     print(m)
#
#     model1.save()

