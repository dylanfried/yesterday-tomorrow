from Population import Population
from WAVWriter import WAVWriter,LilyWriter
from OperationOrganism import OperationOrganism

#tomorrow_combined = [(52,4),(54,8),(52,4),(49,8),(54,8),(52,4),(49,8),(54,8),(52,4),(45,8),(52,8),(50,4),(47,8),(50,8),(49,4),(45,8),(40,4),(47,4),(45,1)]
#tomorrow = [52,54,52,49,54,52,49,54,52,45,52,50,47,50,49,45,40,47,45]
#tomorrow_time = [4,8,4,8,8,4,8,8,4,8,8,4,8,8,4,8,4,4,1]
#yesterday_combined = [(47, 8), (45, 8), (45, -2), (0, 4), (49, 8), (51, 8), (53, 8), (54, 8), (56, 8), (57, 8), (56, -8), (54, 16), (54, -2), (0, 4), (54, 8), (54, 8), (52, 8), (50, 8), (49, 8), (47, 8), (50, 4), (49, 8), (49, -4)]
#yesterday   = [47,45,45,0,49,51,53,54,56,57,56,54,54,0,54,54,52,50,49,47,50,49,49]
#yesterday_time = [8,8,-2,4,8,8,8,8,8,8,-8,16,-2,4,8,8,8,8,8,8,4,8,-4]
#
##sun = [(0, 4), (53, 8), (51, 4), (53, 4), (50, -4), (53, 8), (50, 8), (51, 8), (53, -4), (0, 4), (53, 8), (51, 4), (53, 4), (50, -4), (50, 8), (51, 4), (50, 4), (0, 8), (53, 4), (51, 4), (50, 4), (44, 8), (46, 8), (50, 8), (51, 8), (44, 8), (50, 8), (51, 8), (42, 8), (50, 8), (51, 8), (44, 8), (50, 8), (51, 8), (50, 8), (48, 8), (46, 8), (44, 8)]
#sun = [(0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (52, 8), (48, 8), (50, 8), (52, -4), (0, 4), (52, 8), (50, 4), (52, 4), (48, -4), (48, 8), (50, 4), (48, 4), (0, 8), (52, 4), (50, 4), (48, 4), (43, 8), (45, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (41, 8), (48, 8), (50, 8), (43, 8), (48, 8), (50, 8), (48, 8), (47, 8), (45, 8), (43, 8)]



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

w = LilyWriter()
#w.write([tomorrow],"output/tomorrow")
#w.write([yesterday_combined],"output/yesterday")
#exit(0)
yesterday_combined = [(tup[0]-4 if tup[0] != 0 else 0,tup[1],tup[2]) for tup in yesterday_combined]
tomorrow = [(tup[0]-4 if tup[0] != 0 else 0,tup[1],tup[2]) for tup in tomorrow]


p_melody = Population(200,None,(yesterday_combined,tomorrow),(1,6),1,organism_class=OperationOrganism)
p_melody2 = Population(200,None,(yesterday_combined,tomorrow),(1,6),1,organism_class=OperationOrganism)

w = LilyWriter()
#w.write(p_melody.best(1)[0].resolve(yesterday,tomorrow),"output/"+str(p_melody.number_of_generations)+".wav")
#w.write(tomorrow,"output/final.wav")
#w.write([yesterday_combined],"output/start")
print yesterday_combined
print p_melody.best(1)[0].resolve(yesterday_combined,tomorrow),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit()
print tomorrow
last_fit = 0.0
last_gen = 0
try:
    while (p_melody.most_fit() + p_melody2.most_fit()) > 0.02:
        print "GEN: ", p_melody.number_of_generations, "\t", "(%.5f,%.5f)" % (p_melody.most_fit(),p_melody2.most_fit()), "\t\t","".join(["|" for i in range(int((p_melody.most_fit() + p_melody2.most_fit())*100))])
        p_melody.generation()
        p_melody2.generation()
        if not last_fit or last_fit - p_melody.most_fit() > 0.02 or p_melody.number_of_generations-last_gen > 100:
            last_fit = p_melody.most_fit()
            last_gen = p_melody.number_of_generations
            #print p_melody.best(1)[0].resolve(yesterday_combined,tomorrow),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit(),"level:",p_melody.best(1)[0].fitness_level
            #print tomorrow
            #print p_melody.summary(5)
            #w.write(p_melody.best(1)[0].resolve(yesterday,tomorrow),"output/"+str(p_melody.number_of_generations)+".wav")
        #elif p_melody.number_of_generations > 10000:
        #    break
except KeyboardInterrupt:
    print "STOPPED"
print "OUT"
print p_melody.best(1)[0].resolve(yesterday_combined,tomorrow),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit(),"level:",p_melody.best(1)[0].fitness_level
print tomorrow
#w.write([p_melody.best(1)[0].resolve(yesterday_combined,tomorrow)],"output/"+str(p_melody.number_of_generations)+"_final")
w.write([p_melody.best(1)[0].best_path(yesterday_combined,tomorrow,[1,5,5,5,5,5,10,10,10,10,10,10,10,10,2]),p_melody2.best(1)[0].best_path(yesterday_combined,tomorrow,[1,5,5,5,5,5,10,10,10,10,10,10,10,10,2])],"output/META_path")
w.write([p_melody.best(1)[0].resolve(yesterday_combined,tomorrow),p_melody2.best(1)[0].resolve(yesterday_combined,tomorrow)],"output/META_final")
