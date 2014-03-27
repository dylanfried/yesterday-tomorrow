import pysynth

class WAVWriter:
    keys_s = ('a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#')
    def __init__(self):
        pass
    def write(self, melody,title,times=None):
        abc_notation = []
        for i in range(len(melody)):
            if isinstance(melody[i],tuple):
                note = melody[i][0]
                note_time = melody[i][1]
            else:
                note = melody[i]
                if times:
                    note_time = times[i]
                    if note_time == 0:
                        note_time = 4
                else:
                    note_time = 4
            abc_notation.append((self.number_to_abc(note),note_time))
        print "ABC to write:",abc_notation
        pysynth.make_wav(abc_notation,fn=title)
    def number_to_abc(self,number):
        if number == 0:
            return 'r'
        octave = (number+9) // 12
        note = '%s%u' % (self.keys_s[number%12], octave)
        return note
