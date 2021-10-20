import random


class TravelingSalesperson:
    def __init__(self, population_size, mutation_rate, cities):
        self.mutation_rate, self.population_size = mutation_rate, population_size
        self.population, self.best_route = None, None

        with open('european_cities.csv') as infile:  # Open's CSV file with data
            # Create´s a list of the cities
            self.cities = infile.readline().split(';')[:cities]
            # Create´s a dict where the city is the key and the city´s index is it´s value
            self.cities_keys = {self.cities[i]: i for i in range(len(self.cities))}
            # Storing the distances between the cities
            self.distances = [distance.split(';')[:len(self.cities)] for distance in infile.readlines()]
        infile.close()

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
        children = []
        numbers = [i for i in range(0, len(self.cities))]
        breeding_pool = random.sample(breeding_pool, len(breeding_pool))

        for i in range(len(breeding_pool)):
            parent1 = breeding_pool[i]
            parent2 = breeding_pool[len(breeding_pool) - i - 1]

            if parent2.fitness > parent1.fitness:  # setting highest fitness parent to parent1
                parent1, parent2 = parent2, parent1

            start = random.choice(numbers)
            end = random.choice(numbers)

            if start > end:
                start, end = end, start

            if end - start < len(self.cities) / 2:  # Switches parent so that highest parent have the most effect
                parent1, parent2 = parent2, parent1

            child = parent1.route[start:end]
            for city in parent2.route:
                if city not in child:
                    child.append(city)

                if len(child) == len(parent2.route):
                    break

            children.append(child)

        return children

    def mutate_population(self, population):
        numbers = [i for i in range(0, len(self.cities))]
        for route in population:
            odds = random.random()
            if odds < self.mutation_rate:  # random switch places on 2 cities
                city1 = random.choice(numbers)
                city2 = random.choice(numbers)

                while city1 == city2:
                    city2 = random.choice(numbers)

                route[city1], route[city2] = route[city2], route[city1]

        return population

    def next_generation(self):
        breeding_pool = self.selection()
        new_generation = self.mutate_population(self.breed_population(breeding_pool))
        new_population = []

        for route in new_generation:
            route = Route(route, self.cities_keys, self.distances)
            new_population.append(route)
            if route.distance < self.best_route.distance:
                self.best_route = route

        return new_population

    def evolve(self, generations):
        for i in range(0, generations):
            self.population = self.next_generation()


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

if __name__ == "__main__":
    tsp = TravelingSalesperson(population_size=50, mutation_rate=0.1, cities=10)
    tsp.init_population(100)
    tsp.evolve(10)
    print(tsp.best_route)
