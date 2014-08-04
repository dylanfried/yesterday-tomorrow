from SimpleOrganism import SimpleOrganism
from Population import Population
from WAVWriter import WAVWriter,LilyWriter
import helpers

yesterday_combined = [(47, 8, ['Yes']), (45, 8, ['ter']), (45, -2, ['day']), (0, 4, []), # Yesterday
                      (49, 8, ['all']), (51, 8, ['my']), (53, 8, ['trou']), (54, 8, ['bles']), (56, 8, ['seemed']), (57, 8, ['so']), (56, -8, ['far']), (54, 16, ['a']), (54, -2, ['way']), # All my troubles seemed so far away
                      (0, 4, []), (54, 8, ['now']), (54, 8, ['it']), (52, 8, ['looks']), (50, 8, ['as']), (49, 8, ['though']), (47, 8, ["they're"]), (50, 4, ['here']), (49, 8, ['to']), (49, -4, ['stay']), # Now it looks as though they're here to stay
                      (47, 4, ['oh']),(45, 4, ['I']),(49, 8, ['be']),(47, 2, ['lieve']),(42, 8, ['in']),(45, -4, ['yes']),(49, 8, ['ter']),(49, -2, ['day']), # Oh I believe in (too much pause) yesterday
                      (47, 8, []),(45, 8, []),(45, -2, []), # Suddenly
                      (0, 4, []),(49, 8, []), (51, 8, []), (53, 8, []), (54, 8, []), (56, 8, []), (57, 8, []), (56, -8, []), (54, 16, []), (54, -2, []), # I'm not half the man I used to be
                      (0,4,[]),(54, 8, []), (54, 8, []), (52, 8, []), (50, 8, []), (49, 8, []), (47, 8, []), (50, 4, []), (49, 8, []), (49, -4, []), # There's a shadow hanging over me
                      (47, 4, []),(45, 4, []),(49, 8, []),(47, 2, []),(42, 8, []),(45, -4, []),(49, 8, []),(49, -2, []), #Oh yesterday came (too much pause) suddenly
                      (49,2,[]),(49,2,[]),(54,4,[]),(56,4,[]),(57,4,[]), # Why she had to go
                      (56,8,[]),(54,8,[]),(56,-4,[]),(54,8,[]),(52,4,[]),(54,4,[]),(49,1,[]), # I don't know she wouldn't say
                      (49,2,[]),(49,2,[]),(54,4,[]),(56,4,[]),(57,4,[]), # I said something wrong
                      (56,8,[]),(54,8,[]),(56,-4,[]), # Now I long
                      (54,8,[]),(52,4,[]),(56,4,[]),(57,4,[]),(52,4,[]),(50,4,[]),(49,4,[]), # For yesterday -eh -eh -eh
                      #(47, 8, []), (45, 8, []), (45, -2, []), (0, 4, []), # Yesterday
                      #(49, 8, []), (51, 8, []), (53, 8, []), (54, 8, []), (56, 8, []), (57, 8, []), (56, -8, []), (54, 16, []), (54, -2, []), # All my troubles seemed so far away
                      #(0, 4, []), (54, 8, []), (54, 8, []), (52, 8, []), (50, 8, []), (49, 8, []), (47, 8, []), (50, 4, []), (49, 8, []), (49, -4, []), # Now it looks as though they're here to stay
                      #(47, 4, []),(45, 4, []),(49, 8, []),(47, 2, []),(42, 8, []),(45, -4, []),(49, 8, []),(49, -2, []), # Oh I believe in yesterday
                      #(45,4,[]),(49,4,[]),(47,4,[]),(42,4,[]),(45,4,()),(49,8,[]),(49,-2,[]) # Mmmm, mmm, mmm, mmm, mmm, mm-mm
                      ]
