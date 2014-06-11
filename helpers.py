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
    for (note,time) in combined:
        if time > 0:
            running_total += 1.0/time
        else:
            running_total += 1.0/abs(time) + (1.0/abs(time))/2.0
        new_combined.append((note,running_total))
    return new_combined

def pad_melodies(melodies):
    absolute_melodies = [make_absolute(m) for m in melodies]
    longest = max([m[-1][1] for m in absolute_melodies])
    print "longest",longest
    for i in range(len(melodies)):
        print absolute_melodies[i][-1][1]
        if absolute_melodies[i][-1][1] < longest:
            print "appending",(0,int(1.0/(longest-absolute_melodies[i][-1][1])))
            melodies[i].append((0,int(1.0/(longest-absolute_melodies[i][-1][1]))))
    return melodies
