import geomety_test as gt
import numpy as np
import copy
from matplotlib import pyplot as plt
import pygad
import krossingover
import mutation
import ground
import sss
import main_comsol as mc
import datetime
import os
detail_number = 2
N = 20

def detailspace(solution):
    solution_copy = copy.copy(solution)
    solution_copy[solution_copy != 0] = 1
    return solution_copy

def similarity(parent_1, parent_2):
    similarity_num = 0
    difference_parents = detailspace(parent_1) - detailspace(parent_2)


    return np.sum(np.abs(difference_parents))