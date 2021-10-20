class TravelingSalesperson:
    def __init__(self, population_size, generations, mutationRate, init_population, cities):
        self.mutationRate, self.generations = mutationRate, generations
        self.population_size, self.best_route, self.init_population = population_size, None, init_population

    def init_population(self, population_size):
        pass

    def selection(self):
        pass

    def breed_population(self, breeding_pool):
        pass

    def mutate_population(self, population):
        pass

    def next_generation(self):
        pass
