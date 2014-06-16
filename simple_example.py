from Organism import Organism
from Population import Population
from WAVWriter import WAVWriter,LilyWriter
from helpers import pad_melodies

yesterday_combined = [(47, 8, 'Yest'), (45, 8, 'er'), (45, -2, 'day,'), (0, 4, ''), (49, 8, 'all'), (51, 8, 'my'), (53, 8, 'trou-'), (54, 8, 'bles'), (56, 8, 'seemed'), (57, 8, 'so'), (56, -8, 'far'), (54, 16, 'a-'), (54, -2, 'way'), (0, 4, ''), (54, 8, 'Now'), (54, 8, 'it'), (52, 8, 'looks'), (50, 8, "as"), (49, 8, "though"), (47, 8, "they're"), (50, 4, 'here'), (49, 8, 'to'), (49, -4, 'stay')]
sun = [(0, 4, 'The'), (52, 8, "sun'll"), (50, 4, 'come'), (52, 4, 'out'), (48, -4, 'To-'), (52, 8, 'morr-'), (48, 8, 'ow'), (50, 8, 'Bet'), (52, -4, 'your'), (0, 4, 'bott-'), (52, 8, 'om'), (50, 4, 'doll-'), (52, 4, 'ar'), (48, -4, 'That'), (48, 8, 'to-'), (50, 4, 'mor-'), (48, 4, 'row'), (0, 8, "There'll"), (52, 4, 'be'), (50, 4, 'sun!'), (48, 4, 'Just'), (43, 8, 'thin-'), (45, 8, "kin'"), (48, 8, 'a-'), (50, 8, 'bout'), (43, 8, 'To-'), (48, 8, 'mor-'), (50, 8, 'row'), (41, 8, 'Clears'), (48, 8, 'away'), (50, 8, 'the'), (43, 8, 'cob-'), (48, 8, 'webs,'), (50, 8, 'And'), (48, 8, 'the'), (47, 8, 'sor-'), (45, 8, 'row'), (43, 8, "'Til")]

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
        if p_melody.most_fit() > 50 or p_melody2.most_fit() > 50:
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
            padding1, padding2 = pad_melodies([best1,best2])
            path += best1 + padding1
            path2 += best2 + padding2
            last_melody_fitness = min(p_melody.most_fit(),p_melody2.most_fit())
        if p_melody.most_fit() <= 50 and p_melody2.most_fit() <= 50:
            break
except KeyboardInterrupt:
    print "STOPPED"

#path += sun
#path2 += sun
w.write([path,path2],"output/simple_path")
