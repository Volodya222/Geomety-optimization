import numpy as np
import main_comsol as mc
import geomety_test as gt


if __name__ == "__main__":
    n0 = 10
    matrix0, count0 = gt.parts(gt.smooth(np.random.randint(0, 2, (n0, n0))))
    radius0 = 0.1
    vector = mc.capacitance(matrix0, radius0)
    print(vector)