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



yesterday_combined = [(47, 8, []), (45, 8, []), (45, -2, []), (0, 4, []), # Yesterday
                      (49, 8, []), (51, 8, []), (53, 8, []), (54, 8, []), (56, 8, []), (57, 8, []), (56, -8, []), (54, 16, []), (54, -2, []), # All my troubles seemed so far away
                      (0, 4, []), (54, 8, []), (54, 8, []), (52, 8, []), (50, 8, []), (49, 8, []), (47, 8, []), (50, 4, []), (49, 8, []), (49, -4, []), # Now it looks as though they're here to stay
                      (47, 4, []),(45, 4, []),(49, 8, []),(47, 2, []),(42, 8, []),(45, -4, []),(49, 8, []),(49, -2, []), # Oh I believe in (too much pause) yesterday
                      # Adding bridge between verses (even though it doesn't really go here)
                      (49,2,[]),(49,2,[]),(54,4,[]),(56,4,[]),(57,4,[]), # Why she had to go
                      (56,8,[]),(54,8,[]),(56,-4,[]),(54,8,[]),(52,4,[]),(54,4,[]),(49,1,[]), # I don't know she wouldn't say
                      (49,2,[]),(49,2,[]),(54,4,[]),(56,4,[]),(57,4,[]), # I said something wrong
                      (56,8,[]),(54,8,[]),(56,-4,[]), # Now I long
                      (54,8,[]),(52,4,[]),(56,4,[]),(57,4,[]),(52,4,[]),(50,4,[]),(49,4,[]), # For yesterday -eh -eh -eh
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
                      (0,2,[]),(40,-4,[]),(38,8,[]), # Oh! The
                      (37,-8,[]),(38,16,[]),(40,4,[]), # sun'll come
                      (45,-2,[]),(49,4,[]),(47,4,[]),(45,4,[]),  # out tomorrow
                      (49,-8,[]),(47,16,[]),(45,4,[]),(44,4,[]),(42,8,[]),(47,-4,[]), # So you got to hang on
                      (44,4,[]),(40,4,[]),(37,8,[]),(45,1,[]), # til tomorrow
                      (0,4,[]),(47,2,[]),(49,4,[]),(50,-1,[]), # come what may
                      (52,2,[]), (54,4,[]), (52,2,[]), # tomorrow
                      (49,4,[]), (54,4,[]), (52,2,[]), # tomorrow
                      (49,4,[]), (54,4,[]), (52,2,[]), # I love ya
                      (45,4,[]), (52,4,[]), (50,2,[]), # tomorrow
                      (47,4,[]), (50,4,[]), (49,2,[]), # you're only
                      (45,4,[]), (40,2,[]), (47,2,[]), (45,1,[]) # a day away
                      ] 




p_melody = Population(400,None,(yesterday_combined,tomorrow),(2,6),1,organism_class=OperationOrganism)

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
    while p_melody.most_fit() > 0.1:
        print p_melody.most_fit(), "\t\t\t","".join(["|" for i in range(int(p_melody.most_fit()*100))])
        p_melody.generation()
        if not last_fit or last_fit - p_melody.most_fit() > 0.05 or p_melody.number_of_generations-last_gen > 100:
            last_fit = p_melody.most_fit()
            last_gen = p_melody.number_of_generations
            #print p_melody.best(1)[0].resolve(yesterday_combined,tomorrow),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit(),"level:",p_melody.best(1)[0].fitness_level
            #print tomorrow
            #print p_melody.summary(5)
            #w.write(p_melody.best(1)[0].resolve(yesterday,tomorrow),"output/"+str(p_melody.number_of_generations)+".wav")
        elif p_melody.number_of_generations > 10000:
            break
except KeyboardInterrupt:
    print "STOPPED"
print "OUT"
print p_melody.best(1)[0].resolve(yesterday_combined,tomorrow),"gens:", p_melody.number_of_generations, "melody:",p_melody.most_fit(),"level:",p_melody.best(1)[0].fitness_level
print tomorrow
#w.write([p_melody.best(1)[0].resolve(yesterday_combined,tomorrow)],"output/"+str(p_melody.number_of_generations)+"_final")
w.write([p_melody.best(1)[0].best_path(yesterday_combined,tomorrow,[1,5,10,10])],"output/"+str(p_melody.number_of_generations)+"_path")
