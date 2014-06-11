from Organism import Organism
from Population import Population
from WAVWriter import WAVWriter,LilyWriter
from helpers import pad_melodies

yesterday_combined = [(47, 8), (45, 8), (45, -2), (0, 4), (49, 8), (51, 8), (53, 8), (54, 8), (56, 8), (57, 8), (56, -8), (54, 16), (54, -2), (0, 4), (54, 8), (54, 8), (52, 8), (50, 8), (49, 8), (47, 8), (50, 4), (49, 8), (49, -4)]
sun = [(0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (52, 8), (48, 8), (50, 8), (52, -4), (0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (48, 8), (50, 4), (48, 4), (0, 8), (52, 4), (50, 4), (48, 4), (43, 8), (45, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (41, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (48, 8), (47, 8), (45, 8), (43, 8)]

p_melody = Population(1000,yesterday_combined,sun,(0,88),10)
p_melody2 = Population(1000,yesterday_combined,sun,(0,88),10)

path = []
path += p_melody.best(1)[0].genome
path2 = []
path2 += p_melody.best(1)[0].genome

w = LilyWriter()

last_melody_fitness = p_melody.most_fit()

try:
    while True:
        if p_melody.most_fit() > 200 or p_melody2.most_fit() > 200:
            p_melody.generation([p_melody2.best(1)[0].genome])
            p_melody2.generation([p_melody.best(1)[0].genome])
        if True or p_melody.number_of_generations % 3 == 0 or last_melody_fitness - p_melody.most_fit() > 1000 or last_melody_fitness - p_melody2.most_fit() > 1000:
            print p_melody.number_of_generations
            print p_melody2.number_of_generations
            print "melody:",p_melody.most_fit()
            print "melody2:",p_melody2.most_fit()
            #w.write([p_melody.best(1)[0].genome],"output/"+str(p_melody.number_of_generations))
            best1 = p_melody.best(1)[0].genome
            best2 = p_melody2.best(1)[0].genome
            best1, best2 = pad_melodies([best1,best2])
            path += best1
            path2 += best2
            last_melody_fitness = min(p_melody.most_fit(),p_melody2.most_fit())
        if p_melody.most_fit() <= 200 and p_melody2.most_fit() <= 200:
            break
except KeyboardInterrupt:
    print "STOPPED"

path += sun
path2 += sun
path += sun
w.write([path,path2],"output/simple_path")
