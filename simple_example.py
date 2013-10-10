from Organism import Organism
from Population import Population
from WAVWriter import WAVWriter

tomorrow    = [40,37,38,40,45,49,47,45,49,47,45,44,42,47,44,40,37,45,0,0,0]
yesterday   = [47,45,45,49,51,53,54,56,57,56,54,54,54,54,52,50,49,47,50,49,49]

p = Population(500,yesterday,tomorrow)

w = WAVWriter()
w.write(p.best(1)[0].genome,"output/initial.wav")

while True:
    p.generation()
    if p.number_of_generations % 100 == 0:
        print p.most_fit()
        w.write(p.best(1)[0].genome,"output/"+str(p.number_of_generations)+".wav")
    if p.most_fit() < 250:
        break

w.write(p.best(1)[0].genome,"output/final.wav")
