import random
from OperationOrganism import OperationOrganism
from Organism import Organism

class Population:
    
    def __init__(self,number_of_organisms,start_melody,end_melody,gene_range=(0,88),mutate_max=10):
        self.number_of_organisms = number_of_organisms
        self.start_melody = start_melody
        self.end_melody = end_melody
        
        self.gene_range = gene_range
        self.mutate_max = mutate_max
        
        self.population = []
        self.number_of_generations = 0
        
        for i in range(self.number_of_organisms):
            self.population.append(Organism(start_melody))
        
        self.calculate_fitness()
    
    def generation(self,other_melodies=None):
        ''' Move forward one generation '''
        try:                                             
            new_population = []
            
            # Keep copies of the best
            #new_population += self.best(1)
            
            sampled = self.sample(int(self.number_of_organisms)-100)
            
            random.shuffle(sampled)
            
            for i in range(0,len(sampled),2):
                m1 = sampled[i].mutate(self.gene_range,self.mutate_max)
                m2 = sampled[i+1].mutate(self.gene_range,self.mutate_max)
                if random.random() > 0.7:
                    new_population += m1.crossover(m2)
                else:
                    new_population.append(m1)
                    new_population.append(m2)
            
            # Generate some random organisms
            for i in range(self.number_of_organisms - len(new_population)):
                random_organism = Organism()
                random_organism.random_genome(len(self.end_melody))
                new_population.append(random_organism)
            
            ## Keep some
            #sampled = self.sample(int(self.number_of_organisms*0.2))
            #new_population += [s.copy() for s in sampled]
            #
            ## Keep some with mutations
            #sampled = self.sample(int(self.number_of_organisms*0.3))
            #new_population += [s.mutate(self.gene_range,self.mutate_max) for s in sampled]
            #
            ## Keep some with crossover
            #for i in range(int(self.number_of_organisms*0.35)):
            #    sampled = self.sample(2)
            #    new_population.append(sampled[0].crossover(sampled[1]))
            #
            ## Fill out the rest with random new organisms
            #for i in range(self.number_of_organisms-len(new_population)):
            #    new_population.append(OperationOrganism(self.start_melody))
            
            self.population = new_population
            self.number_of_generations += 1
            # Calculate fitness
            self.calculate_fitness(other_melodies)
        except KeyboardInterrupt:
            print "Caught keyboard interrupt"
            self.calculate_fitness(other_melodies)
            raise
    
    def calculate_fitness(self,other_melodies=None):
        for organism in self.population:
            organism.calculate_fitness(self.end_melody,other_melodies)
    
    def most_fit(self):
        ''' Return the highest fitness '''
        return self.best(1)[0].fitness
    
    def best(self,n):
        ''' Return the best n organisms '''
        sorted_organisms = sorted(self.population,key=lambda organism: organism.fitness)
        return sorted_organisms[:n]
    
    def sample(self,n):
        ''' Sample n organisms from the population, with the fitness acting as a weight '''
        container = []
        for i in range(n):
            container.append(self.tournament_choice())
        return container

    def tournament_choice(self,k=2):
        organisms = random.sample(self.population,2)
        if organisms[0].fitness > organisms[1].fitness:
            return organisms[1]
        else:
            return organisms[0]

    def weighted_choice(self):
        max_fitness = max([organism.fitness for organism in self.population])
        attempts = 0
        while True:
            organism = random.sample(self.population,1)[0]
            product = random.random()*max_fitness
            if product >= organism.fitness:
                return organism
            attempts += 1
            if attempts > 100:
                return organism
    
    def summary(self,n):
        ''' Print a summary of the best n organisms '''
        best_n = self.best(n)
        for organism in best_n:
            print "\nORGANISM"
            print "FITNESS:",organism.fitness
            print "GENOME:",organism.genome
