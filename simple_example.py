from Organism import Organism
from Population import Population
from WAVWriter import WAVWriter,LilyWriter
import helpers

yesterday_combined = [(47, 8, []), (45, 8, []), (45, -2, []), (0, 4, []), # Yesterday
                      (49, 8, []), (51, 8, []), (53, 8, []), (54, 8, []), (56, 8, []), (57, 8, []), (56, -8, []), (54, 16, []), (54, -2, []), # All my troubles seemed so far away
                      (0, 4, []), (54, 8, []), (54, 8, []), (52, 8, []), (50, 8, []), (49, 8, []), (47, 8, []), (50, 4, []), (49, 8, []), (49, -4, []), # Now it looks as though they're here to stay
                      (47, 4, []),(45, 4, []),(49, 8, []),(47, 2, []),(42, 8, []),(45, -4, []),(49, 8, []),(49, -2, []), # Oh I believe in (too much pause) yesterday
                      ]
                      #(47, 8, []),(45, 8, []),(45, -2, []), # Suddenly
                      #(0, 4, []),(49, 8, []), (51, 8, []), (53, 8, []), (54, 8, []), (56, 8, []), (57, 8, []), (56, -8, []), (54, 16, []), (54, -2, []), # I'm not half the man I used to be
                      #(0,4,[]),(54, 8, []), (54, 8, []), (52, 8, []), (50, 8, []), (49, 8, []), (47, 8, []), (50, 4, []), (49, 8, []), (49, -4, []), # There's a shadow hanging over me
                      #(47, 4, []),(45, 4, []),(49, 8, []),(47, 2, []),(42, 8, []),(45, -4, []),(49, 8, []),(49, -2, []), #Oh yesterday came (too much pause) suddenly
                      #(49,2,[]),(49,2,[]),(54,4,[]),(56,4,[]),(57,4,[]), # Why she had to go
                      #(56,8,[]),(54,8,[]),(56,-4,[]),(54,8,[]),(52,4,[]),(54,4,[]),(49,1,[]), # I don't know she wouldn't say
                      #(49,2,[]),(49,2,[]),(54,4,[]),(56,4,[]),(57,4,[]), # I said something wrong
                      #(56,8,[]),(54,8,[]),(56,-4,[]), # Now I long
                      #(54,8,[]),(52,4,[]),(56,4,[]),(57,4,[]),(52,4,[]),(50,4,[]),(49,4,[]), # For yesterday -eh -eh -eh
                      #(47, 8, []), (45, 8, []), (45, -2, []), (0, 4, []), # Yesterday
                      #(49, 8, []), (51, 8, []), (53, 8, []), (54, 8, []), (56, 8, []), (57, 8, []), (56, -8, []), (54, 16, []), (54, -2, []), # All my troubles seemed so far away
                      #(0, 4, []), (54, 8, []), (54, 8, []), (52, 8, []), (50, 8, []), (49, 8, []), (47, 8, []), (50, 4, []), (49, 8, []), (49, -4, []), # Now it looks as though they're here to stay
                      #(47, 4, []),(45, 4, []),(49, 8, []),(47, 2, []),(42, 8, []),(45, -4, []),(49, 8, []),(49, -2, []), # Oh I believe in yesterday
                      #(45,4,[]),(49,4,[]),(47,4,[]),(42,4,[]),(45,4,()),(49,8,[]),(49,-2,[])] # Mmmm, mmm, mmm, mmm, mmm, mm-mm
tomorrow           = [(40,8,[]),(37,-8,[]),(38,16,[]),(40,4,[]), # The sun'll come
                      (45,-2,[]),(49,4,[]),(47,4,[]),(45,4,[]),  # out tomorrow
                      (49,-8,[]),(47,16,[]),(45,4,[]),(44,4,[]),(42,8,[]),(47,-4,[]), # Bet your bottom dollar
                      (44,4,[]),(40,4,[]),(37,8,[]),(45,1,[]), # that tomorrow
                      (47,8,[]),(49,-4,[]),(38,1,[]), # there'll be sun
                      ]
                      #(40,8,[]),(37,-8,[]),(38,16,[]),(40,4,[]), # Just thinking about
                      #(45,-2,[]),(49,4,[]),(47,4,[]),(45,4,[]),  # tomorrow
                      #(49,-8,[]),(47,16,[]),(45,4,[]),(44,4,[]),(42,4,[]),(47,4,[]), # clears away the cobwebs
                      #(44,4,[]),(40,4,[]),(37,8,[]),(45,1,[]), # and the sorrow
                      #(47,4,[]),(49,4,[]),(38,1,[]), # till there's none
                      #(0,8,[]),(40,8,[]),(40,8,[]),(40,4,[]),(45,8,[]),(47,4,[]), # when I'm stuck with a 
                      #(48,-2,[]),(45,4,[]),(49,-2,[]),(45,4,[]), # day that's gray and
                      #(48,4,[]),(51,-2,[]), # lonely
                      #(0,8,[]),(43,8,[]),(44,8,[]),(44,4,[]),(49,8,[]),(50,4,[]), # I just stick out my
                      #(52,-2,[]),(48,4,[]),(52,-2,[]),(49,4,[]),(52,1,[]), # chin and grin and say
                      #(0,1,[]),(40,-4,[]),(38,8,[]), # Oh! The
                      #(37,-8,[]),(38,16,[]),(40,4,[]), # sun'll come
                      #(45,-2,[]),(49,4,[]),(47,4,[]),(45,4,[]),  # out tomorrow
                      #(49,-8,[]),(47,16,[]),(45,4,[]),(44,4,[]),(42,8,[]),(47,-4,[]), # So you got to hang on
                      #(44,4,[]),(40,4,[]),(37,8,[]),(45,1,[]), # til tomorrow
                      #(0,4,[]),(47,2,[]),(49,4,[]),(50,-1,[]), # come what may
                      #(52,2,[]), (54,4,[]), (52,2,[]), # tomorrow
                      #(49,4,[]), (54,4,[]), (52,2,[]), # tomorrow
                      #(49,4,[]), (54,4,[]), (52,2,[]), # I love ya
                      #(45,4,[]), (52,4,[]), (50,2,[]), # tomorrow
                      #(47,4,[]), (50,4,[]), (49,2,[]), # you're only
                      #(45,4,[]), (40,2,[]), (47,2,[]), (45,1,[]) # a day away
                      #] 
