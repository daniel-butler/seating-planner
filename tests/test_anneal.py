import math
import time

from numpy import random

from seating_planner import anneal


def test_annealer_with_traveling_salesman_problem():
    """Test annealer with a traveling salesman problem."""
    start = time.time()

    # List latitude and longitude (degrees) for the twenty largest U.S. cities
    cities = {
        'New York City': (40.72,74.00), 'Los Angeles': (34.05,118.25), 'Chicago': (41.88,87.63),
        'Houston': (29.77,95.38), 'Phoenix': (33.45,112.07), 'Philadelphia': (39.95,75.17),
        'San Antonio': (29.53,98.47), 'Dallas': (32.78,96.80), 'San Diego': (32.78,117.15), 'San Jose': (37.30,121.87),
        'Detroit': (42.33,83.05), 'San Francisco': (37.78,122.42), 'Jacksonville': (30.32,81.70),
        'Indianapolis': (39.78,86.15), 'Austin': (30.27,97.77), 'Columbus': (39.98,82.98), 'Fort Worth': (32.75,97.33),
        'Charlotte': (35.23,80.85), 'Memphis': (35.12,89.97), 'Baltimore': (39.28,76.62)
    }

    def distance(a, b):
        """Calculates distance between two latitude-longitude coordinates."""
        R = 3963  # radius of Earth (miles)
        lat1, lon1 = math.radians(a[0]), math.radians(a[1])
        lat2, lon2 = math.radians(b[0]), math.radians(b[1])
        return math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon1-lon2)) * R

    def route_move(state):
        """Swaps two cities in the route."""
        a = random.randint( 0, len(state)-1 )
        b = random.randint( 0, len(state)-1 )
        state[a], state[b] = state[b], state[a]

    def route_energy(state):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(state)):
            e += distance(cities[state[i-1]], cities[state[i]])
        return e

    # Start with the cities listed in random order
    state = list(cities.keys())
    random.shuffle(state)

    # Minimize the distance to be traveled by simulated annealing with a
    # manually chosen temperature schedule
    annealer = anneal.Annealer(route_energy, route_move)
    state, energy = annealer.anneal(state, 10000000, 0.01, 18000*len(state), 9)
    while state[0] != 'New York City':
        state = state[1:] + state[:1]  # rotate NYC to start

    print(f"{int(route_energy(state))} mile route")

    assert int(route_energy(state)) <= 6900

    for city in state:
        print("\t", city)

    # # Minimize the distance to be traveled by simulated annealing with an
    # # automatically chosen temperature schedule
    params_to_run_anneal = annealer.auto(state, 4)
    # while state[0] != 'New York City':
    #     state = state[1:] + state[:1]  # rotate NYC to start
    # print("%i mile route:" % route_energy(state))
    # for city in state:
    #     print("\t", city)

    print(f'Elapsed time: {time.time() - start}')