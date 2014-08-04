from copy import copy
import random
import numpy as np
from helpers import get_intervals,make_absolute,SYLLABLES,counter_cosine_similarity,get_weighted
import collections
import time

class Organism:
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
        for i in range(length):
            self.genome.append(self.population.start_melody[random.randint(0,len(self.population.start_melody)-1)])
    
    def mutate(self,gene_range,mutate_max):
        ''' Return a mutated organism '''
        c = self.copy()
        # Add note?
        attempts = 0
        if self.population.number_of_generations > 10:
            attempts = 1
        if self.population.number_of_generations > 40:
            attempts = 2
        elif self.population.number_of_generations > 100:
            attempts = 5
        for attempt in range(attempts):
            if random.random() < 0.005 or (self.population.number_of_generations >= 10 and random.random() < 0.02) or (self.population.number_of_generations >= 20 and random.random() < 0.1) or (self.population.number_of_generations >= 50 and random.random() < 0.25):
                # How many to insert?
                if self.population.number_of_generations > 20:
                    insert = 3
                elif self.population.number_of_generations > 10:
                    insert = 2
                else:
                    insert = 1
                #insert = random.randint(1,3)
                target_index = random.randint(0,min(len(self.target)-insert,len(c.genome)))
                for j in range(insert):
                    c.genome.insert(target_index,(self.target[target_index][0],self.target[target_index][1],[]))
                    target_index += 1
        # Remove note?
        if self.population.number_of_generations > 300:
            remove = 5
        elif self.population.number_of_generations > 100:
            remove = 3
        elif self.population.number_of_generations > 40:
            remove = 2
        elif self.population.number_of_generations > 20:
            remove = 1
        else:
            remove = 0
        for i in range(remove):
            if (random.random() < 0.005 or (self.population.number_of_generations >= 20 and random.random() < 0.02) or (self.population.number_of_generations >= 40 and random.random() < 0.1) or (self.population.number_of_generations >= 100 and random.random() < 0.5)) and len(c.genome) > 0:
                biggest_diff = 0
                biggest_diff_position = None
                for i in range(min(len(self.target),len(c.genome))):
                    if abs(self.target[i][0] - c.genome[i][0]) > biggest_diff:
                        biggest_diff = abs(self.target[i][0] - c.genome[i][0])
                        biggest_diff_position = i
                if biggest_diff_position is not None:
                    c.genome.pop(biggest_diff_position)
        
        i = 0
        while i < len(c.genome):
            if (random.random() < 0.0005 or (self.population.number_of_generations >= 20 and random.random() < 0.01) or (self.population.number_of_generations >= 40 and random.random() < 0.05) or (self.population.number_of_generations >= 100 and random.random() < 0.1)) and len(c.genome) > 0 and i < len(self.target):
                # Turn this one into the correct note
                c.genome[i] = (self.target[i][0],self.target[i][1],self.target[i][2])
                i += 1
                continue
            try:
                note = c.genome[i][0]
                time = c.genome[i][1]
            except:
                print "i",i
                print "g",c.genome[i]
            syllable = c.genome[i][2]
            # Add note?
            #if random.random() < 0.02:
            #    #print i,len(c.genome)
            #    #print "old",[tup[0] for tup in self.target]
            #    #print "new",[tup[0] for tup in self.target for j in range(int(5*(1-abs(i/float(len(c.genome))))))]
            #    # How many to insert?
            #    insert = random.randint(1,2)
            #    #target_index = random.randint(0,len(self.target)-insert)
            #    target_index = i % (len(self.target)-1)
            #    for j in range(insert):
            #        c.genome.insert(i,(self.target[target_index][0],self.target[target_index][1],[]))
            #        target_index += 1
            #        i += 1
            #    #c.genome.insert(i,(random.sample(get_weighted(i,len(c.genome),[tup[0] for tup in self.target]),1)[0],random.sample(get_weighted(i,len(c.genome),[tup[1] for tup in self.target]),1)[0],random.sample(SYLLABLES,1)[0]))
            #    #i += 1
            #    if i >= len(c.genome):
            #        break
            ## Remove note?
            #if random.random() < 0.02 and i > 0:
            #    c.genome.pop(i-1)
            #    i -= 1
            #    if i >= len(c.genome):
            #        break
            # Note
            if random.random() < 0.001:
                if (note and random.random() < 0.85) or (not note and random.random() < 0.15):
                    if random.random() < 0.5 and len([tup[0] for tup in self.target if tup[0] >= note - mutate_max and tup[0] <= note + mutate_max]) > 0:
                        note = random.sample(get_weighted(i,len(c.genome),[tup[0] for tup in self.target if tup[0] >= note - mutate_max and tup[0] <= note + mutate_max]),1)[0]
                    else:
                        note += int(random.uniform(-mutate_max,mutate_max))
                        if note > gene_range[1]:
                            note = gene_range[1]
                        if note < gene_range[0]:
                            note = gene_range[0]
                else:
                    note = 0
            # time
            if random.random() < 0.001:
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
            #elif random.random() < 0.1 or syllable == '':
            #    syllable = random.sample(SYLLABLES,1)[0]
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
        
            To do this, loop over all of the time encompassed by the
            two melodies and reward ones that are similar at the same
            time.
        '''
        # First, make the melodies absolute times:
        self_absolute = make_absolute(self.genome)
        genomes_absolute = []
        #genomes_absolute.append(make_absolute(target))
        genomes_absolute.append(target)
        if other_genomes:
            #genomes_absolute += [make_absolute(genome) for genome in other_genomes]
            genomes_absolute += other_genomes
        f = 0.0
        first = True
        tim = time.clock()
        if genomes_absolute:
            for genome_absolute in genomes_absolute:
                notes1 = [g[0] for g in self.genome]
                notes2 = [g[0] for g in genome_absolute]
                f += 1-max(np.correlate(notes1/np.linalg.norm(notes1),notes2/np.linalg.norm(notes2)))
                #if other_genomes:
                #    if first:
                #        print "FIRST!!!!"
                #    print "notes!",1-max(np.correlate(notes1/np.linalg.norm(notes1),notes2/np.linalg.norm(notes2)))
                times1 = [g[1] for g in self.genome]
                times2 = [g[1] for g in genome_absolute]
                f += 1-max(np.correlate(times1/np.linalg.norm(times1),times2/np.linalg.norm(times2)))
                #if other_genomes:
                #    if not first:
                #        print [g[1] for g in self.genome]
                #        print [g[1] for g in genome_absolute]
                #    print "times!",1-max(np.correlate(times1/np.linalg.norm(times1),times2/np.linalg.norm(times2)))
                #print "f1",f
                first = False
        #for genome_absolute in genomes_absolute:
        #    self_index = 0
        #    target_index = 0
        #    absolute_time = 0
        #    while self_index < len(self.genome) and target_index < len(genome_absolute):
        #        if first or (self.genome[self_index][0] != 0 and genome_absolute[target_index][0] != 0):
        #            f += (self.genome[self_index][0] - genome_absolute[target_index][0])**2
        #        #elif self.genome[self_index][0] != 0 or genome_absolute[target_index][0] != 0:
        #        #    f += 10
        #        #if first and self.genome[self_index][2] != genome_absolute[target_index][2]:
        #        #    f += 10
        #        absolute_time += 1.0/32.0
        #        if absolute_time > self_absolute[self_index][1]:
        #            self_index += 1
        #        if absolute_time > genome_absolute[target_index][1]:
        #            target_index += 1
        #    # Do special things for first melody because it is the true target
        #    first = False
        times = []
        times.append(time.clock()-tim)
        tim = time.clock()
        first = True
        if genomes_absolute:
            for genome_absolute in genomes_absolute:
                intervals1 = get_intervals([g[0] for g in self.genome])
                intervals2 = get_intervals([g[0] for g in genome_absolute])
                f += 1- max(np.correlate(intervals1/np.linalg.norm(intervals1),intervals2/np.linalg.norm(intervals2)))
                #print "f2",f
                continue
                if first:
                    f -= 100000*max(np.correlate(intervals1/np.linalg.norm(intervals1),intervals2/np.linalg.norm(intervals2)))
                else:
                    f -= 10000*max(np.correlate(intervals1/np.linalg.norm(intervals1),intervals2/np.linalg.norm(intervals2)))
                first = False
        times.append(time.clock()-tim)
        tim = time.clock()
        first = True
        if genomes_absolute:
            c1 = collections.Counter([tup[0] for tup in self.genome])
            for genome_absolute in genomes_absolute:
                c2 = collections.Counter([tup[0] for tup in genome_absolute])
                f += 1- counter_cosine_similarity(c1,c2)
                #print "f3",f
                continue
                if first:
                    f -= 100000*counter_cosine_similarity(c1,c2)
                else:
                    f -= 10000*counter_cosine_similarity(c1,c2)
                first = False
        times.append(time.clock()-tim)
        # 2-gram counters
        tim = time.clock()
        first = True
        if genomes_absolute:
            c1 = collections.Counter([(self.genome[index][0],self.genome[index+1][0]) for index in range(len(self.genome)-1)])
            for genome_absolute in genomes_absolute:
                c2 = collections.Counter([(genome_absolute[index][0],genome_absolute[index+1][0]) for index in range(len(genome_absolute)-1)])
                f += 1- counter_cosine_similarity(c1,c2)
                #print "f3",f
                continue
                if first:
                    f -= 100000*counter_cosine_similarity(c1,c2)
                else:
                    f -= 10000*counter_cosine_similarity(c1,c2)
                first = False
        times.append(time.clock()-tim)
        
        #print "TIMES",times
        
        self.fitness = f/5.0
    
    def copy(self):
        c = Organism()
        c.genome = copy(self.genome)
        c.target = self.target
        c.population = self.population
        return c
