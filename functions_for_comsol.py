import numpy as np
import mph as mph
import geomety_test as gt
circle_ground = 'circle_ground'
circle_leg = 'circle_leg'
ground = 'ground'
terminal_leg = 'terminal_leg'
terminal_other = 'terminal_other'
initial_values = 'Initial Values 1'

def calc_capacity(model, c: str, dimension: str):
    return model.evaluate('es.C'+c, dimension)


def maxwell_to_mutual(matrix, decimals):

    new_matrix = np.array([[1., 1.], [1., 1.]])

    new_matrix[0, 0] = np.around(matrix[0, 0] + matrix[0, 1], decimals)
    new_matrix[0, 1] = np.around((-1)*matrix[0, 1], decimals)
    new_matrix[1, 0] = np.around((-1)*matrix[1, 0], decimals)
    new_matrix[1, 1] = np.around(matrix[1, 0] + matrix[1, 1], decimals)
    return new_matrix


# размер квадратной матрицы
# N = 7
# matrix - матрица, count - кол-во деталей
# matrix0, count = gt.parts(gt.smooth(np.random.randint(0, 2, (N, N))))
# radius1 = 0.1
# m = np.array([[1,1,1,1,1], [0,0,0,1,0], [0,0,1,0,0],[0,1,0,0,0],[1,1,1,1,1] ])


# генерирует детали
def creating_details(matrix, size: int, a, model):
    # a - сторона квадрата
    k = a/size    # цена деления
    geometry = name_of_geometry(model)
    node = model/'geometry'/geometry
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
                # сравнить initial values и добавить домен в эту функцию, ввести список с доменами
    model.build(geometry)
    return


# возвращает имя геометрии при заданной модели
def name_of_geometry(model):
    return model.geometries()[0]


# возвращает имя физики при заданной модели
def name_of_physic(model):
    return model.physics()[0]


# очищает геометрию модели
def remove_details(model):
    geometry = name_of_geometry(model)
    node_local = model/'geometry'/geometry
    list_of_details = node_local.children()
    for i in range(0, len(list_of_details)-1):
        # detail_i -- название объекта в геометрии
        detail_i = str(list_of_details[i]).partition('/')[2][str(list_of_details[i]).partition('/')[2].find('/')+1:]
        if (detail_i != 'circle_ground') and (detail_i != 'circle_leg'):
            node_local_local = node_local/detail_i
            node_local_local.remove()
    return


# генерирует землю
def creating_ground(model, radius):
    geometry = name_of_geometry(model)
    node_local = model/'geometry'/geometry
    node_local.create('Circle', name='circle_ground')
    node_local = model / 'geometry' / geometry/'circle_ground'
    node_local.property('r', radius)
    node_local.property('x', str(-radius))
    node_local.property('y', str(-radius))
    node_local.property('type', 'solid')
    node_local.property('selresultshow', 'all')
    node_local.property('color', '2')

    return

# задает второй терминал
# def sorting_terminals(model, ground, terminal_leg, terminal_other, initial_values):
#     physic = name_of_physic(model)
#     node_other = model / 'physics' / physic / terminal_other
#     node_ground = model / 'physics' / physic / ground
#     node_values = model/'physics'/physic/initial_values
#     node_leg = model/'physics'/physic/terminal_leg
#     print('leg:', node_leg.selection())
#     # list_ground = node_ground.selection()
#     # print(list_ground)
#     list_values = node_values.selection()
#     print('values:', list_values)
#     list_leg = node_leg.selection()
#
#     list_other = node_other.selection()
#     print('other:', list_other)
#     list_other_new = list(list_other.copy())
#     # list_other_new.remove('1')
#     for i in range(0, len(list_other)):
#         if list_other[i] in list_leg:
#             list_other_new.remove(list_other[i])
#
#     node_other.select(list_other_new)
#     print('new:', list_other_new)
#     print('new_selection:', node_other.selection())
#     return


# смена радиуса земли
def change_radius_out(model, circle_ground, r):
    geometry = name_of_geometry(model)
    node_local = model/'geometry'/geometry/circle_ground
    node_local.property('r', r)
    return


# смена радиуса ноги
def change_radius_leg(model, circle_leg, r):
    geometry = name_of_geometry(model)
    node_local = model/'geometry'/geometry/circle_leg
    node_local.property('r', r)
    return


# считает матрицу
# def evaluate_matrix(model, count, dataset):
#     answer = np.zeros((count, count))
#     for i in range(1, count+1):
#         for j in range(1, count+1):
#             answer[i-1][j-1] = model.evaluate('es.C'+str(i)+str(j), 'pF', dataset=dataset)
#     return answer


# client = mph.start()
# model1 = client.load("test.mph")
# node1 = model1/'geometry'/'geometry_test'/'circle_ground'
# geometry0 = name_of_geometry(model1)
# node3 = model1/'physics'/'Electrostatics'/'terminal_leg'
#
#
#
# remove_details(model1)
# creating_details(matrix0, N, radius1*2, model1)
# sorting_terminals(model1, ground, terminal_leg, terminal_other, initial_values)
# creating_ground(model, 1)
# model.build(geometry0)




# print(node22.properties())
# print(model.evaluate('es.C11', 'pF', dataset='Study 1//Parametric Solutions 1'))
# print(model.evaluate('es.C12', 'pF', dataset='Study 1//Parametric Solutions 1'))
# print(model.evaluate('es.C21', 'pF', dataset='Study 1//Parametric Solutions 1'))
# print(model.evaluate('es.C22', 'pF', dataset='Study 1//Parametric Solutions 1'))
# c12 = float(model.evaluate('es.C11', 'pF'))
# print(c12)
# c12 = float(model.evaluate('es.C12', 'pF'))
# c13 = float(model.evaluate('es.C13', 'pF'))
# c21 = float(model.evaluate('es.C21', 'pF', dataset='Study 2//Parametric Solutions 2'))
# c22 = float(model.evaluate('es.C22', 'pF'))


# model1.build()
# model1.save()

