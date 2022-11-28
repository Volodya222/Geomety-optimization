# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:47:49 2022

@author: dmitry
"""

import main_comsol
import numpy as np
import geomety_test as gt
#import timeit
from time import time

radius = 0.1
N = 7 # размер матрицы в пикселях
N_part = 3 # количество деталей

ts=[]

for i in range(10):

    count = 0

    while count != N_part: 
        x = np.random.randint(0, 2, (N,N))
        matrix0, count = gt.parts(gt.smooth(x))

    t0 = time()
    main_comsol.capacitance(matrix0, count, radius)
    t1 = time()
    
    t = t1-t0
    
    ts.append(t)
    print(t)

print(f'Average: {np.mean(ts)}')
    
#    timeit.timeit('"-".join(main_comsol.capacitance(matrix0, count, radius))', number=1)
