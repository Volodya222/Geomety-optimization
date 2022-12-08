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
# radius0 = 0.1
# ffc.change_radius_out(model0, geometry0, circle_ground0, radius0)
rad = 6.5  # радиус земли
x = 11.4  # сторона квадрата, в котром генерируются окружности
ffc.change_radius_out_cylinder(model0, geometry0, circle_ground0, x, rad)


def capacitance(matrix, radius):
    n = np.shape(matrix)[0]
    ffc.remove_details(model0, geometry0)
    ffc.creating_details(matrix, n, radius * 2, model0, geometry0, physics0, terminal_other0, initial_values0,
                         terminal_leg0)
    model0.build(geometry0)
    model0.solve('Study 1')
    vector = ffc.evaluate_matrix(model0, 'Study 1//Parametric Solutions 2')
    model0.save()
    return vector


def capacitance_cylinder(matrix, radius):
    n = np.shape(matrix)[0]
    ffc.remove_details(model0, geometry0)
    node_local = model0/'geometry'/geometry0/circle_ground0
    node_local.property('type', 'curve')
    ffc.creating_details(matrix, n, radius * 2, model0, geometry0, physics0, terminal_other0, initial_values0,
                         terminal_leg0)
    node_local.property('type', 'solid')
    model0.build(geometry0)
    model0.solve('Study 1')
    vector = ffc.evaluate_matrix(model0, 'Study 1//Parametric Solutions 2')
    model0.save()
    return vector


if __name__ == "__main__":
    geometry0 = 'geometry_test'
    circle_ground0 = 'circle_ground'
    ground0 = 'ground'
    terminal_leg0 = 'terminal_leg'
    terminal_other0 = 'terminal_other'
    initial_values0 = 'Initial Values 1'
    physics0 = 'Electrostatics'
    # N = 7
    # matrix0, count = gt.parts(gt.smooth(np.random.randint(0, 2, (N, N))))
    # radius1 = 0.1
    #
    # ffc.remove_details(model0, geometry0)
    #
    # ffc.creating_details(matrix0, N, radius1*2, model0, geometry0, physics0, terminal_other0, initial_values0, terminal_leg0)
    #
    # ffc.change_radius_out(model0, geometry0, circle_ground0, radius1*3)
    #
    # model0.build(geometry0)
    # model0.save()
    # model0.solve('Study 1')
    # m = ffc.evaluate_matrix(model0, 'Study 1//Parametric Solutions 2')
    # print(m)
    # model0.save()
    # print('Maxwell capacitance(matrix):')
    # print(m)

