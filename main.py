'''
The Knapsack Problem:
Given a set of items with specific values and sizes,
select a subset of items to fit into a container while maximizing the total value of the items selected, without exceeding the container's capacity.
'''
import random
import math
import matplotlib.pyplot as plt

def generate_chart(file_path):
    population_evaluations = []
    best_individuals = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                population, best = map(float, line.split())
                population_evaluations.append(population)
                best_individuals.append(best)

    iterations = list(range(1, len(population_evaluations) + 1))

    plt.figure(figsize=(10, 6))

    plt.plot(iterations, population_evaluations, marker='o', linestyle='-', color='b', label='Population Evaluation')

    plt.xlabel('Population Evaluation')
    plt.ylabel('Values')
    plt.title('Iterations vs Population Evaluation')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Display the plot
    plt.savefig('population_fitness.png')


    ######################

    plt.figure(figsize=(10, 6))
    plt.plot(iterations, best_individuals, marker='o', linestyle='-', color='r', label='Best Individual')

    plt.xlabel('Best Individual Evaluation')
    plt.ylabel('Values')
    plt.title('Iterations vs Best Individual Evaluation')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig('best_individual_fitness.png')

def generate_items(n):
    items = []
    for i in range(n):
        print(i)
        items.append({"value": i, "weight": i})
    return items

def calculate_fitness(candidate, items, capacity):
    total_value = 0
    total_weight = 0

    for i in range(len(candidate)):
        if candidate[i] == '1':
            total_value += items[i]['value']
            total_weight += items[i]['weight']

    if total_weight < capacity:
        return total_value
    else:
        return 0

def initialize_chromossome(number_of_items):
    return ''.join(random.choice('01') for _ in range(number_of_items))

def initialize_population(population, size, number_of_items):
    for _ in range(size):
        chromosome = initialize_chromossome(number_of_items)
        population.append(chromosome)

def select_parent(evaluation_table, total):
    pick = random.uniform(0, total)    
    current = 0
    for candidate in evaluation_table:
        current += evaluation_table[candidate]
        if current >= pick:
            return candidate

def single_point_crossover(parent_1, parent_2, number_of_items):
    crossover_point = random.randint(1, (number_of_items) - 1)
    
    parent_1_left = parent_1[:crossover_point]
    parent_1_right = parent_1[-((number_of_items) - crossover_point):]
    parent_2_left = parent_2[:crossover_point]
    parent_2_right = parent_2[-((number_of_items) - crossover_point):]

    son_1 = parent_1_left + parent_2_right
    son_2 = parent_2_left + parent_1_right

    return random.choice([son_1, son_2])

def mutation(son, chance):
    son = list(son)
    for i in range(len(son)):
        num = random.uniform(0, 1)
        if num < chance:
            son[i] = str(random.randint(0, 1))
    return ''.join(son)
    
def main():
    with open("run.txt", "w") as f:
        capacity = 5050
        # Creating the first generation population (or pool) of candidate solutions (solutions are also called: individuals, creatures, specimens, organisms or phenotypes)
        number_of_items = 100
        items = generate_items(number_of_items)
        population_size = 1000

        population = []
        initialize_population(population, population_size, number_of_items)

        for _ in range(200):
            evaluation_table = {}
            
            for candidate in population:
                fitness = calculate_fitness(candidate, items, capacity)
                evaluation_table[candidate] = fitness

            total = 0
            for candidate in evaluation_table:
                total += evaluation_table[candidate]

            f.write(str(total) + ' ' + str(evaluation_table[max(evaluation_table, key=evaluation_table.get)]) + '\n')

            new_population = []
            for _ in range(population_size):
                parent_1 = select_parent(evaluation_table, total)
                parent_2 = select_parent(evaluation_table, total)

                son = single_point_crossover(parent_1, parent_2, number_of_items)
                son = mutation(son, 0.01)
                new_population.append(son)

            population = new_population
    
    f.close()

    maximum = max(evaluation_table, key=evaluation_table.get)
    print(maximum)

    generate_chart('./run.txt')


if __name__ == "__main__":
    main()
