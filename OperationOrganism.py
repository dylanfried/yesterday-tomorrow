from copy import copy
import random
from helpers import shift

class OperationOrganism:
    length = 200
    def __init__(self,genome=None,target=None):
        if genome:
            self.genome = genome[:]
        else:
            self.genome = [(random.randint(2,6),random.randint(-20,20)) for i in range(self.length)]
    
    def random_genome(self,length):
        return
    
    def mutate(self,gene_range,mutate_max):
        ''' Return a mutated organism '''
        c = self.copy()
        for i in range(len(c.genome)):
            if random.random() < 0.01:
                # New random gene replacement
                c.genome[i] = (random.randint(gene_range[0],gene_range[1]),random.randint(-20,20))
            elif random.random() < 0.01:
                # Permute just the operand
                c.genome[i] = (c.genome[i][0],c.genome[i][1] + random.randint(-mutate_max,mutate_max))
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
        ''' Calculate the fitness of this organism '''
        # First, must resolve
        result = self.resolve(target[0],target[1])
        final_pattern = target[1]
        p_common = 0
        p_correct = 0
        p_common = float(len([1 for item in result if item in final_pattern]))/float(max(len(result),len(final_pattern)))
        for idx,item in enumerate(result):
            if idx < len(final_pattern) and item == final_pattern[idx]:
                p_correct += 1
        p_correct = float(p_correct)/float(max(len(result),len(final_pattern)))
        self.fitness = 1.0 - 0.5*(p_common + p_correct)
        self.fitness_level = self.length-1
        return
        result_path = self.resolve(target[0],target[1],record_path=True)
        final_pattern = target[1]
        self.fitness = 1
        for level,result in enumerate(result_path):
            p_common = 0
            p_correct = 0
            p_common = float(len([1 for item in result if item in final_pattern]))/float(max(len(result),len(final_pattern)))
            for idx,item in enumerate(result):
                if idx < len(final_pattern) and item == final_pattern[idx]:
                    p_correct += 1
            p_correct = float(p_correct)/float(max(len(result),len(final_pattern)))
            fitness = 1.0 - 0.5*(p_common + p_correct)
            if fitness < self.fitness:
                self.fitness = fitness
                self.fitness_level = level
    
    def copy(self):
        c = OperationOrganism(genome=self.genome)
        return c
        
    def resolve(self,start_pattern,final_pattern,record_path=False):
        result = start_pattern[:]
        if record_path:
            path = [result[:]]
        for operation_tuple in self.genome:
            operation = operation_tuple[0]
            operand = operation_tuple[1]
            if operation == 1:
                # no op
                pass
            elif operation == 2:
                # add
                #index = random.randint(0,len(final_pattern)-1)
                index = operand % len(final_pattern)
                result[index:index] = [final_pattern[index]]
            elif operation == 3 and len(result) > 0:
                # delete
                #index = random.randint(0,len(result)-1)
                index = operand % len(result)
                del result[index]
            elif operation == 4 and len(result) > 0:
                # mutate
                #index = random.randint(0,min(len(result)-1,len(final_pattern)-1))
                index = operand % min(len(result),len(final_pattern))
                result[index] = final_pattern[index]
            elif operation == 5 and len(result) > 0 and operand != 0:
                # rotation
                amount = (operand/abs(operand)) * (operand % len(result))
                result = shift(result,amount)
            elif operation == 6 and len(result) > 0:
                # exchange
                index1 = operand % len(result)
                index2 = (operand+1)%len(result)
                result[index1],result[index2] = result[index2],result[index1]
            elif operation == 7:
                # incorrect rotation
                pass
            elif operation == 8:
                # incorrect exchange
                pass
            if record_path:
                path.append(result[:])
        if record_path:
            return path
        else:
            return result
    
    def best_path(self,start_pattern,final_pattern,condense=[1]):
        condense = [i for i in condense for j in range(i)]
        to_return = []
        result_path = self.resolve(start_pattern,final_pattern,record_path=True)
        for j in range(len(condense)):
            start = int(self.fitness_level/len(condense))*j
            stop = int(self.fitness_level/len(condense))*(j+1)
            for i in range(start,stop,condense[j]):
                to_return += result_path[i]
        #to_return += final_pattern
        return to_return
