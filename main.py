import random


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

        self.population = self.init_population(init_population)

    def init_population(self, population_size):
        random.shuffle(self.cities)  # random route
        routes = [Route(self.cities.copy(), self.cities_keys, self.distances)]
        self.best_route = routes[0]

        for i in range(1, population_size):
            while True:
                random.shuffle(self.cities)  # random route
                route = Route(self.cities.copy(), self.cities_keys, self.distances)  # creating instance route

                if route not in routes:
                    break

            routes.append(route)

            if route.distance < self.best_route.distance:
                self.best_route = route

        return routes

    def selection(self):
        selection_pool = sorted(self.population, key=lambda route: route.fitness, reverse=False)
        total = sum(route.fitness for route in selection_pool)

        selection_pool[0].proportion = selection_pool[0].fitness / total
        for i in range(1, len(selection_pool)):
            selection_pool[i].proportion = (selection_pool[i].fitness / total) + selection_pool[i - 1].proportion

        breeding_pool = []
        while len(breeding_pool) <= self.population_size:
            choice = random.random()
            if choice < selection_pool[1].proportion and selection_pool[0] not in breeding_pool:
                breeding_pool.append(selection_pool[0])
            else:
                for i in range(1, len(selection_pool)):
                    if selection_pool[i - 1].proportion <= choice and selection_pool[i] not in breeding_pool:
                        breeding_pool.append(selection_pool[i])
                        break

        return breeding_pool

    def breed_population(self, breeding_pool):
        pass

    def mutate_population(self, population):
        pass

    def next_generation(self):
        pass


class Route:
    def __init__(self, cities, cities_keys, distances):
        self.route = cities
        self.distance = self.calculate_distance(cities_keys, distances)
        self.fitness = 1 / self.distance
        self.proportion = None

    def calculate_distance(self, cities_keys, distances):
        length = 0
        for i in range(1, len(self.route)):
            length += float(distances[cities_keys[self.route[i - 1]]][cities_keys[self.route[i]]])
        length += float(distances[cities_keys[self.route[-1]]][cities_keys[self.route[0]]])

        return length
