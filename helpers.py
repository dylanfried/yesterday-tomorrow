from math import log,sqrt
from hyphen import Hyphenator
import re


#SYLLABLES = [['Yest', 'er', 'day,'], ['all'], ['my'], ['trou-', 'bles'], ['seemed'], ['so'], ['far'], ['a-', 'way'], ['Now'], ['it'], ['looks'], ['as'], ['though'], ["they're"], ['here'], ['to'], ['stay'], ['oh'], ['I'], ['be-', 'lieve'], ['in'], ['yest-', 'er-', 'day'], ['Sudd-', 'en-', 'ly'], ["I'm"], ['not'], ['half'], ['the'], ['man'], ['I'], ['used'], ['to'], ['be'], ["There's"], 'a', 'shad-', 'ow', 'hang-', 'ing', 'over', 'me', 'Oh', 'yest-', 'er-', 'day', 'came', 'sudd-', 'en-', 'ly.', 'Why', 'she', 'had', 'to', 'go?', 'I', "don't", 'know', 'she', 'would-', "n't", 'say', 'I', 'said', 'some-', 'thing', 'wrong', 'Now', 'I', 'long', 'for', 'yest-', 'er-', 'day.', 'yest-', 'er-', 'day', 'love', 'was', 'such', 'an', 'easy', 'game', 'to', 'play', 'Now', 'I', 'need', 'a', 'place', 'to', 'hide', 'a-', 'way', 'Oh', 'I', 'be-', 'lieve', 'in', 'yest-', 'er-', 'day.', 'Why', 'did', 'she', 'have', 'to', 'go?', 'I', "don't", 'know', 'she', 'would-', "n't", 'say', 'I', 'said', 'some-', 'thing', 'wrong', 'Now', 'I', 'long', 'for', 'yest-', 'er-', 'day.', 'Yest-', 'er-', 'day', 'love', 'was', 'such', 'an', 'eas-', '-y', 'game', 'to', 'play', 'Now', 'I', 'need', 'a', 'place', 'to', 'hide', 'a-', 'way', 'Oh', 'I', 'be-', 'lieve', 'in', 'yest-', 'er-', 'day', 'The', "sun'll", 'come', 'out', 'To-', 'morr-', 'ow', 'Bet', 'your', 'bott-', 'om', 'doll-', 'ar', 'That', 'to-', 'mor-', 'row', "There'll", 'be', 'sun!', 'Just', 'thin-', "kin'", 'a-', 'bout', 'To-', 'mor-', 'row', 'Clears', 'away', 'the', 'cob-', 'webs,', 'And', 'the', 'sor-', 'row', "'Til", "there's", 'none!', 'When', "I'm", 'stuck', 'a day', "That's", 'gray,', 'And', 'lone-', 'ly,', 'I', 'just', 'stick', 'out', 'my', 'chin', 'And', 'Grin,', 'And', 'Say,', 'Oh!', 'The', "sun'll", 'come', 'out', 'To-', 'mor-', 'row', 'So', 'ya', 'got-', 'ta', 'hang', 'on', "'Til", 'to-', 'morr-', 'ow', 'Come', 'what', 'may', 'To-', 'morr-', 'ow!', 'To-', 'morr-', 'ow!', 'I', 'love', 'ya', 'To-', 'morr-', 'ow!', "You're", 'al-', 'ways', 'A', 'day', 'A', 'way!']
yesterday_lyrics = u"Yesterday, all my troubles seemed so far away Now it looks as though they're here to stay Oh, I believe in yesterday Suddenly, I'm not half the man I used to be There's a shadow hanging over me. Oh, I yesterday came suddenly Why she had to go I don't know she wouldn't say I said something wrong, now I long for yesterday Yesterday, love was such an easy game to play Now I need a place to hide away Oh, I believe in yesterday Why she had to go I don't know she wouldn't say I said something wrong, now I long for yesterday Yesterday, love was such an easy game to play Now I need a place to hide away Oh, I believe in yesterday"
tomorrow_lyrics = u"The sun'll come out tomorrow Bet your bottom dollar that tomorrow there'll be sun Just thinkin' about tomorrow Clears away the cobwebs and the sorrow till' there's none When I'm stuck in the day that's grey and lonely I just stick up my chin and grin and say oh The sun'll come out tomorrow So you got to hang on till' tomorrow, come what may! Tomorrow, tomorrow, I love you, tomorrow You're only a day away! When I'm stuck with a day that's gray and lonely I just stick up my chin and grin and say The sun'll come out tomorrow So you got to hang on till' tomorrow, come what may! Tomorrow, tomorrow, I love you tomorrow You're only a day away Tomorrow, tomorrow I love you tomorrow You're always a day away"

