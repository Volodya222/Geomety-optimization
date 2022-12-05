import geomety_test as gt
import numpy as np
import copy
from matplotlib import pyplot as plt
import pygad
import krossingover
import mutation
import ground
import main_comsol as mc

N = 5
mutation_flag = True
rad_ground = N / 2
count_matrix = []
count_matrix_1 = []


pop_size = 5
initial_population = []
counting_list = []
for i in range(pop_size):
    x_i = np.random.randint(0, 2, (N, N))
    x1_i = gt.smooth(x_i)
    y_i, count_i = gt.parts(x1_i)
    y_ig = ground.ground_test(y_i, rad_ground, N)
    counting_list.append(count_i)
    y_inum=y_ig.reshape((-1,))

    initial_population.append(y_inum)

print(initial_population)


def fitness_func(solution, solution_idx):
    vector_cap = mc.capacitance(solution.reshape(N, N))
    fitness = 1.0 / (0.000001 + sqrt((vector_cap[0]-c11)**2) + sqrt((vector_cap[1]-c12)**2) + sqrt((vector_cap[2]-c22)**2))
    return fitness
    
def crossover_func(parents, offspring_size, ga_instance):
    offspring = []
    parent1 = parents[0].reshape(N, N)
    parent2 = parents[1].reshape(N, N)
    offspring1, offspring2 = krossingover.krossingover(parent1, parent2)
    offspring1_resh = offspring1.reshape((-1,))
    offspring2_resh = offspring2.reshape((-1,))
    offspring.append(offspring1_resh)
    offspring.append(offspring2_resh)
    return numpy.array(offspring)

def mutation_func(offspring, ga_instance):
    offspring1 = offspring[0].reshape(N,N)
    offspring2 = offspring[1].reshape(N, N)
    mut_offspring1 = mutation.mutation(offspring1)
    mut_offspring2 = mutation.mutation(offspring2)
    mut_offspring1_resh = mut_offspring1.reshape((-1,))
    mut_offspring2_resh = mut_offspring2.reshape((-1,))
    offspring.append(mut_offspring1_resh)
    offspring.append(mut_offspring2_resh)
    return offspring





ga_instance = pygad.GA(num_generations = 100000000,
                    fitness_func = fitness_func,
                    num_parents_mating=2,
                    initial_population = initial_population,
                       # offspring_size = 2,
                    crossover_type = crossover_func,
                    mutation_type = mutation_func,
                    parent_selection_type="sss",
                       # save_best_solutions=True,
                       stop_criteria = ["reach_500000"])


ga_instance.run()
best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()
print(best_solution.reshape(N, N))
print(best_solution_fitness)
# print(ga_instance.initial_population)
# print(ga_instance.population)

