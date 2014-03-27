from Organism import Organism
from Population import Population
from WAVWriter import WAVWriter,LilyWriter

#tomorrow    = [40, 37, 38, 40, 45, 49, 47, 45, 49, 47, 45, 44, 42, 47, 44, 40, 37, 45, 47, 49, 38,0,0]
#tomorrow_time = [8, -8, 16, 4, -2, 4, 4, 4, -8, 16, 4, 4, 8, -4, 4, 4, 8, 2, 8, -4, 1,8,8]
tomorrow = [52,54,52,49,54,52,49,54,52,45,52,50,47,50,49,45,40,47,45,0,0,0,0]
tomorrow_time = [4,8,4,8,8,4,8,8,4,8,8,4,8,8,4,8,4,4,1,8,8,8,8]
yesterday   = [47,45,45,0,49,51,53,54,56,57,56,54,54,0,54,54,52,50,49,47,50,49,49]
yesterday_time = [8,8,-2,4,8,8,8,8,8,8,-8,16,-2,4,8,8,8,8,8,8,4,8,-4]

yesterday_combined = [(47, 8), (45, 8), (45, -2), (0, 4), (49, 8), (51, 8), (53, 8), (54, 8), (56, 8), (57, 8), (56, -8), (54, 16), (54, -2), (0, 4), (54, 8), (54, 8), (52, 8), (50, 8), (49, 8), (47, 8), (50, 4), (49, 8), (49, -4)]
sun = [(0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (52, 8), (48, 8), (50, 8), (52, -4), (0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (48, 8), (50, 4), (48, 4), (0, 8), (52, 4), (50, 4), (48, 4), (43, 8), (45, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (41, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (48, 8), (47, 8), (45, 8), (43, 8)]

p_melody = Population(1000,yesterday_combined,sun,(0,88),10)
p_melody2 = Population(1000,yesterday_combined,sun,(0,88),10)
#p_time = Population(1000,yesterday_time,tomorrow_time,(-32,32),4)

path = []
path += p_melody.best(1)[0].genome
path2 = []
path2 += p_melody.best(1)[0].genome

w = LilyWriter()
#w.write([[(47,0)]],'output/TESTER')
#w.write([p_melody.best(1)[0].genome],"output/initial")
#w.write([sun],"output/final")

last_melody_fitness = p_melody.most_fit()

try:
    while True:
        if p_melody.most_fit() > 250 and p_melody2.most_fit() > 250:
            p_melody.generation([p_melody2.best(1)[0].genome])
            p_melody2.generation([p_melody.best(1)[0].genome])
        if last_melody_fitness - p_melody.most_fit() > 1000 or last_melody_fitness - p_melody2.most_fit() > 1000:
            print "melody:",p_melody.most_fit()
            print "melody2:",p_melody2.most_fit()
            #w.write([p_melody.best(1)[0].genome],"output/"+str(p_melody.number_of_generations))
            path += p_melody.best(1)[0].genome
            path2 += p_melody2.best(1)[0].genome
            last_melody_fitness = min(p_melody.most_fit(),p_melody2.most_fit())
        if p_melody.most_fit() <= 250:
            break
except KeyboardInterrupt:
    print "STOPPED"

#w.write([p_melody.best(1)[0].genome],"output/"+ str(p_melody.number_of_generations))
path += sun
path2 += sun
path += sun
w.write([path,path2],"output/simple_path")
