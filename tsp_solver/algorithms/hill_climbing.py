import random

def calculate_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[i + 1]]
        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def get_neighbors(route):
    neighbors = []
    for i in range(len(route) - 1):
        for j in range(i + 1, len(route)):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbors.append(new_route)
    return neighbors

def solve_tsp(cities, max_iterations=1000):
    num_cities = len(cities)
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = calculate_distance(current_route, cities)

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_route)
        best_neighbor = min(neighbors, key=lambda route: calculate_distance(route, cities))
        best_neighbor_distance = calculate_distance(best_neighbor, cities)

        if best_neighbor_distance < current_distance:
            current_route = best_neighbor
            current_distance = best_neighbor_distance
        else:
            break  # Stop if no improvement

    return current_route, current_distance