SYLLABLES = [[u'Yes', u'ter', u'day,'], [u'all'], [u'my'], [u'trou', u'bles'], [u'seemed'], [u'so'], [u'far'], [u'away'], [u'Now'], [u'it'], [u'looks'], [u'as'], [u'though'], [u'they', u"'re"], [u'here'], [u'to'], [u'stay'], [u'Oh,'], [u'I'], [u'be', u'lieve'], [u'in'], [u'yes', u'ter', u'day'], [u'Sud', u'den', u'ly,'], [u"I'm"], [u'not'], [u'half'], [u'the'], [u'man'], [u'I'], [u'used'], [u'to'], [u'be'], [u"There's"], [u'a'], [u'shadow'], [u'hang', u'ing'], [u'over'], [u'me.'], [u'Oh,'], [u'I'], [u'yes', u'ter', u'day'], [u'came'], [u'sud', u'denly'], [u'Why'], [u'she'], [u'had'], [u'to'], [u'go'], [u'I'], [u"don't"], [u'know'], [u'she'], [u"wouldn't"], [u'say'], [u'I'], [u'said'], [u'some', u'thing'], [u'wrong,'], [u'now'], [u'I'], [u'long'], [u'for'], [u'yes', u'ter', u'day'], [u'Yes', u'ter', u'day,'], [u'love'], [u'was'], [u'such'], [u'an'], [u'easy'], [u'game'], [u'to'], [u'play'], [u'Now'], [u'I'], [u'need'], [u'a'], [u'place'], [u'to'], [u'hide'], [u'away'], [u'Oh,'], [u'I'], [u'be', u'lieve'], [u'in'], [u'yes', u'ter', u'day'], [u'Why'], [u'she'], [u'had'], [u'to'], [u'go'], [u'I'], [u"don't"], [u'know'], [u'she'], [u"wouldn't"], [u'say'], [u'I'], [u'said'], [u'some', u'thing'], [u'wrong,'], [u'now'], [u'I'], [u'long'], [u'for'], [u'yes', u'ter', u'day'], [u'Yes', u'ter', u'day,'], [u'love'], [u'was'], [u'such'], [u'an'], [u'easy'], [u'game'], [u'to'], [u'play'], [u'Now'], [u'I'], [u'need'], [u'a'], [u'place'], [u'to'], [u'hide'], [u'away'], [u'Oh,'], [u'I'], [u'be', u'lieve'], [u'in'], [u'yes', u'ter', u'day'],[u'The'], [u'sun', u"'ll"], [u'come'], [u'out'], [u'to', u'mor', u'row'], [u'Bet'], [u'your'], [u'bot', u'tom'], [u'dol', u'lar'], [u'that'], [u'to', u'mor', u'row'], [u'there', u"'ll"], [u'be'], [u'sun'], [u'Just'], [u"thinkin'"], [u'about'], [u'to', u'mor', u'row'], [u'Clears'], [u'away'], [u'the'], [u'cob', u'webs'], [u'and'], [u'the'], [u'sor', u'row'], [u"till'"], [u"there's"], [u'none'], [u'When'], [u"I'm"], [u'stuck'], [u'in'], [u'the'], [u'day'], [u"that's"], [u'grey'], [u'and'], [u'lonely'], [u'I'], [u'just'], [u'stick'], [u'up'], [u'my'], [u'chin'], [u'and'], [u'grin'], [u'and'], [u'say'], [u'oh'], [u'The'], [u'sun', u"'ll"], [u'come'], [u'out'], [u'to', u'mor', u'row'], [u'So'], [u'you'], [u'got'], [u'to'], [u'hang'], [u'on'], [u"till'"], [u'to', u'mor', u'row,'], [u'come'], [u'what'], [u'may!'], [u'To', u'mor', u'row,'], [u'to', u'mor', u'row,'], [u'I'], [u'love'], [u'you,'], [u'to', u'mor', u'row'], [u'You', u"'re"], [u'only'], [u'a'], [u'day'], [u'away!'], [u'When'], [u"I'm"], [u'stuck'], [u'with'], [u'a'], [u'day'], [u"that's"], [u'gray'], [u'and'], [u'lonely'], [u'I'], [u'just'], [u'stick'], [u'up'], [u'my'], [u'chin'], [u'and'], [u'grin'], [u'and'], [u'say'], [u'The'], [u'sun', u"'ll"], [u'come'], [u'out'], [u'to', u'mor', u'row'], [u'So'], [u'you'], [u'got'], [u'to'], [u'hang'], [u'on'], [u"till'"], [u'to', u'mor', u'row,'], [u'come'], [u'what'], [u'may!'], [u'To', u'mor', u'row,'], [u'to', u'mor', u'row,'], [u'I'], [u'love'], [u'you'], [u'to', u'mor', u'row'], [u'You', u"'re"], [u'only'], [u'a'], [u'day'], [u'away'], [u'To', u'mor', u'row,'], [u'to', u'mor', u'row'], [u'I'], [u'love'], [u'you'], [u'to', u'mor', u'row'], [u'You', u"'re"], [u'al', u'ways'], [u'a'], [u'day'], [u'away']]

