import numpy as np
import mph as mph
import functions_for_comsol as ffc
client = mph.start()
model0 = client.load("test.mph")
geometry0 = 'geometry_test'
circle_ground0 = 'circle_ground'
ground0 = 'ground'
terminal_leg0 = 'terminal_leg'
terminal_other0 = 'terminal_other'
initial_values0 = 'Initial Values 1'
physics0 = 'Electrostatics'
#-----------------------------------------------------------------------------------------------------
# если запускается testing_random_geometry, нужно заккоментить функцию ffc.change_radius_out_cylinder
radius0 = 0.1  # радиус земли в метрах
ffc.change_radius_out(model0, geometry0, circle_ground0, radius0)
#-----------------------------------------------------------------------------------------------------
# если запускается cylinder_capacitance, нужно заккоментить функцию ffc.change_radius_out
# rad = 7  # радиус земли в метрах
# x = 13  # сторона квадрата в метрах, в котором генерируются окружности
# ffc.change_radius_out_cylinder(model0, geometry0, circle_ground0, x, rad)
#-----------------------------------------------------------------------------------------------------
# ffc.remove_details(model0, geometry0)
# model0.save()
# n = 10
# list_terminal = ffc.creating_details_new(n, radius0 * 2, model0, geometry0, physics0,
#                                          initial_values0, circle_ground0)
# node_other = model0 / 'physics' / physics0 / terminal_other0
# node_leg = model0 / 'physics' / physics0 / terminal_leg0
# node_local = model0 / 'geometry' / geometry0 / circle_ground0


def capacitance(matrix, radius):
    n = np.shape(matrix)[0]
    ffc.remove_details(model0, geometry0)
    node_local = model0 / 'geometry' / geometry0 / circle_ground0
    node_local.property('type', 'curve')
    ffc.creating_details(matrix, n, radius * 2, model0, geometry0, physics0, terminal_other0, initial_values0,
                         terminal_leg0)
    node_local.property('type', 'solid')
    model0.build(geometry0)
    model0.solve('Study 1')
    vector = ffc.evaluate_matrix(model0, 'Study 1//Parametric Solutions 2')
    # model0.save()
    return vector


# def capacitance_new(matrix):
#     node_local.property('type', 'curve')
#     ffc.change_terminals(matrix, list_terminal, n, model0, physics0, terminal_other0, terminal_leg0)
#     model0.build(geometry0)
#     node_local.property('type', 'solid')
#     model0.build(geometry0)
#     # model0.solve('Study 1')
#     # vector = ffc.evaluate_matrix(model0, 'Study 1//Parametric Solutions 2')
#     model0.save()
#     return







