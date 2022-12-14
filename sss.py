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
