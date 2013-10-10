import random
from Organism import Organism

class Population:
    population = []
    number_of_organisms = 0
    start_melody = None
    end_melody = None
    
    def __init__(self,number_of_organisms,start_melody,end_melody):
        self.number_of_organisms = number_of_organisms
        self.start_melody = start_melody
        self.end_melody = end_melody
        
        for i in range(self.number_of_organisms):
            self.population.append(Organism(start_melody))
            self.population[-1].calculate_fitness(end_melody)
    
    def generation(self):
        ''' Move forward one generation '''
        new_population = []
        
        # Keep some
        sampled = self.sample(int(self.number_of_organisms/5))
        print self.number_of_organisms, int(self.number_of_organisms/5), sampled
        new_population += [s.copy() for s in sampled]
        
        # Keep some with mutations
        sampled = self.sample(int(self.number_of_organisms/4))
        new_population += [s.mutate() for s in sampled]
        
        # Keep some with crossover
        for i in range(int(self.number_of_organisms/4)):
            sampled = self.sample(2)
            new_population.append(sampled[0].crossover(sampled[1]))
        
        # Fill out the rest with random new organisms
        for i in range(self.number_of_organisms-len(new_population)):
            new_population.append(Organism(self.start_melody))
        
        self.population = new_population
        
        # Calculate fitness
        self.calculate_fitness()
    
    def calculate_fitness(self):
        for organism in self.population:
            organism.calculate_fitness(self.end_melody)
    
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
            container.append(self.weighted_choice())
        return container

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
