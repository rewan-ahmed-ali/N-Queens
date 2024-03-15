#rewan ahmed abdelghfar ali
import random
import numpy as np
def uniform_crossover(parent1, parent2, pc=0.70):
    if len(parent1) != len(parent2):
        raise ValueError("Parents must be the same length")
    child1 = []
    child2 = []
    for i in range(len(parent1)):
        if random.random() < pc:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1, child2

def Single_Point_Crossover(parent1,parent2,Pc):
    P_crossover = np.random.random()    
    if P_crossover < Pc :
            point = np.random.randint(1,8)
            child1 = np.concatenate([parent1[ : point] , parent2[point: ]])
            child2 = np.concatenate([parent2[ : point] , parent1[point : ]])
    else :
            child1 = parent1.copy()
            child2 = parent2.copy()    
    return child1 , child2

def Three_Parent_Crossover(parent1 , parent2 , parent3 , Pc ) :
    P_crossover = np.random.random()
    child = []
    if P_crossover < Pc :
            for i in range (8):
                if parent1[i] == parent2[i]:
                    child.append(parent1[i])
                else :
                    child.append(parent3[i])                   
    else :
            child = parent1.copy()
    return child


def Two_Point_Crossover(parent1,parent2,Pc):
        
        P_crossover = np.random.random()
        if P_crossover < Pc :
                point1 = np.random.randint(1,4)
                point2 =np.random.randint(4,8)
                child1 = np.concatenate([parent1[ : point1] , parent2[point1:point2],parent1[point2:]])
                child2 = np.concatenate([parent2[ : point1] , parent1[point1:point2],parent2[point2:]])
        else :
                child1 = parent1.copy()
                child2 = parent2.copy()

        # print("crossover gene",point1 ,",", point2)
        # print(point1,point2)
        return child1 , child2

def PMX_Crossover(parent1, parent2,pc):
    n = len(parent1)
    cut1 = random.randint(0, n-2)
    cut2 = random.randint(cut1+1, n-1)
    offspring1 = [-1]*n
    offspring2 = [-1]*n
    for i in range(cut1, cut2):
        offspring1[i] = parent1[i]
        offspring2[i] = parent2[i]
    for i in range(n):
        if i < pc or i >= pc:
            while parent2[i] in offspring1[cut1:cut2]:
                i = np.where(parent1 == parent2[i])[0][0]
            offspring1[i] = parent2[i]
            while parent1[i] in offspring2[cut1:cut2]:
                i = np.where(parent2 == parent1[i])[0][0]
            offspring2[i] = parent1[i]
            
    return offspring1, offspring2



def ox_crossover(parent1, parent2):
    n = len(parent1)
    cut1 = random.randint(0, n-2)
    cut2 = random.randint(cut1+1, n-1)
    offspring1 = np.full(n, -1)
    offspring2 = np.full(n, -1)
    # copy the selected segment from the first parent
    offspring1[cut1:cut2] = parent1[cut1:cut2]
    offspring2[cut1:cut2] = parent2[cut1:cut2]
    # fill in the remaining positions in offspring1
    sequence = cut2
    for i in range(n):
        if parent2[i] not in offspring1:
            offspring1[sequence] = parent2[i]
            sequence = (sequence + 1) % n
    # fill in the remaining positions in offspring2
    sequence = cut2
    for i in range(n):
        if parent1[i] not in offspring2:
            offspring2[sequence] = parent1[i]
            sequence = (sequence + 1) % n
    print(offspring1)
    print(offspring2)


def cycle_crossover(parent1, parent2):
    n = len(parent1)
    offspring1 = np.full(n, -1)
    offspring2 = np.full(n, -1)
    # select a random starting position
    pos = random.randint(0, n-1)
    # loop until we complete a cycle
    while offspring1[pos] == -1:
        # copy the corresponding values from the parents
        offspring1[pos] = parent1[pos]
        offspring2[pos] = parent2[pos]
        # find the corresponding position in the other parent
        index = np.where(parent1 == parent2[pos])[0]
        if len(index) > 0:
            index = index[0]
            # switch parents and continue the cycle
            pos = index
            parent1, parent2 = parent2, parent1
        else:
            # if parent2[pos] is not present in parent1, choose a random position
            pos = random.randint(0, n-1)
            # reset the offspring arrays
            offspring1 = np.full(n, -1)
            offspring2 = np.full(n, -1)
    return offspring1, offspring2    
parent1=[0,1,0,1,0,1]
parent2=[1,0,1,0,1,1]
parent3=[0,0,1,0,1,0]
child  = uniform_crossover(parent1 ,parent2 , pc=0.70)
print(child)

child1 ,child2 = Single_Point_Crossover(parent1 ,parent2 , Pc=0.70)
print('crossover')
print(parent1,'-->',child1)
print(parent2,'-->',child2)

child3 ,child4 =Two_Point_Crossover(parent1 ,parent2 , Pc=0.70)
print('crossover')
print(parent1,'-->',child3)
print(parent2,'-->',child4)