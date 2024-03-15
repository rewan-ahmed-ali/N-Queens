import random

def cycle_crossover(parent1, parent2):
    # Initialize offspring with empty values
    offspring = [None] * len(parent1)
    # Select a random starting index
    start_idx = random.randint(0, len(parent1)-1)
    # Perform cycle crossover
    while None in offspring:
        # Copy values from parent 1
        if offspring[start_idx] is None:
            offspring[start_idx] = parent1[start_idx]
            idx = parent2.index(parent1[start_idx])
            while offspring[idx] is None:
                offspring[idx] = parent1[idx]
                idx = parent2.index(parent1[idx])
        # Copy values from parent 2
        else:
            start_idx = offspring.index(None)
            for value in parent2:
                if value not in offspring:
                    start_idx = parent2.index(value)
                    break
            idx = parent1.index(parent2[start_idx])
            while offspring[idx] is None:
                offspring[idx] = parent2[idx]
                idx = parent1.index(parent2[idx])
    return offspring
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
offspring = cycle_crossover(parent1, parent2)
print("cycle crossover")
print("Parent 1: {}".format(parent1))
print("Parent 2: {}".format(parent2))
print("Offspring: {}".format(offspring))





def order_crossover(parent1, parent2):
    # Select two random crossover points
    crossover_points = sorted(random.sample(range(len(parent1)), 2))
    # Create the offspring with the selected subset from parent 1
    offspring = parent1[crossover_points[0]:crossover_points[1]]
    # Fill in the remaining elements from parent 2 in order
    for i in range(len(parent2)):
        if parent2[i] not in offspring:
            if len(offspring) == len(parent1):
                break
            offspring.append(parent2[i])
    return offspring

parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
offspring = order_crossover(parent1, parent2)
print("ox crossover")
print("Parent 1: {}".format(parent1))
print("Parent 2: {}".format(parent2))
print("Offspring: {}".format(offspring))

def pmx_crossover(parent1, parent2):
    # Select two random crossover points
    crossover_points = sorted(random.sample(range(len(parent1)), 2))
    # Create the offspring with the selected subset from parent 1
    offspring = parent1[crossover_points[0]:crossover_points[1]]
    # Fill in the remaining elements from parent 2
    for i in range(len(parent2)):
        if parent2[i] not in offspring:
            if len(offspring) == len(parent1):
                break
            # Find the corresponding element from parent 1
            idx = parent2.index(parent1[i])
            while parent1[idx] in offspring:
                idx = parent2.index(parent1[idx])
            offspring.append(parent1[idx])
    return offspring

parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
offspring = pmx_crossover(parent1, parent2)
print("pmx crossover")
print("Parent 1: {}".format(parent1))
print("Parent 2: {}".format(parent2))
print("Offspring: {}".format(offspring))