def get_syllables(lyrics):
    h = Hyphenator()
    syllables = []
    for word in lyrics.split(" "):
        syl = h.syllables(word)
        if syl:
            syllables.append(syl)
        else:
            syllables.append([word])
    return syllables

def assign_syllables(melody,lyrics):
    melody_syllables = get_syllables(lyrics)
    new_melody = []
    for i in range(len(melody)):
        new_melody.append((melody[i][0],melody[i][1],[]))
    i = 0
    j = 0
    while i < len(new_melody) and j < len(melody_syllables):
        new_melody[i] = (new_melody[i][0],new_melody[i][1],melody_syllables[j])
        i += len(melody_syllables[j])
        j += 1
    return new_melody

def generate_lyrics(melody):
    # First calculate how many said notes there are
    length = len([n for n in melody if n[0] != 0])
    lyrics = lyrics_test.generate_lyrics(length)
    for i in range(len(melody)):
        if melody[i][0] != 0:
            melody[i] = (melody[i][0],melody[i][1],lyrics[i])

def shift(l, n):
    return l[n:] + l[:n]

def get_intervals(sequence):
    to_return = []
    for i in range(len(sequence)-1):
        to_return.append(sequence[i+1]-sequence[i])
    return to_return


keys_s = ('C', '^C', 'D', '^D', 'E', 'F', '^F', 'G', '^G','A', '^A', 'B','c', '^c', 'd', '^d', 'e', 'f', '^f', 'g', '^g','a', '^a', 'b')
#yesterday = "g/2 f/4 f13/4 z a/2 b/2 ^c/4 d3/4 e/2 f/2 e3/2 d/2 d2 z d/2 d/4 c'/2 ^a/2 =a3/4 g/2 ^a =a/2 a3/2 z/2 g/2 f a/2 g3/2 z/2 d/2 f a/2 a5/2 g/2 f/4 f13/4 z a/2 b/2 ^c/2 d/4 e3/4 f/2 e/2 d/4 d13/4 z d/4 d/2 c'/2 ^a3/4 =a/2 g/2 ^a =a/2 a3/2 z/2 g/2 f a/2 g3/2 z/2 d/2 f a/2 a5/2 a2 a2 d e f e/2 d e d/2 c' d/2 a7/2 z a2 a2 d e f e/2 d e d/2 c' e f4 g/2 f/4 f13/4 z a/2 b/2 ^c/4 d3/4 e/2 f/2 e3/2 d/2 d2 z d/2 d/4 c'/2 ^a/2 =a3/4 g/2 ^a =a/2 a3/2 z/2 g/2 f a/2 g3/2 z/2 d/2 f a/2 a5/2 a2 a2 d e f e/2 d e d/2 c' d/2 a7/2 z a2 a2 d e f e/2 d e d/2 c' e f c' ^a =a g/2 f/4 f13/4 z a/2 b/2 ^c/4 d3/4 e/2 f/2 e3/2 d/2 d2 z d/2 d/4 c'/2 ^a/2 =a3/4 g/2 ^a =a/2 a3/2 z/2 g/2 f a/2 g3/2 z/2 d/2 f a/2 a5/2 f9/8 a9/8 g9/8 d z/8 f a5/8 a29/4"
yesterday = "d/2 c/4 c3/1 z e/2 ^f/2 ^g/4 a3/4 b/2 c'/2 b3/2 a/2 a2 z a/2 a/4 =g/2 =f/2 e3/4 d/2 f e/2 e3/2 z/2 d/2 c e/2 d3/2 z/2 A/2 c e/2 e5/2 d/2 c/4 c3/1 z e/2 ^f/2 ^g/2 a/4 b3/4 c'/2 b/2 a/4 a3/1 z a/4 a/2 =g/2 =f3/4 e/2 d/2 f e/2 e3/2 z/2 d/2 c e/2 d3/2 z/2 A/2 c e/2 e5/2 e2 e2 a b c' b/2 a b a/2 g a/2 e7/2 z e2 e2 a b c' b/2 a b a/2 g b c'4 d/2 c/4 c3/1 z e/2 ^f/2 ^g/4 a3/4 b/2 c'/2 b3/2 a/2 a2 z a/2 a/4 =g/2 =f/2 e3/4 d/2 f e/2 e3/2 z/2 d/2 c e/2 d3/2 z/2 A/2 c e/2 e5/2 e2 e2 a b c' b/2 a b a/2 g a/2 e7/2 z e2 e2 a b c' b/2 a b a/2 g b c' g f e d/2 c/4 c3/1 z e/2 ^f/2 ^g/4 a3/4 b/2 c'/2 b3/2 a/2 a2 z a/2 a/4 =g/2 =f/2 e3/4 d/2 f e/2 e3/2 z/2 d/2 c e/2 d3/2 z/2 A/2 c e/2 e5/2 c9/8 e9/8 d9/8 A z/8 c e5/8 e29/4"
tomorrow = "^A/4 z/8 [G12/8z/4] ^G/8 z/4 ^A3/8 z/4 ^d7/4 z/8 g/2 z/8 f/2 z/8 ^d/2 z3/4 g3/8 z/8 f/8 ^d/2 z/8 =d/2 z/4 c/8 z/8 f5/8 z3/8 d3/8 z/4 ^A3/8 z/4 =G3/8 z/4 ^d23/8 z/4 f3/8 z/4 g3/8 z/4 ^G7/4 z3/1 ^A/4 z/8 [=G12/8z/4] ^G/8 z/4 ^A3/8 z/4 ^d2 z/4 g3/8 z/4 f3/8 z/4 ^d3/8 z7/8 g3/8 z/8 f/8 ^d3/8 z/4 =d/2 z/8 c/4 z/8 f5/8 z/4 d/2 z/8 ^A/2 z/8 =G/2 z/8 ^d3/1 z/4 f3/8 z/4 g3/8 z/4 ^G2 z5/4 ^A/8 z/8 ^A/4 z/8 ^A/2 z/8 ^d/8 z/8 f/2 z/8 ^f5/4 z5/8 ^d/2 z/8 ^f11/8 z5/8 ^d3/8 z/4 ^f3/8 z/4 ^g5/4 z7/8 ^c/4 z/8 ^c/4 ^c5/8 z/8 ^f/8 z/8 ^g3/8 z/4 ^a5/4 z5/8 ^f/2 z/8 ^a5/4 z5/8 ^f3/4 ^a53/8 z17/8 ^A3/4 z/4 ^G/4 z/8 =G3/8 z/8 ^G/8 ^A/2 z/4 ^d15/8 z/4 =g/2 z/8 [=f/2=d/2] z/4 [^d/2=c/2] z7/8 g3/8 z/4 f/8 ^d/2 z/4 =d3/8 z/4 c/2 z/4 f/2 z/4 d3/8 z/4 ^A/2 z/4 =G/2 z/4 ^d11/8 z11/8 f z3/8 g/2 z/4 ^g15/4 z/2 ^a7/8 z/2 c'/2 z/4 ^a7/8 z/2 =g/2 z/4 c'/2 z/8 ^a z/2 g/2 z/8 c'/2 z/4 ^a z3/8 ^d/2 z/4 ^a/2 z/4 ^g7/8 z/2 f/2 z/4 ^g3/8 z/4 =g z/2 ^d3/8 z/4 ^A z3/8 f z/2 ^d3/1"
def midi_to_combined(text):
    combined = []
    for abc in text.split(" "):
        note,time = abc_to_number(abc)
        combined.append((note,time,[]))
    return combined

