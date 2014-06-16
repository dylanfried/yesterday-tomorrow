from math import log

SYLLABLES = ['Yest', 'er', 'day,', 'all', 'my', 'trou-', 'bles', 'seemed', 'so', 'far', 'a-', 'way', 'Now', 'it', 'looks', 'as', 'though', "they're", 'here', 'to', 'stay', 'oh', 'I', 'be-', 'lieve', 'in', 'yest-', 'er-', 'day', 'Sudd-', 'en-', 'ly', "I'm", 'not', 'half', 'the', 'man', 'I', 'used', 'to', 'be', "There's", 'a', 'shad-', 'ow', 'hang-', 'ing', 'over', 'me', 'Oh', 'yest-', 'er-', 'day', 'came', 'sudd-', 'en-', 'ly.', 'Why', 'she', 'had', 'to', 'go?', 'I', "don't", 'know', 'she', 'would-', "n't", 'say', 'I', 'said', 'some-', 'thing', 'wrong', 'Now', 'I', 'long', 'for', 'yest-', 'er-', 'day.', 'yest-', 'er-', 'day', 'love', 'was', 'such', 'an', 'easy', 'game', 'to', 'play', 'Now', 'I', 'need', 'a', 'place', 'to', 'hide', 'a-', 'way', 'Oh', 'I', 'be-', 'lieve', 'in', 'yest-', 'er-', 'day.', 'Why', 'did', 'she', 'have', 'to', 'go?', 'I', "don't", 'know', 'she', 'would-', "n't", 'say', 'I', 'said', 'some-', 'thing', 'wrong', 'Now', 'I', 'long', 'for', 'yest-', 'er-', 'day.', 'Yest-', 'er-', 'day', 'love', 'was', 'such', 'an', 'eas-', '-y', 'game', 'to', 'play', 'Now', 'I', 'need', 'a', 'place', 'to', 'hide', 'a-', 'way', 'Oh', 'I', 'be-', 'lieve', 'in', 'yest-', 'er-', 'day', 'The', "sun'll", 'come', 'out', 'To-', 'morr-', 'ow', 'Bet', 'your', 'bott-', 'om', 'doll-', 'ar', 'That', 'to-', 'mor-', 'row', "There'll", 'be', 'sun!', 'Just', 'thin-', "kin'", 'a-', 'bout', 'To-', 'mor-', 'row', 'Clears', 'away', 'the', 'cob-', 'webs,', 'And', 'the', 'sor-', 'row', "'Til", "there's", 'none!', 'When', "I'm", 'stuck', 'a day', "That's", 'gray,', 'And', 'lone-', 'ly,', 'I', 'just', 'stick', 'out', 'my', 'chin', 'And', 'Grin,', 'And', 'Say,', 'Oh!', 'The', "sun'll", 'come', 'out', 'To-', 'mor-', 'row', 'So', 'ya', 'got-', 'ta', 'hang', 'on', "'Til", 'to-', 'morr-', 'ow', 'Come', 'what', 'may', 'To-', 'morr-', 'ow!', 'To-', 'morr-', 'ow!', 'I', 'love', 'ya', 'To-', 'morr-', 'ow!', "You're", 'al-', 'ways', 'A', 'day', 'A', 'way!']

def shift(l, n):
    return l[n:] + l[:n]

def get_intervals(sequence):
    to_return = []
    for i in range(len(sequence)-1):
        to_return.append(sequence[i+1]-sequence[i])
    return to_return
    
def midi_to_combined(midifile):
    pass

def make_absolute(combined):
    new_combined = []
    running_total = 0
    for (note,time,syllable) in combined:
        if time > 0:
            running_total += 1.0/time
        else:
            running_total += 1.0/abs(time) + (1.0/abs(time))/2.0
        new_combined.append((note,running_total,syllable))
    return new_combined

def pad_melodies(melodies):
    absolute_melodies = [make_absolute(m) for m in melodies]
    longest = max([m[-1][1] for m in absolute_melodies])
    padding = []
    print "longest",longest
    for i in range(len(melodies)):
        print absolute_melodies[i][-1][1]
        if absolute_melodies[i][-1][1] < longest:
            diff = (longest-absolute_melodies[i][-1][1])/(1.0/64.0)
            print "appending",diff,"rests"
            placeholder = []
            while diff//64 > 0:
                placeholder.append((0,1,''))
                diff -= 64
            while diff//32 > 0:
                placeholder.append((0,2,''))
                diff -= 32
            while diff//16 > 0:
                placeholder.append((0,4,''))
                diff -= 16
            while diff//8 > 0:
                placeholder.append((0,8,''))
                diff -= 8
            while diff//4 > 0:
                placeholder.append((0,16,''))
                diff -= 4
            while diff//2 > 0:
                placeholder.append((0,32,''))
                diff -= 2
            while diff > 0:
                placeholder.append((0,64,''))
                diff -= 1
            print placeholder
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
    print "n",n
    return pow(2, int(log(n, 2) + 0.5))