tomorrow           = [#(40,8,[]),(37,-8,[]),(38,16,[]),(40,4,[]), # The sun'll come
                      #(45,-2,[]),(49,4,[]),(47,4,[]),(45,4,[]),  # out tomorrow
                      #(49,-8,[]),(47,16,[]),(45,4,[]),(44,4,[]),(42,8,[]),(47,-4,[]), # Bet your bottom dollar
                      #(44,4,[]),(40,4,[]),(37,8,[]),(45,1,[]), # that tomorrow
                      #(47,8,[]),(49,-4,[]),(38,1,[]), # there'll be sun
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
                      (0,2,[]),(40,-4,['Oh']),(38,8,['the']), # Oh! The
                      (37,-8,['sun']),(38,16,["'ll"]),(40,4,['come']), # sun'll come
                      (45,-2,['out']),(49,4,['to']),(47,4,['mor']),(45,4,['row']),  # out tomorrow
                      (49,-8,['So']),(47,16,['you']),(45,4,['got']),(44,4,['to']),(42,8,['hang']),(47,-4,['on']), # So you got to hang on
                      (44,4,['til']),(40,4,['to']),(37,8,['mor']),(45,1,['row']), # til tomorrow
                      (0,4,[]),(47,2,['come']),(49,4,['what']),(50,-1,['may']), # come what may
                      (52,2,['to']), (54,4,['mor']), (52,2,['row']), # tomorrow
                      (49,4,['to']), (54,4,['mor']), (52,2,['row']), # tomorrow
                      (49,4,['I']), (54,4,['love']), (52,2,['ya']), # I love ya
                      (45,4,['to']), (52,4,['mor']), (50,2,['row']), # tomorrow
                      (47,4,["You're"]), (50,4,['on']), (49,2,['ly']), # you're only
                      (45,4,['a']), (40,2,['day']), (47,2,['a']), (45,1,['way']) # a day away
                      ] 

yesterday_combined = [(tup[0]-4 if tup[0] != 0 else 0,tup[1],tup[2]) for tup in yesterday_combined]
tomorrow = [(tup[0]-4 if tup[0] != 0 else 0,tup[1],tup[2]) for tup in tomorrow]

w = LilyWriter()

p_melody = Population(200,yesterday_combined,tomorrow,(19,88),2,organism_class=SimpleOrganism)
p_melody2 = Population(200,yesterday_combined,tomorrow,(19,88),2,organism_class=SimpleOrganism)
p_melody3 = Population(200,yesterday_combined,tomorrow,(19,88),2,organism_class=SimpleOrganism)

path = []
path += p_melody.best(1)[0].genome
path2 = []
path2 += p_melody2.best(1)[0].genome
path3 = []
path3 += p_melody3.best(1)[0].genome

last_melody_fitness = p_melody.most_fit()

interval = 1

repeats = 0

total_paths = 0