def abc_to_number(abc):
    #print "-------"
    # First, get octave
    octave = 4
    octave -= abc.count(',')
    octave += abc.count("'")
    # Second, figure out note
    sharp = abc.count("^")
    note = 0
    for i in range(len(keys_s)):
        key = keys_s[i]
        if key in abc:
            note = 1 + i + sharp
            break
    if not note and ('r' in abc or 'z' in abc):
        note = 0
    elif not note:
        print "Couldn't recognize note",abc
    else:
        note = note + 12*octave
    # Now grab the timing
    if "/" in abc:
        #print re.sub(r'([^\d])(\d*/\d*)',"\\2",abc)
        digits = [int(thing.strip("]")) if thing else 1 for thing in re.sub(r'([^\d]*)(\d*/\d*)',"\\2",abc).split("/")]
        #print "digits",digits
    else:
        digits = ["1","1"]
        #print "didnt"
    numerator = float(digits[0])
    denominator = float(digits[1])*4.0
    #print numerator, denominator
    while numerator % 2 == 0 and denominator % 2 == 0:
        numerator /= 2
        denominator /= 2
    odd = False
    if numerator > 1 and numerator % 2 == 1:
        odd = True
        numerator -= 1
    time = int(round(denominator/numerator))
    #print abc, odd
    if odd:
        time *= -1
    #print time,"time"
    return note,time

