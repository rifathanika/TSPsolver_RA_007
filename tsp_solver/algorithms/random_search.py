import random
import itertools

def calculate_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[i + 1]]
        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def solve_tsp(cities, iterations=1000):
    num_cities = len(cities)
    best_route = list(range(num_cities))
    best_distance = float('inf')

    for _ in range(iterations):
        random_route = random.sample(best_route, num_cities)
        distance = calculate_distance(random_route, cities)
        
        if distance < best_distance:
            best_distance = distance
            best_route = random_route

    return best_route, best_distance
