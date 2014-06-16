from copy import deepcopy
import random
import numpy as np
from helpers import get_intervals,make_absolute

class Organism:
    genome = None
    fitness = None
    
    def __init__(self,genome=None):
        if genome:
            self.genome = deepcopy(genome)
        else:
            self.genome = []
    
    def random_genome(self,length):
        for i in range(length):
            note = random.randint(0,88)
            time = random.sample([8,4,2,1,-1,-2,-4,-8],1)[0]
            if random.random() > 0.8:
                note = 0
            self.genome.append((note,time))
    
    def mutate(self,gene_range,mutate_max):
        ''' Return a mutated organism '''
        c = self.copy()
        for i in range(len(c.genome)):
            note = c.genome[i][0]
            time = c.genome[i][1]
            # Note
            if random.random() < 0.1:
                if (note and random.random() < 0.8) or (not note and random.random() < 0.2):
                    note += int(random.uniform(-mutate_max,mutate_max))
                    if note > gene_range[1]:
                        note = gene_range[1]
                    if note < gene_range[0]:
                        note = gene_range[0]
                else:
                    note = 0
            # time
            if random.random() < 0.1:
                if random.random() < 0.5:
                    time *= 2
                else:
                    time /= 2
                if random.random() < 0.5:
                    time *= -1
                if time > 16:
                    time = 16
                elif time < -16:
                    time = -16
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
        ''' Calculate the fitness of this organism 
        
            To do this, loop over all of the time encompassed by the
            two melodies and reward ones that are similar at the same
            time.
        '''
        # First, make the melodies absolute times:
        self_absolute = make_absolute(self.genome)
        genomes_absolute = []
        genomes_absolute.append(make_absolute(target))
        if other_genomes:
            genomes_absolute += [make_absolute(genome) for genome in other_genomes]
        f = 0
        first = True
        for genome_absolute in genomes_absolute:
            self_index = 0
            target_index = 0
            absolute_time = 0
            while self_index < len(self.genome) and target_index < len(genome_absolute):
                if first or (self.genome[self_index][0] != 0 and genome_absolute[target_index][0] != 0):
                    f += (self.genome[self_index][0] - genome_absolute[target_index][0])**2
                #elif self.genome[self_index][0] != 0 or genome_absolute[target_index][0] != 0:
                #    f += 10
                absolute_time += 1.0/32.0
                if absolute_time > self_absolute[self_index][1]:
                    self_index += 1
                if absolute_time > genome_absolute[target_index][1]:
                    target_index += 1
            # Do special things for first melody because it is the true target
            first = False
        #if other_genomes:
        #    for other_genome in other_genomes:
        #        intervals1 = get_intervals([g[0] for g in self.genome])
        #        intervals2 = get_intervals([g[0] for g in other_genome])
        #        f -= 50*max(np.correlate(intervals1/np.linalg.norm(intervals1),intervals2/np.linalg.norm(intervals2)))
                        
        self.fitness = f
    
    def copy(self):
        c = Organism()
        c.genome = deepcopy(self.genome)
        return c
