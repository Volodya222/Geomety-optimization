import numpy as np
import main_comsol as mc
import geomety_test as gt
# import time
# start = time.time()

if __name__ == "__main__":
   n0 = 10
   matrix0, count0 = gt.parts(gt.smooth(np.random.randint(0, 2, (n0, n0))))
   radius0 = 0.1
   vector = mc.capacitance(matrix0, radius0)
   print(vector)
    # m = np.array([[1, 0, 0, 0, 0, 0, 2], [0, 0, 3, 3, 3, 0, 2], [3, 3, 3, 3, 3, 0, 2], [3, 3, 3, 3, 0, 0, 0],
    #               [0, 3, 3, 3, 0, 0, 4], [0, 0, 3, 3, 0, 0, 4], [5, 0, 3, 0, 0, 0, 4]])
    # n0 = 10
    # mass = [np.array([[1, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    #    [1, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    #    [1, 1, 1, 1, 1, 0, 0, 0, 2, 2],
    #    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    #    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    #    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    #    [0, 0, 4, 4, 4, 0, 0, 0, 0, 3]]), np.array([[0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    #    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    #    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    #    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1]]), np.array([[0, 1, 1, 0, 2, 2, 2, 2, 2, 2],
    #    [0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
    #    [3, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    #    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [4, 4, 4, 0, 0, 0, 0, 0, 0, 0],
    #    [4, 4, 4, 4, 4, 0, 0, 0, 0, 0],
    #    [4, 4, 4, 4, 4, 4, 4, 0, 0, 0]]), np.array([[0, 0, 1, 1, 1, 0, 0, 0, 2, 0],
    #    [0, 0, 1, 1, 1, 1, 1, 0, 2, 2],
    #    [0, 0, 0, 1, 1, 1, 1, 0, 2, 2],
    #    [0, 0, 0, 1, 1, 0, 0, 0, 2, 2],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    #    [3, 3, 0, 0, 0, 0, 0, 0, 0, 2],
    #    [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    #    [0, 0, 1, 1, 0, 2, 2, 2, 0, 1],
    #    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    #    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    #    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    #    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]), np.array([[0, 0, 0, 0, 1, 1, 0, 2, 2, 2],
    #    [0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    #    [0, 0, 0, 3, 3, 3, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 3, 3, 0, 0, 0, 4]]), np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    #    [1, 1, 1, 1, 0, 2, 0, 1, 1, 1],
    #    [1, 1, 0, 0, 0, 2, 0, 0, 0, 1],
    #    [1, 1, 0, 0, 0, 2, 0, 0, 0, 0],
    #    [1, 1, 0, 0, 0, 2, 0, 0, 0, 0],
    #    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]), np.array([[0, 1, 1, 0, 2, 2, 2, 2, 2, 2],
    #    [1, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    #    [0, 0, 0, 0, 3, 3, 0, 0, 0, 0],
    #    [0, 0, 0, 0, 3, 3, 0, 0, 0, 0],
    #    [4, 4, 0, 0, 3, 3, 0, 0, 0, 0],
    #    [4, 4, 0, 3, 3, 3, 0, 0, 0, 0],
    #    [0, 0, 0, 3, 3, 3, 0, 0, 0, 0],
    #    [5, 0, 0, 3, 3, 3, 3, 3, 3, 3],
    #    [5, 0, 0, 0, 0, 3, 3, 3, 3, 3],
    #    [5, 5, 0, 0, 0, 3, 3, 3, 0, 0]]), np.array([[1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    #    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [1, 0, 0, 0, 0, 2, 2, 2, 0, 0],
    #    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 1, 1, 1, 0, 0, 0, 0, 0, 2]]), np.array([[0, 1, 0, 2, 2, 2, 2, 2, 2, 2],
    #    [0, 1, 0, 2, 2, 2, 2, 2, 2, 2],
    #    [1, 1, 0, 0, 0, 2, 2, 2, 2, 2],
    #    [0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
    #    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    #    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    #    [2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
    #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [3, 0, 0, 0, 4, 4, 4, 0, 0, 0]]), np.array([[1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #    [1, 1, 1, 1, 0, 0, 0, 1, 0, 2],
    #    [1, 1, 1, 1, 0, 0, 0, 1, 0, 2],
    #    [1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    #    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    #    [3, 0, 0, 1, 1, 1, 1, 1, 0, 0]]), np.array([[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #    [0, 1, 1, 0, 0, 0, 0, 2, 0, 0],
    #    [0, 1, 1, 0, 0, 2, 2, 2, 0, 0],
    #    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    #    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    #    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    #    [2, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    #    [2, 2, 2, 0, 0, 0, 0, 1, 1, 1]])]
    #
    # # print(mass[6])
    #
    # for i in range(len(mass)):
    #    print('iter:', i+1,'/12')
    #    radius0 = 0.1
    #    vec1 = mc.capacitance_new(mass[i])
    #    print(vec1)
    #    print('----------------')
    #    if i == 1:
    #      print(mass[i])
    #      break
    #
    # end = time.time() - start
    # print(end)
    # vec2 = mc.capacitance_new(matrix0, radius0)
    # print(vec2)
