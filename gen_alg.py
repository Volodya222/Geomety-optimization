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
import similarity as sim
import project_2 as pr
import pngtopy as png





now = datetime.datetime.now()
s1 = now.strftime("%m_%d_%Y_%H_%M")
gen_plotpath = f'gen_plots_{s1}'
os.mkdir(gen_plotpath)
step_count = 0
radius = 0.1
N = 100
Full_sq = N ** 2
mutation_flag = True
rad_ground = N / 2
count_matrix = []
count_matrix_1 = []
c11 = 2845
c12 = 2289
c22 = 3644
detail_number = 2
delta = 1
desired_detail_num = 2
desired_square_percent = 0.4

pop_size = 3
initial_population = []
counting_list = []
# for i in range(pop_size):
#     count_i = 0
#     while count_i != detail_number:
#
#         x_i = np.random.randint(0, 2, (N, N))
#         x1_i = gt.smooth(x_i)
#         y_i, count_i = gt.parts(x1_i)
#         y_ig = ground.ground_test(y_i, rad_ground, N)
#         y_ig, count_i = gt.parts(y_ig)
#     counting_list.append(count_i)
#     y_inum=y_ig.reshape((-1,))
#
#     initial_population.append(y_inum)
initial_population.append(png.convert('g1.jpeg').reshape((-1,)))
initial_population.append(png.convert('g2.jpeg').reshape((-1,)))
initial_population.append(png.convert('g3.jpeg').reshape((-1,)))
# initial_population.append(png.convert('g4.jpeg').reshape((-1,)))
# initial_population.append(png.convert('g5.jpeg').reshape((-1,)))

# print(initial_population)

print(type(initial_population[1]))
print(initial_population[1].reshape(N,N))
print(initial_population[1].reshape(N,N).shape)
print(type(initial_population[2]))
print(initial_population[2].reshape(N,N).shape)

def fitness_func(solution, solution_idx):
    # vector_cap = mc.capacitance(solution.reshape(N, N), radius)
    # a = np.random.random(3)
    # fitness = 1.0 / (delta + np.sqrt((vector_cap[0]-c11)**2) + np.sqrt((vector_cap[1]-c12)**2) + np.sqrt((vector_cap[2]-c22)**2))
    count_matrix = np.zeros((detail_number,), dtype = int)
    # print(count_matrix)
    # for k in range(1, detail_number + 1):
    #     for i in range(0, N):
    #         for j in range(0, N):
    #             solution_resh = solution.reshape(N, N)
    #             if solution_resh[i, j] == k:
    #                 count_matrix[k - 1] += 1
    # print(count_matrix/ Full_sq)
    fitness = 1.0 / (delta + abs(c11 - pr.solver(solution.reshape(N,N))[0]) +
                     abs(c12 - pr.solver(solution.reshape(N,N))[1]) +
                     abs(c22 - pr.solver(solution.reshape(N,N))[3]))
    return fitness


def crossover_func(parents, offspring_size, ga_instance):

    new_gen = parents.copy()
    offspring = []
    parent1 = parents[0].reshape(N, N)
    # parent2 = parents[1].reshape(N, N)
    # print(parent1)
    # print(sim.detailspace(parent2))
    # print(sim.similarity(parent1, parent2))
    choose_parents = []

    for i in range(1, len(parents)):
        choose_parents.append(sim.similarity(parent1, parents[i].reshape(N,N)))
    parent2 = parents[choose_parents.index(max(choose_parents)) + 1].reshape(N,N)
    # print(parent2)
    # print(sim.similarity(parent1, parent2))

    # a, count = gt.parts(parent1)
    # a_1, count_1 = gt.parts(parent2)
    # count_min = min(count, count_1)
    # kross_numbers = np.random.permutation(np.arange(1, count_min + 1))
    kross_flag = False
    kross_flag1 = False
    fitness = np.sort(ga_instance.last_generation_fitness)[::-1]

    for kross_number in np.random.permutation(np.arange(1, detail_number + 1)):
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
    '''
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].imshow(parent1)
    axs[1, 0].imshow(parent2)
    axs[0, 1].imshow(offspring1)
    axs[1, 1].imshow(offspring2)
    plt.show()
    '''
    # print(kross_flag, kross_flag1)
    offspring1_resh = offspring1.reshape((-1,))
    offspring2_resh = offspring2.reshape((-1,))

    # f1 = ga_instance.fitness_func(offspring1_resh, 0)
    # f2 = ga_instance.fitness_func(offspring2_resh, 0)
    # new_gen = np.concatenate((parents, offspring1.reshape(1,-1), offspring2.reshape(1,-1)))
    # fitness = np.sort(ga_instance.last_generation_fitness)[::-1]
    # fitness = np.concatenate((fitness, [f1, f2]))
    # print(fitness)
    ind = np.argsort(fitness)[::-1]
    fitness_sort = fitness[ind]
    new_gen = new_gen[ind, :]
    offspring = new_gen[:offspring_size[0], :]
    return offspring

def mutation_func(offspring, ga_instance):
    new_offspring = []

    for i in offspring:
        solution_idx = 0
        offspring1 = i.reshape(N,N)
        mutation_flag = False
        while mutation_flag == False:
            if fitness_func(i, solution_idx) < 1 / (delta + 0.1 * desired_square_percent * Full_sq):
                a, mut_offspring1, mutation_flag = mutation.weak_mutation(offspring1, N)
            else:
                a, mut_offspring1, mutation_flag = mutation.mutation(offspring1, N)
            mut_offspring1_resh = mut_offspring1.reshape((-1,))
            # print('a')

            # a, mut_offspring1, mutation_flag = mutation.mutation(offspring1, N)
        mut_offspring1_resh = mut_offspring1.reshape((-1,))
        # print(mutation_flag)
        new_offspring.append(mut_offspring1_resh)
        # solution_idx += 1
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
                # t = round((1/ga_instance.last_generation_fitness[i*n + j] - delta)/ Full_sq, 5)
                fit = 1000 * round(ga_instance.last_generation_fitness[i*n + j], 8)
                axs[i, j].set_title(f'{fit}')
                [axi.set_axis_off() for axi in axs.ravel()]
    plt.suptitle(f'step {step_count}')
    #plt.show()
    plt.tight_layout()
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


def on_start(ga_instance):
    fig, axs = plt.subplots(n, n)
    for i in range(n):
        for j in range(n):
            if (i * n + j) < pop_size:
                vector = ga_instance.initial_population[i * n + j - 1]
                axs[i, j].imshow(vector.reshape((N, N)))
                [axi.set_axis_off() for axi in axs.ravel()]
    plt.suptitle(f'step {step_count}')
    #plt.show()
    plt.tight_layout()
    plt.savefig(f'{gen_plotpath}/plot_{step_count}')
    plt.clf()





ga_instance = pygad.GA(num_generations = 10000,
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
                       on_start = on_start,
                       parallel_processing=5)


ga_instance.run()
# best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()
# print(best_solution.reshape(N, N))
# print(best_solution_fitness)
# print(ga_instance.initial_population)
# print(ga_instance.population)