def make_absolute(combined):
    new_combined = []
    running_total = 0
    for (note,time,syllable) in combined:
        if time > 0:
            running_total += 1.0/time
        else:
            #print (note,time,syllable)
            running_total += 1.0/abs(time) + (1.0/abs(time))/2.0
        new_combined.append((note,running_total,syllable))
    return new_combined

def pad_melodies(melodies):
    absolute_melodies = [make_absolute(m) for m in melodies]
    longest = max([m[-1][1] for m in absolute_melodies])
    padding = []
    #print "longest",longest
    for i in range(len(melodies)):
        #print absolute_melodies[i][-1][1]
        if absolute_melodies[i][-1][1] < longest:
            diff = (longest-absolute_melodies[i][-1][1])/(1.0/64.0)
            #print "appending",diff,"rests"
            placeholder = []
            while diff//64 > 0:
                placeholder.append((0,1,[]))
                diff -= 64
            while diff//32 > 0:
                placeholder.append((0,2,[]))
                diff -= 32
            while diff//16 > 0:
                placeholder.append((0,4,[]))
                diff -= 16
            while diff//8 > 0:
                placeholder.append((0,8,[]))
                diff -= 8
            while diff//4 > 0:
                placeholder.append((0,16,[]))
                diff -= 4
            while diff//2 > 0:
                placeholder.append((0,32,[]))
                diff -= 2
            while diff > 0:
                placeholder.append((0,64,[]))
                diff -= 1
            #print placeholder
            #if int(diff) != diff:
            #    # Need to add a half rest in there
            #    melodies[i].append((0,-32))
            #    diff -= 1.5
            #for j in range(int(diff)):
            #    placeholder.append((0,64,''))
            padding.append(placeholder)
        else:
            padding.append([])
    return padding
    
def nearest_pow_of_2(n):
    #print "n",n
    return pow(2, int(log(n, 2) + 0.5))

def get_weighted(i,length,population):
    return population
    my_percent = float(i)/float(length)
    new_population = []
    for j in range(len(population)):
        their_percent = float(j)/float(len(population))
        for k in range(int(5*(1-abs(my_percent-their_percent)))):
            new_population.append(population[j])
    return new_population

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)
