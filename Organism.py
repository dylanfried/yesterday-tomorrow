from copy import deepcopy
import random

class Organism:
    genome = None
    fitness = None
    
    def __init__(self,genome=None):
        if genome:
            self.genome = deepcopy(genome)
    
    def mutate(self):
        ''' Return a mutated organism '''
        c = self.copy()
        for i in range(len(c.genome)):
            if random.random() < 0.1:
                if random.random() < 0.5:
                    c.genome[i] += int(random.uniform(0,10))
                    if c.genome[i] > 88:
                        c.genome[i] = 88
                else:
                    c.genome[i] -= int(random.uniform(0,10))
                    if c.genome[i] < 1:
                        c.genome[i] = 1
        return c
    
    def crossover(self,organism):
        ''' Return an organism that is a crossover between this organism and the provided organism '''
        c = self.copy()
        for i in range(len(c.genome)):
            if random.random() > 0.5:
                c.genome[i] = organism.genome[i]
        return c
    
    def calculate_fitness(self,target):
        ''' Calculate the fitness of this organism '''
        f = 0
        for i in range(len(self.genome)):
            f += (self.genome[i] - target[i])**2
        self.fitness = f
    
    def copy(self):
        c = Organism()
        c.genome = deepcopy(self.genome)
        return c
