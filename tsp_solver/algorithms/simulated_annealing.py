import random
import math

def calculate_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[i + 1]]
        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def swap(route):
    new_route = route[:]
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def solve_tsp(cities, temp=1000, cooling_rate=0.995, max_iterations=1000):
    num_cities = len(cities)
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = calculate_distance(current_route, cities)

    while temp > 1:
        for _ in range(max_iterations):
            new_route = swap(current_route)
            new_distance = calculate_distance(new_route, cities)

            # Accept if better or probabilistically accept worse solution
            if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temp):
                current_route, current_distance = new_route, new_distance

        temp *= cooling_rate  # Reduce temperature

    return current_route, current_distance
