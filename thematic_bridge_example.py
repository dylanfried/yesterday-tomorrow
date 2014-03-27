from Organism import Organism
from Population import Population
from WAVWriter import WAVWriter,LilyWriter

tomorrow_combined = [(52,4),(54,8),(52,4),(49,8),(54,8),(52,4),(49,8),(54,8),(52,4),(45,8),(52,8),(50,4),(47,8),(50,8),(49,4),(45,8),(40,4),(47,4),(45,1)]
tomorrow = [52,54,52,49,54,52,49,54,52,45,52,50,47,50,49,45,40,47,45]
tomorrow_time = [4,8,4,8,8,4,8,8,4,8,8,4,8,8,4,8,4,4,1]
yesterday_combined = [(47, 8), (45, 8), (45, -2), (0, 4), (49, 8), (51, 8), (53, 8), (54, 8), (56, 8), (57, 8), (56, -8), (54, 16), (54, -2), (0, 4), (54, 8), (54, 8), (52, 8), (50, 8), (49, 8), (47, 8), (50, 4), (49, 8), (49, -4)]
yesterday   = [47,45,45,0,49,51,53,54,56,57,56,54,54,0,54,54,52,50,49,47,50,49,49]
yesterday_time = [8,8,-2,4,8,8,8,8,8,8,-8,16,-2,4,8,8,8,8,8,8,4,8,-4]

#sun = [(0, 4), (53, 8), (51, 4), (53, 4), (50, -4), (53, 8), (50, 8), (51, 8), (53, -4), (0, 4), (53, 8), (51, 4), (53, 4), (50, -4), (50, 8), (51, 4), (50, 4), (0, 8), (53, 4), (51, 4), (50, 4), (44, 8), (46, 8), (50, 8), (51, 8), (44, 8), (50, 8), (51, 8), (42, 8), (50, 8), (51, 8), (44, 8), (50, 8), (51, 8), (50, 8), (48, 8), (46, 8), (44, 8)]
sun = [(0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (52, 8), (48, 8), (50, 8), (52, -4), (0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (48, 8), (50, 4), (48, 4), (0, 8), (52, 4), (50, 4), (48, 4), (43, 8), (45, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (41, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (48, 8), (47, 8), (45, 8), (43, 8)]

p_melody = Population(100,None,(yesterday_combined,sun),(1,5),1)

w = LilyWriter()
#w.write(p_melody.best(1)[0].resolve(yesterday,tomorrow),"output/"+str(p_melody.number_of_generations)+".wav")
#w.write(tomorrow,"output/final.wav")
w.write(yesterday_combined,"output/start")
print yesterday_combined
print p_melody.best(1)[0].resolve(yesterday_combined,sun),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit()
print tomorrow
last_fit = 0.0
last_gen = 0
try:
    while p_melody.most_fit() > 0.1:
        print p_melody.most_fit()
        p_melody.generation()
        if not last_fit or last_fit - p_melody.most_fit() > 0.05 or p_melody.number_of_generations-last_gen > 100:
            last_fit = p_melody.most_fit()
            last_gen = p_melody.number_of_generations
            print p_melody.best(1)[0].resolve(yesterday_combined,sun),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit(),"level:",p_melody.best(1)[0].fitness_level
            print tomorrow
            print p_melody.summary(5)
            #w.write(p_melody.best(1)[0].resolve(yesterday,tomorrow),"output/"+str(p_melody.number_of_generations)+".wav")
        elif p_melody.number_of_generations > 10000:
            break
except KeyboardInterrupt:
    print "STOPPED"
print "OUT"
print p_melody.best(1)[0].resolve(yesterday_combined,sun),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit(),"level:",p_melody.best(1)[0].fitness_level
print tomorrow
w.write(p_melody.best(1)[0].resolve(yesterday_combined,sun),"output/"+str(p_melody.number_of_generations)+"_final")
w.write(p_melody.best(1)[0].best_path(yesterday_combined,sun,4),"output/"+str(p_melody.number_of_generations)+"_path")
