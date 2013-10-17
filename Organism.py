from copy import deepcopy
import random

class Organism:
    genome = None
    fitness = None
    
    def __init__(self,genome=None):
        if genome:
            self.genome = deepcopy(genome)
    
    def mutate(self,gene_range,mutate_max):
        ''' Return a mutated organism '''
        c = self.copy()
        for i in range(len(c.genome)):
            if random.random() < 0.1:
                if random.random() < 0.5:
                    c.genome[i] += int(random.uniform(0,mutate_max))
                    if c.genome[i] > gene_range[1]:
                        c.genome[i] = gene_range[1]
                else:
                    c.genome[i] -= int(random.uniform(0,mutate_max))
                    if c.genome[i] < gene_range[0]:
                        c.genome[i] = gene_range[0]
        return c
    
    def crossover(self,organism):
        ''' Return an organism that is a crossover between this organism and the provided organism '''
        c = self.copy()
        for i in range(len(c.genome)):
            if random.random() > 0.5:
                c.genome[i] = organism.genome[i]
        return c
    
    def calculate_fitness(self,target,div_by_two=False):
        ''' Calculate the fitness of this organism '''
        f = 0
        for i in range(len(self.genome)):
            if div_by_two:
                f += (self.genome[i]/2 - target[i]/2)**2
            else:
                f += (self.genome[i] - target[i])**2
        self.fitness = f
    
    def copy(self):
        c = Organism()
        c.genome = deepcopy(self.genome)
        return c
