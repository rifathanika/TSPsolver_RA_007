import heapq
from itertools import permutations

def calculate_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[i + 1]]
        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def heuristic(route, cities):
    return calculate_distance(route, cities)

def solve_tsp(cities):
    num_cities = len(cities)
    initial_route = tuple(range(num_cities))
    frontier = [(heuristic(initial_route, cities), 0, initial_route)]
    visited = set()

    while frontier:
        _, current_cost, current_route = heapq.heappop(frontier)
        
        if current_route in visited:
            continue
        visited.add(current_route)

        if len(set(current_route)) == num_cities:  # If we visited all cities
            return current_route, calculate_distance(current_route, cities)

        for perm in permutations(current_route):
            if perm not in visited:
                new_cost = current_cost + heuristic(perm, cities)
                heapq.heappush(frontier, (new_cost, current_cost + 1, perm))

    return None, float('inf')  # If no route found
