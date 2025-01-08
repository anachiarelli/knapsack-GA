'''
The Knapsack Problem:
Given a set of items with specific values and sizes,
select a subset of items to fit into a container while maximizing the total value of the items selected, without exceeding the container's capacity.
'''
import random

# Generating items:
def generate_items(n):
    items = []
    for i in range(n + 1):
        items.append({"value": i, "weight": i})
    return items

# Creating a random generation:
def generate_population(population_size, genes, n):
    population = []
    for _ in range (population_size + 1):
        # The chromossome (or genome) encodes a solution. The encoding for this problem are binary strings made of the possible genes: 0 or 1.
        genome = []
        for _ in range(n):
            genome.append(random.choice(genes))
        population.append({"genome": genome, "fitness": None})
    return population

# A fitness function evaluates the quality of a solution, with higher values representing better solutions.
# In this problem, the fitness function returns: if the total weight of items is lesser or equal to the capacity of the container: the sum of values of the selected items, else: 0 
def calculate_fitness(genome, items, capacity):
    total_value = 0
    total_weight = 0
    for i in range(len(genome)):
        if genome[i]:
            total_value += items[i]["value"]
            total_weight += items[i]["weight"]
    
    if total_weight <= capacity:
        return total_value
    else:
        return 0
    

capacity = 20
# Creating the first generation population (or pool) of candidate solutions (solutions are also called: individuals, creatures, specimens, organisms or phenotypes)
number_of_items = 10
items = generate_items(number_of_items)

population_size = 10
# The gene represents a parameter. In this problem, the possible gene values are: 1, indicating that the corresponding item is part of the selected set, or 0, indicating that the item is not included.
genes = [0, 1]

population = generate_population(population_size, genes,number_of_items)
print(population)

for solution in population:
    solution["fitness"] = calculate_fitness(solution["genome"], items, capacity)
    print(solution)