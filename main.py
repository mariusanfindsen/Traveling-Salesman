class TravelingSalesperson:
    def __init__(self, population_size, generations, mutation_rate, init_population, cities):
        self.mutation_rate, self.generations = mutation_rate, generations
        self.population_size, self.best_route, self.init_population = population_size, None, init_population

        with open('european_cities.csv') as infile:  # Open's CSV file with data
            # Create´s a list of the cities
            self.cities = infile.readline().split(';')[:cities]
            # Create´s a dict where the city is the key and the city´s index is it´s value
            self.cities_keys = {self.cities[i]: i for i in range(len(self.cities))}
            # Storing the distances between the cities
            self.distances = [distance.split(';')[:len(self.cities)] for distance in infile.readlines()]
        infile.close()

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
