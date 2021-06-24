#solving TSP using genetic algorithm

import random , sys

#generates a random number between 1 and the number of cities minus 1.
def Rand_City(size):
    return random.randint(1, size-1)

#checks if a city was seen before of not.
def Is_New(Gene, city):
    for c in Gene:
        if c == city:
            return False
    
    return True

#find the fitness using the given matrix
def Find_Fitness(Gene, cities):
    fitness = 0
    for i in range(0, len(Gene)-1):
        if cities[Gene[i]][Gene[i+1]] == 0:
            return sys.maxint
        else:
            fitness += cities[Gene[i]][Gene[i+1]]

    return fitness

#generates a Gene randomly or generates a path randomly
def Create_Gene(size):
    Gene = [0]
    for i in range(size-1):
        while True:
            new_city = Rand_City(size)
            if Is_New(Gene, new_city):
                Gene += [new_city]
                break
    
    Gene += [0]

    return Gene

#gets 2 cities and swap them to make a mutation.
def Mutation(Gene, size):
    change1 = Rand_City(size)
    change2 = Rand_City(size)
    if change1 > change2:
        temp = change1
        change1 = change2
        change2 = temp
    if change1 != change2 :
        temp = Gene[change1]
        Gene[change1] = Gene[change2]
        Gene[change2] = temp

    return Gene

#checks if the best fitness has changes during the last N times
def Do_it(last_costs):
    if last_costs[-1] == 0:
        return True
    for i in range(len(last_costs)-1):
        if last_costs[i] != last_costs[i+1]:
            return True
    
    return False

#append the best fitness to the list of last best fitnesses
def Append_Cost(last_costs, new_cost):
    prev = new_cost
    for i in range(len(last_costs)):
        new = last_costs[i]
        last_costs[i] = prev
        prev = new 


def TSP(cities, size, number_of_first_population, N, end_point):
    Population = []
    #generate the first population
    for _ in range(number_of_first_population):
        Gene = Create_Gene(size)
        Fitness = Find_Fitness(Gene, cities)
        Population.append((Gene,Fitness))

    Population.sort(key=lambda x:x[1])
    Population = Population[:(len(Population)*N)/100+1]
    print("Best initial population:")    
    print(Population[0][0])
    print("Cost:")
    print(Population[0][1])

    generation = 2
    #lasts_costs save the last N generation's best fitness
    last_costs = []
    for _ in range(end_point):
        last_costs.append(0)
    #append the fitness of the first generation to last_costs
    last_costs[0] = Population[0][1]

    #repeats untill the best fitness does not change for N times
    while(Do_it(last_costs)):
        new_population = Population
        #make a mutation in each parent and consider them as a child and append them to the generation
        for i in range(len(new_population)):
            new_gene = Mutation(new_population[i][0][:], size)
            new_fitness = Find_Fitness(new_gene, cities)

            Population.append((new_gene, new_fitness))
        
        #sort the generation by the fitness
        Population.sort(key=lambda x:x[1])
        #choose the N% of best fitnesses
        Population = Population[:(len(Population)*N)/100 + 1]

        print("generation number: ", generation)
        print("best population:")    
        print(Population[0][0])
        print("cost:")
        print(Population[0][1])
        Append_Cost(last_costs, Population[0][1])
        generation += 1


size = 20
cities = [
    [0,15,34,56,33,24,83,67,54,97,23,80,73,39,98,64,12,65,17,33],
    [15, 0,17,28,60, 5,39,74,16,12,96,74,24,28,41,59,58,53,33,48],
    [34,17, 0,18,10,40,15,27,89,50,40,75,72,49,33,43,86,67,65, 5],
    [56,28,18, 0,59,65,67, 9,20,68,84,33,90,26,47,34,10,58,83,26],
    [33,60,10,59, 0,84,40,31,44, 6,23,52,35,74,91,75,53,64,49,36],
    [24, 5,40,65,84, 0,59,52,53,75, 2,68,53,37,38,39,56,46,62,99],
    [83,39,15,67,40,59, 0,65,10,24,92,81,65,71,83,45,83,20, 7,84],
    [67,74,27, 9,31,52,65, 0,98,88,47,53,67,63,13,67,84,50,99,56],
    [54,16,89,20,44,53,10,98, 0,14, 6,65,20,66,97,94,18,10,89,47],
    [97,12,50,68, 6,75,24,88,14, 0,69,42,24,52,38,26,42,92,65,14],
    [23,96,40,84,23, 2,92,47, 6,69, 0,86,51,74,79,29,40,13,84,94],
    [80,74,75,33,52,68,81,53,65,42,86, 0,31, 9,72,15,88,81,56,55],
    [73,24,72,90,35,53,65,67,20,24,51,31, 0,18,39,25,60,59,38,92],
    [39,28,49,26,74,37,71,63,66,52,74, 9,18, 0,84, 2,47,20,27,98],
    [98,41,33,47,91,38,83,13,97,38,79,72,39,84, 0,89,87,43,87,66],
    [64,59,43,34,75,39,45,67,94,26,29,15,25, 2,89, 0,27,88,87,43],
    [12,58,86,10,53,56,83,84,18,42,40,88,60,47,87,27, 0,88,34,21],
    [65,53,67,58,64,46,20,50,10,92,13,81,59,20,43,88,88, 0,86,86],
    [17,33,65,83,49,62, 7,99,89,65,84,56,38,27,87,87,34,86, 0,79],
    [33,48, 5,26,36,99,84,56,47,14,94,55,92,98,66,43,21,86,79, 0]
    ]
number_of_first_population = size*2
N = 50 #N%  of the best fitnesses will be chosen
end_point = 100 #after 100 times that th best fitness didn't change it it will end
TSP(cities, size, number_of_first_population, N, end_point)