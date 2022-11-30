import numpy as np

import geomety_test as gt
import main_comsol as mc
N = 7
matrix0, count = gt.parts(gt.smooth(np.random.randint(0, 2, (N, N))))
radius1 = 0.1
m = mc.capacitance(matrix0, radius1)
print(m)
