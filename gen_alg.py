import geomety_test as gt
import numpy as np
import copy
from matplotlib import pyplot as plt
import pygad
# import krossingover
# import mutation

N = 5
x = np.random.randint(0, 2, (N,N))
x1 = gt.smooth(x)
y, count = gt.parts(x1)
x = np.random.randint(0, 2, (N,N))
x1 = gt.smooth(x)
y_1, count_1 = gt.parts(x1)
rad_ground = N / 2
count_matrix = []
count_matrix_1 = []
zero = np.zeros_like(y)

pop_size = 5
initial_population = []
counting_list = []
for i in range(pop_size):
    x_i = np.random.randint(0, 2, (N, N))
    x1_i = gt.smooth(x_i)
    y_i, count_i = gt.parts(x1_i)
    counting_list.append(count_i)
    y_inum=y_i.reshape((-1,))

    initial_population.append(y_inum)

# print(initial_population)


def fitness_func(solution, solution_idx):
    
    

    




ga_instance = pygad.GA(num_generations = 10,
                    fitness_func = fitness_func,
                    num_parents_mating=2,
                    initial_population = initial_population)
                    # crossover_type = crossover_func,
                    # mutation_type = mutation_func,
                    # parent_selection_type="sss"


ga_instance.run()
print(ga_instance.initial_population)
print(ga_instance.population)

