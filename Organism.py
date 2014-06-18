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
    
    def __init__(self,genome=None,target_genome=None):
        if genome:
            self.genome = copy(genome)
        else:
            self.genome = []
        self.target = target_genome
    
    def random_genome(self,length):
        for i in range(length):
            note = random.sample(get_weighted(i,length,[tup[0] for tup in self.target]),1)[0]
            time = random.sample(get_weighted(i,length,[tup[1] for tup in self.target]),1)[0]
            syllable = []
            if note != 0:
                syllable = random.sample(SYLLABLES,1)[0]
            self.genome.append((note,time,syllable))
    
    def mutate(self,gene_range,mutate_max):
        ''' Return a mutated organism '''
        c = self.copy()
        i = 0
        while i < len(c.genome):
            try:
                note = c.genome[i][0]
                time = c.genome[i][1]
            except:
                print "i",i
                print "g",c.genome[i]
            syllable = c.genome[i][2]
            # Add note?
            if random.random() < 0.02:
                #print i,len(c.genome)
                #print "old",[tup[0] for tup in self.target]
                #print "new",[tup[0] for tup in self.target for j in range(int(5*(1-abs(i/float(len(c.genome))))))]
                # How many to insert?
                insert = random.randint(1,2)
                target_index = random.randint(0,len(self.target)-insert)
                for j in range(insert):
                    c.genome.insert(i,(self.target[target_index][0],self.target[target_index][1],[]))
                    target_index += 1
                    i += 1
                #c.genome.insert(i,(random.sample(get_weighted(i,len(c.genome),[tup[0] for tup in self.target]),1)[0],random.sample(get_weighted(i,len(c.genome),[tup[1] for tup in self.target]),1)[0],random.sample(SYLLABLES,1)[0]))
                #i += 1
                if i >= len(c.genome):
                    break
            # Remove note?
            if random.random() < 0.02 and i > 0:
                c.genome.pop(i-1)
                i -= 1
                if i >= len(c.genome):
                    break
            # Note
            if random.random() < 0.02:
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
            if random.random() < 0.02:
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
            elif random.random() < 0.1 or syllable == '':
                syllable = random.sample(SYLLABLES,1)[0]
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
        
        #print "TIMES",times
        
        self.fitness = f
    
    def copy(self):
        c = Organism()
        c.genome = copy(self.genome)
        c.target = self.target
        return c
