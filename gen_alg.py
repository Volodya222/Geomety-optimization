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

now = datetime.datetime.now()
s1 = now.strftime("%m_%d_%Y_%H_%M")
gen_plotpath = f'gen_plots_{s1}'
os.mkdir(gen_plotpath)
step_count = 0
radius = 0.1
N = 15
mutation_flag = True
rad_ground = N / 2
count_matrix = []
count_matrix_1 = []
c11 = 2845
c12 = 2289
c22 = 3644
detail_number = 3


pop_size = 5
initial_population = []
counting_list = []
for i in range(pop_size):
    count_i = 0
    while count_i != detail_number:

        x_i = np.random.randint(0, 2, (N, N))
        x1_i = gt.smooth(x_i)
        y_i, count_i = gt.parts(x1_i)
        y_ig = ground.ground_test(y_i, rad_ground, N)
        y_ig, count_i = gt.parts(y_ig)
    counting_list.append(count_i)
    y_inum=y_ig.reshape((-1,))

    initial_population.append(y_inum)

# print(initial_population)



def fitness_func(solution, solution_idx):
    vector_cap = mc.capacitance(solution.reshape(N, N), radius)
    # a = np.random.random(3)
    fitness = 1.0 / (0.000001 + np.sqrt((vector_cap[0]-c11)**2) + np.sqrt((vector_cap[1]-c12)**2) + np.sqrt((vector_cap[2]-c22)**2))
    # fitness = hash(solution.tostring)
    return fitness


def crossover_func(parents, offspring_size, ga_instance):

    new_gen = parents.copy()
    offspring = []
    parent1 = parents[0].reshape(N, N)
    parent2 = parents[1].reshape(N, N)
    a, count = gt.parts(parent1)
    a_1, count_1 = gt.parts(parent2)
    count_min = min(count, count_1)
    kross_numbers = np.random.permutation(np.arange(1, count_min + 1))
    kross_flag = False
    kross_flag1 = False
    fitness = np.sort(ga_instance.last_generation_fitness)[::-1]
    for kross_number in kross_numbers:
        offspring1, offspring2, kross_flag, kross_flag1 = krossingover.krossingover(parent1, parent2, N, kross_number)
        if kross_flag:
            new_gen = np.concatenate((new_gen, offspring1.reshape(1, -1)))
            f1 = ga_instance.fitness_func(offspring1.reshape((-1)), 0)
            fitness = np.concatenate((fitness, [f1]))
        if kross_flag1:
            new_gen = np.concatenate((new_gen, offspring2.reshape(1, -1)))
            f2 = ga_instance.fitness_func(offspring2.reshape((-1)), 0)
            fitness = np.concatenate((fitness, [f2]))
        if kross_flag1 or kross_flag:
            break
    print(kross_flag, kross_flag1)
    offspring1_resh = offspring1.reshape((-1,))
    offspring2_resh = offspring2.reshape((-1,))

    # f1 = ga_instance.fitness_func(offspring1_resh, 0)
    # f2 = ga_instance.fitness_func(offspring2_resh, 0)
    # new_gen = np.concatenate((parents, offspring1.reshape(1,-1), offspring2.reshape(1,-1)))
    # fitness = np.sort(ga_instance.last_generation_fitness)[::-1]
    # fitness = np.concatenate((fitness, [f1, f2]))
    print(fitness)
    ind = np.argsort(fitness)[::-1]
    fitness_sort = fitness[ind]
    new_gen = new_gen[ind, :]
    offspring = new_gen[:offspring_size[0], :]
    return offspring

def mutation_func(offspring, ga_instance):
    new_offspring = []
    for i in offspring:
        offspring1 = i.reshape(N,N)
        mutation_flag = False
        while mutation_flag == False:
            mut_offspring1, mutation_flag = mutation.mutation(offspring1, N)
            mut_offspring1_resh = mut_offspring1.reshape((-1,))
            # print('a')
        print(mutation_flag)
        new_offspring.append(mut_offspring1_resh)
    # return new_offspring
    return np.array(new_offspring)

n = int(np.ceil(np.sqrt(pop_size)))
def on_generation(ga_instance):
    global step_count
    step_count += 1
    fig, axs = plt.subplots(n, n)
    for i in range(n):
        for j in range(n):
            if (i*n + j) < pop_size:
                vector = ga_instance.population[i*n + j]
                axs[i, j].imshow(vector.reshape((N, N)))
    plt.suptitle(f'step {step_count}')
    #plt.show()
    plt.savefig(f'{gen_plotpath}/plot_{step_count}')
    plt.clf()

def on_crossover(ga_instance, offspring):
    index_del = np.ones((ga_instance.population.shape[0]))

    for i in range(len(ga_instance.population) - 1):
        for j in range(i, len(ga_instance.population)):
            if (ga_instance.population[i] == ga_instance.population[j]).all():
                index_del[j] = 0
                break
    index_del = np.asarray(index_del, dtype=bool)

    ga_instance.population = ga_instance.population[index_del, :]
def on_fitness(ga_instance, population_fitness):
    print("on_fitness()")

def on_start(ga_instance):
    fig, axs = plt.subplots(n, n)
    for i in range(n):
        for j in range(n):
            if (i * n + j) < pop_size:
                vector = ga_instance.initial_population[i * n + j - 1]
                axs[i, j].imshow(vector.reshape((N, N)))
    plt.suptitle(f'step {step_count}')
    #plt.show()
    plt.savefig(f'{gen_plotpath}/plot_{step_count}')
    plt.clf()





ga_instance = pygad.GA(num_generations = 3,
                    fitness_func = fitness_func,
                    num_parents_mating = pop_size,
                    initial_population = initial_population,
                       # offspring_size = 2,
                    crossover_type = crossover_func,
                    mutation_type = mutation_func,
                    parent_selection_type='sss',
                       keep_parents = 0,
                       keep_elitism = 0,
                       # save_best_solutions=True,
                       # stop_criteria = ["reach_500000"],
                       on_generation = on_generation,
                       on_crossover = on_crossover,
                       on_start = on_start)


ga_instance.run()
# best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()
# print(best_solution.reshape(N, N))
# print(best_solution_fitness)
# print(ga_instance.initial_population)
# print(ga_instance.population)

