import numpy as np
import mph as mph
import geomety_test as gt
import functions_for_comsol as ffc

client = mph.start()
model0 = client.load("test.mph")

def capacitance(a_matrix0, a_count, a_radius):
    # вход: геометрия в виде матрицы, радиус земли
    # общая функция 24-36, убрать save
    # вектор с емкостями

    geometry0 = 'geometry_test'
    circle_ground0 = 'circle_ground'
    ground0 = 'ground'
    terminal_leg0 = 'terminal_leg'
    terminal_other0 = 'terminal_other'
    initial_values0 = 'Initial Values 1'
    physics0 = 'Electrostatics'

    ffc.remove_details(model0, geometry0)
    ffc.creating_details(a_matrix0, a_matrix0.shape[0], a_radius*2, model0, 
                         geometry0, physics0, terminal_other0, initial_values0, 
                         terminal_leg0)

#    ffc.change_radius_out(model0, geometry0, circle_ground0, radius1*3)

    model0.build(geometry0)
#    model0.save()
    model0.solve('Study 1')
    m = ffc.evaluate_matrix(model0, 'Study 1//Parametric Solutions 2')
#    model0.save()
    print('Maxwell capacitance(matrix):')
    print(m)

    return m
