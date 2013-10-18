from Organism import Organism
from Population import Population
from WAVWriter import WAVWriter

#tomorrow    = [40, 37, 38, 40, 45, 49, 47, 45, 49, 47, 45, 44, 42, 47, 44, 40, 37, 45, 47, 49, 38,0,0]
#tomorrow_time = [8, -8, 16, 4, -2, 4, 4, 4, -8, 16, 4, 4, 8, -4, 4, 4, 8, 2, 8, -4, 1,8,8]
tomorrow = [52,54,52,49,54,52,49,54,52,45,52,50,47,50,49,45,40,47,45,0,0,0,0]
tomorrow_time = [4,8,4,8,8,4,8,8,4,8,8,4,8,8,4,8,4,4,1,8,8,8,8]
yesterday   = [47,45,45,0,49,51,53,54,56,57,56,54,54,0,54,54,52,50,49,47,50,49,49]
yesterday_time = [8,8,-2,4,8,8,8,8,8,8,-8,16,-2,4,8,8,8,8,8,8,4,8,-4]

p_melody = Population(1000,yesterday,tomorrow,(0,88),10)
p_time = Population(1000,yesterday_time,tomorrow_time,(-32,32),4)

w = WAVWriter()
w.write(p_melody.best(1)[0].genome,"output/initial.wav",p_time.best(1)[0].genome)
w.write(tomorrow,"output/final.wav",tomorrow_time)

last_melody_fitness = p_melody.most_fit()

while True:
    if p_melody.most_fit() > 250:
        p_melody.generation()
    if p_time.most_fit() > 10:
        for i in range(5):
            p_time.generation()
    if last_melody_fitness - p_melody.most_fit() > 1000:
        print "melody:",p_melody.most_fit(),"time:",p_time.most_fit()
        w.write(p_melody.best(1)[0].genome,"output/"+str(p_melody.number_of_generations)+".wav",p_time.best(1)[0].genome)
        last_melody_fitness = p_melody.most_fit()
    if p_melody.most_fit() <= 250 and p_time.most_fit() <= 10:
        break

w.write(p_melody.best(1)[0].genome,"output/"+ str(p_melody.number_of_generations) +".wav",p_time.best(1)[0].genome)