try:
    while True:
        if p_melody.most_fit() > 0.01 or p_melody2.most_fit() > 0.01 or p_melody3.most_fit() > 0.01:
        #if p_melody.most_fit() > 0.05:
            #p_melody.generation([p_melody2.best(1)[0].genome])
            p_melody.generation()
            p_melody2.generation()
            p_melody3.generation()
            #p_melody2.generation([p_melody.best(1)[0].genome])
        new_melody_fitness = min(p_melody.most_fit(),p_melody2.most_fit(),p_melody3.most_fit())
        #new_melody_fitness = p_melody.most_fit()
        if new_melody_fitness != last_melody_fitness:
            repeats = 0
        else:
            repeats += 1
        #if  repeats < 1 and (p_melody.number_of_generations % interval == 0 or last_melody_fitness - p_melody.most_fit() > 0.1 or last_melody_fitness - p_melody2.most_fit() > 0.1):
        #if  repeats < 1 and (p_melody.number_of_generations % interval == 0 or last_melody_fitness - p_melody.most_fit() > 0.1):
        if  repeats < 1 and p_melody.number_of_generations % interval == 0:
            total_paths += 1
            #print "GEN: ",p_melody.number_of_generations, "FITNESS:",min(p_melody.most_fit(),p_melody2.most_fit()), "||"
            print "MIDI GEN: ", total_paths, "\tGEN: ",p_melody.number_of_generations, "\tFITNESS1: %.5f" %p_melody.most_fit(), "\tFITNESS2: %.5f" % p_melody2.most_fit(), "\tFITNESS3: %.5f" % p_melody3.most_fit()#, "\t","".join(["|" for counter in range(int((p_melody.most_fit() + p_melody2.most_fit())/6))])
            if p_melody.number_of_generations > 20:
                interval = 5
            if p_melody.number_of_generations > 100:
                interval = 20
            #print p_melody2.number_of_generations
            #print "melody:",p_melody.most_fit()
            #print "melody2:",p_melody2.most_fit()
            #w.write([p_melody.best(1)[0].genome],"output/"+str(p_melody.number_of_generations))
            best_organism1 = p_melody.best(1)[0]
            best_organism2 = p_melody2.best(1)[0]
            best_organism3 = p_melody3.best(1)[0]
            best1 = p_melody.best(1)[0].genome
            best2 = p_melody2.best(1)[0].genome
            best3 = p_melody3.best(1)[0].genome
            min_fitness = min([best_organism1.fitness,best_organism2.fitness,best_organism3.fitness])
            if min_fitness < best_organism1.fitness and (float(best_organism1.fitness) - float(min_fitness))/best_organism1.fitness > 0.25:
                print "MUTING 1"
                best1 = [(0,b[1],b[2]) for b in best1]
            if min_fitness < best_organism2.fitness and (float(best_organism2.fitness) - float(min_fitness))/best_organism2.fitness > 0.25:
                print "MUTING 2"
                best2 = [(0,b[1],b[2]) for b in best2]
            if min_fitness < best_organism3.fitness and (float(best_organism3.fitness) - float(min_fitness))/best_organism3.fitness > 0.25:
                print "MUTING 3"
                best3 = [(0,b[1],b[2]) for b in best3]
            #if best_organism1.fitness and best_organism2.fitness:
            #    # If one is too far behind the other, then mute it
            #    if float(best_organism1.fitness)/float(best_organism2.fitness) < 0.7:
            #        print "MUTING 2"
            #        # better mute organism 2
            #        best2 = [(0,b[1],b[2]) for b in best2]
            #    elif float(best_organism2.fitness)/float(best_organism1.fitness) < 0.7:
            #        print "MUTING 1"
            #        best1 = [(0,b[1],b[2]) for b in best1]
            padding1, padding2,padding3 = helpers.pad_melodies([best1,best2,best3])
            path += best1 + padding1
            #path += best1
            path2 += best2 + padding2
            path3 += best3 + padding3
            #if last_melody_fitness == min(p_melody.most_fit(),p_melody2.most_fit()):
            #if last_melody_fitness == p_melody.most_fit():
            #    repeats += 1
            #else:
            #    repeats = 0
            last_melody_fitness = min(p_melody.most_fit(),p_melody2.most_fit(),p_melody3.most_fit())
            #last_melody_fitness = p_melody.most_fit()
        if p_melody.most_fit() <= 0.01 and p_melody2.most_fit() <= 0.01 and p_melody3.most_fit() <= 0.01:
        #if p_melody.most_fit() <= 0.05:
            print "BREAKING"
            print "MIDI GEN: ", total_paths, "\tGEN: ",p_melody.number_of_generations, "\tFITNESS1: %.5f" %p_melody.most_fit(), "\tFITNESS2: %.5f" % p_melody2.most_fit(), "\tFITNESS3: %.5f" % p_melody3.most_fit()#, "\t","".join(["|" for counter in range(int((p_melody.most_fit() + p_melody2.most_fit())/6))])
            break
except KeyboardInterrupt:
    print "STOPPED"

#path += tomorrow
#path2 += tomorrow

# Get some lyrics for these:
#lyrics1 = generate_lyrics(path1)
#lyrics2 = generate_lyrics(path2)

w.write([best1,best2,best3],"output/super_simple_final")
w.write([path,path2,path3],"output/super_simple_path")
#w.write([path],"output/simple_path")
