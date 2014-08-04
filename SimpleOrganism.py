from copy import copy
import random
import numpy as np
from helpers import get_intervals,make_absolute,SYLLABLES,counter_cosine_similarity,get_weighted
import collections
import time
import math

class SimpleOrganism:
    genome = None
    fitness = None
    target = None
    
    def __init__(self,genome=None,target_genome=None,population=None):
        self.population = population
        if genome:
            self.genome = copy(genome)
        else:
            self.genome = []
        self.target = target_genome
    
    def random_genome(self,length):
        self.genome = copy(self.population.start_melody)
        return
    
    def mutate(self,gene_range,mutate_max):
        ''' Return a mutated organism '''
        c = self.copy()
        i = 0
        while i < len(c.genome):
            note = c.genome[i][0]
            time = c.genome[i][1]
            syllable = c.genome[i][2]
            # Add note?
            if random.random() < 0.005:
                # How many to insert?
                insert = 1
                c.genome.insert(i,(random.randint(19,88),random.sample([-16,-8,-4,-2,-1,1,2,4,8,16],1)[0],random.sample(SYLLABLES,1)[0]))
                i += 1
                if i >= len(c.genome):
                    break
            # Remove note?
            elif random.random() < 0.005 and i > 0:
                c.genome.pop(i-1)
                i -= 1
                if i >= len(c.genome):
                    break
            # Note
            elif random.random() < 0.005:
                if (note and random.random() < 0.85) or (not note and random.random() < 0.15):
                    note += int(random.uniform(-mutate_max,mutate_max))
                    if note > gene_range[1]:
                        note = gene_range[1]
                    if note < gene_range[0]:
                        note = gene_range[0]
                else:
                    note = 0
            # time
            elif random.random() < 0.005:
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
            # Syllable
            if note == 0:
                syllable = []
            c.genome[i] = (note,time,syllable)
            i += 1
        return c
    
    def crossover(self,organism):
        ''' Return an organism that is a crossover between this organism and the provided organism '''
        c1 = self.copy()
        c2 = organism.copy()
        for i in range(min(len(c1.genome),len(c2.genome))):
            if random.random() < 0.3:
                c1.genome[i] = organism.genome[i]
                c2.genome[i] = self.genome[i]
        return [c1,c2]
    
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
        
            Just a simple sum of squared distances for notes and for times
        '''
        fitness = 0
        for i in range(max(len(target),len(self.genome))):
            note1 = self.genome[i][0] if i < len(self.genome) else 0
            note2 = target[i][0] if i < len(target) else 0
            fitness += (note1-note2)**2
            time1 = self.genome[i][1] if i < len(self.genome) else 0
            time2 = target[i][1] if i < len(target) else 0
            fitness += (time1-time2)**2
        self.fitness = fitness
    
    def copy(self):
        c = SimpleOrganism()
        c.genome = copy(self.genome)
        c.target = self.target
        c.population = self.population
        return c
