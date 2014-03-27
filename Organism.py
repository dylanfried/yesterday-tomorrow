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
            note = c.genome[i][0]
            time = c.genome[i][1]
            # Note
            if random.random() < 0.1:
                if random.random() < 0.5:
                    note += int(random.uniform(-mutate_max,mutate_max))
                    if note > gene_range[1]:
                        note = gene_range[1]
                    if note < gene_range[0]:
                        note = gene_range[0]
            # time
            if random.random() < 0.1:
                if random.random() < 0.5:
                    time *= 2
                else:
                    time /= 2
                if random.random() < 0.5:
                    time *= -1
                if time > 32:
                    time = 32
                elif time < -32:
                    time = -32
                elif time == 0:
                    time = 1
            c.genome[i] = (note,time)
        return c
    
    def crossover(self,organism):
        ''' Return an organism that is a crossover between this organism and the provided organism '''
        c = self.copy()
        for i in range(len(c.genome)):
            if random.random() > 0.5:
                c.genome[i] = organism.genome[i]
        return c
    
    def onepointcrossover(self,organism):
        inflection_point = random.randint(0,len(organism.genome)-1)
        
        c1 = self.copy()
        c2 = organism.copy()
        
        genome1 = c1.genome[:inflection_point] + c2.genome[inflection_point:]
        genome2 = c2.genome[:inflection_point] + c1.genome[inflection_point:]
        
        c1.genome = genome1
        c2.genome = genome2
        
        return [c1,c2]
    
    def calculate_fitness(self,target,other_genomes=None):
        ''' Calculate the fitness of this organism '''
        f = 0
        for i in range(len(self.genome)):
            f += (self.genome[i][0] - target[i][0])**2
            f += (self.genome[i][1] - target[i][1])**2
        if other_genomes:
            for other_genome in other_genomes:
                for i in range(len(self.genome)):
                    if abs(self.genome[i][0] - other_genome[i][0]) in [2, 4, 5, 7, 9, 11]:
                        f -= 50
                        
        self.fitness = f
    
    def copy(self):
        c = Organism()
        c.genome = deepcopy(self.genome)
        return c
