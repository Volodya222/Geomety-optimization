import geomety_test as gt
import numpy as np
import copy
from matplotlib import pyplot as plt
import pygad
import krossingover
import mutation
import ground
# import main_comsol as mc

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


pop_size = 5
initial_population = []
counting_list = []
for i in range(pop_size):
    count_i = 0
    while count_i < 2:

        x_i = np.random.randint(0, 2, (N, N))
        x1_i = gt.smooth(x_i)
        y_i, count_i = gt.parts(x1_i)
        y_ig = ground.ground_test(y_i, rad_ground, N)
        y_ig, count_i = gt.parts(y_ig)
    counting_list.append(count_i)
    y_inum=y_ig.reshape((-1,))

    initial_population.append(y_inum)

print(initial_population)



def fitness_func(solution, solution_idx):
    # vector_cap = mc.capacitance(solution.reshape(N, N), radius)
    # a = np.random.random(3)
    # fitness = 1.0 / (0.000001 + np.sqrt((vector_cap[0]-c11)**2) + np.sqrt((vector_cap[1]-c12)**2) + np.sqrt((vector_cap[2]-c22)**2))
    return hash(solution.tostring)

    def steady_state_selection(self, fitness, num_parents):

        """
        Selects the parents using the steady-state selection technique. Later, these parents will mate to produce the offspring.
        It accepts 2 parameters:
            -fitness: The fitness values of the solutions in the current population.
            -num_parents: The number of parents to be selected.
        It returns an array of the selected parents.
        """

        fitness_sorted = sorted(range(len(fitness)), key=lambda k: fitness[k])
        fitness_sorted.reverse()
        # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
        if self.gene_type_single == True:
            parents = numpy.empty((num_parents, self.population.shape[1]), dtype=self.gene_type[0])
        else:
            parents = numpy.empty((num_parents, self.population.shape[1]), dtype=object)
        for parent_num in range(num_parents):
            parents[parent_num, :] = self.population[fitness_sorted[parent_num], :].copy()

        return parents, fitness_sorted[:num_parents]


def crossover_func(parents, offspring_size, ga_instance):
    print(offspring_size, '111')
    offspring = []
    parent1 = parents[0].reshape(N, N)
    parent2 = parents[1].reshape(N, N)
    offspring1, offspring2 = krossingover.krossingover(parent1, parent2, N)
    offspring1_resh = offspring1.reshape((-1,))
    offspring2_resh = offspring2.reshape((-1,))
    offspring.append(offspring1_resh)
    offspring.append(offspring2_resh)
    offspring.append(parents[0])
    offspring.append(parents[1])

    return np.array(offspring)

def mutation_func(offspring, ga_instance):
    new_offspring = []
    for i in offspring:
        offspring1 = i.reshape(N,N)
        mut_offspring1 = mutation.mutation(offspring1, N)
        mut_offspring1_resh = mut_offspring1.reshape((-1,))

        new_offspring.append(mut_offspring1_resh)
    return offspring
    # return np.array(new_offspring)

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
    plt.show()

def on_crossover(ga_instance, offspring):
    index_del = np.ones((ga_instance.population.shape[0]))

    for i in range(len(ga_instance.population) - 1):
        for j in range(i, len(ga_instance.population)):
            if (ga_instance.population[i] == ga_instance.population[j]).all():
                index_del[j] = 0
                break
    index_del = np.asarray(index_del, dtype=bool)

    ga_instance.population = ga_instance.population[index_del, :]







ga_instance = pygad.GA(num_generations = 3,
                    fitness_func = fitness_func,
                    num_parents_mating=2,
                    initial_population = initial_population,
                       # offspring_size = 2,
                    crossover_type = crossover_func,
                    mutation_type = mutation_func,
                    parent_selection_type="sss",
                       # save_best_solutions=True,
                       # stop_criteria = ["reach_500000"],
                       on_generation = on_generation,
                       on_crossover = on_crossover)


ga_instance.run()
best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()
print(best_solution.reshape(N, N))
print(best_solution_fitness)
# print(ga_instance.initial_population)
# print(ga_instance.population)