#sun = [(0, 4, 'The'), (52, 8, "sun'll"), (50, 4, 'come'), (52, 4, 'out'), (48, -4, 'To-'), (52, 8, 'morr-'), (48, 8, 'ow'), (50, 8, 'Bet'), (52, -4, 'your'), (0, 4, 'bott-'), (52, 8, 'om'), (50, 4, 'doll-'), (52, 4, 'ar'), (48, -4, 'That'), (48, 8, 'to-'), (50, 4, 'mor-'), (48, 4, 'row'), (0, 8, "There'll"), (52, 4, 'be'), (50, 4, 'sun!'), (48, 4, 'Just'), (43, 8, 'thin-'), (45, 8, "kin'"), (48, 8, 'a-'), (50, 8, 'bout'), (43, 8, 'To-'), (48, 8, 'mor-'), (50, 8, 'row'), (41, 8, 'Clears'), (48, 8, 'away'), (50, 8, 'the'), (43, 8, 'cob-'), (48, 8, 'webs,'), (50, 8, 'And'), (48, 8, 'the'), (47, 8, 'sor-'), (45, 8, 'row'), (43, 8, "'Til")]

w = LilyWriter()

#sun = helpers.midi_to_combined(helpers.tomorrow)
#yesterday_combined = helpers.midi_to_combined(helpers.yesterday)

yesterday_combined = helpers.assign_syllables(yesterday_combined,helpers.yesterday_lyrics)
tomorrow = helpers.assign_syllables(tomorrow,helpers.tomorrow_lyrics)

p_melody = Population(1000,yesterday_combined,tomorrow,(19,88),10)
p_melody2 = Population(1000,yesterday_combined,tomorrow,(19,88),10)

path = []
path += p_melody.best(1)[0].genome
path2 = []
path2 += p_melody2.best(1)[0].genome

last_melody_fitness = p_melody.most_fit()

try:
    while True:
        if p_melody.most_fit() > 0.05 or p_melody2.most_fit() > 0.05:
        #if p_melody.most_fit() > 0.2:
            p_melody.generation([p_melody2.best(1)[0].genome])
            #p_melody.generation()
            p_melody2.generation([p_melody.best(1)[0].genome])
        if  True or p_melody.number_of_generations % 5 == 0 or last_melody_fitness - p_melody.most_fit() > 0.1 or last_melody_fitness - p_melody2.most_fit() > 0.1:
            print p_melody.number_of_generations
            #print p_melody2.number_of_generations
            print "melody:",p_melody.most_fit()
            #print "melody2:",p_melody2.most_fit()
            #w.write([p_melody.best(1)[0].genome],"output/"+str(p_melody.number_of_generations))
            best1 = p_melody.best(1)[0].genome
            best2 = p_melody2.best(1)[0].genome
            padding1, padding2 = helpers.pad_melodies([best1,best2])
            path += best1 + padding1
            #path += best1
            path2 += best2 + padding2
            last_melody_fitness = min(p_melody.most_fit(),p_melody2.most_fit())
            #last_melody_fitness = p_melody.most_fit()
        if p_melody.most_fit() <= 0.05 and p_melody2.most_fit() <= 0.05:
        #if p_melody.most_fit() <= 0.2:
            break
except KeyboardInterrupt:
    print "STOPPED"

#path += tomorrow
#path2 += tomorrow

# Get some lyrics for these:
#lyrics1 = generate_lyrics(path1)
#lyrics2 = generate_lyrics(path2)

w.write([path,path2],"output/simple_path")
