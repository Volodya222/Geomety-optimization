import numpy as np
import mph as mph
import geomety_test as gt
import functions_for_comsol as ffc


circle_ground = 'circle_ground'
circle_leg = 'circle_leg'
ground = 'ground'
terminal_leg = 'terminal_leg'
terminal_other = 'terminal_other'
initial_values = 'Initial Values 1'

# размер квадратной матрицы
N = 7
# matrix - матрица, count - кол-во деталей
matrix0, count = gt.parts(gt.smooth(np.random.randint(0, 2, (N, N))))
radius1 = 0.1
# m = np.array([[1,1,1,1,1], [0,0,0,1,0], [0,0,1,0,0],[0,1,0,0,0],[1,1,1,1,1] ])


if __name__ == '__main__':
    client = mph.start()
    model1 = client.load('test.mph')
    node1 = model1 / 'geometry' / 'geometry_test' / 'circle_ground'
    geometry0 = ffc.name_of_geometry(model1)
    node3 = model1 / 'physics' / 'Electrostatics' / 'terminal_leg'

    # model1.build()
    # model1.save()
