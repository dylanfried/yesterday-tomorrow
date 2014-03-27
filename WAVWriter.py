import pysynth
import datetime
from string import Template

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

class LilyWriter:
    TEMPLATE = """
    \\version "2.14.2"
    
    \header {
        title = "$title"
        subtitle = "Created on: $created_on"
        composer = "Dylan"
    }
    
    result = {
        <<
        \\new Staff
        {
            \\time 4/4
            \clef treble
            {
                $melody
            }
        }
        >>
    }
    
    \paper {
        raggedbottom = ##t
        indent = 7. \mm
        linewidth = 183.5 \mm
        betweensystemspace = 25\mm
        betweensystempadding = 0\mm
    }
    
    \score{
        \\result
        \midi {
            \context {
                \Score
                tempoWholesPerMinute = #(ly:make-moment 160 4)
            }
        }
        \layout {}
    }
    """
    keys_s = ('a', 'ais', 'b', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis')
    def write(self,melody, title):
        created_on = datetime.datetime.today()
        
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
            if note_time < 0:
                note_time = str(abs(note_time)) + "."
            else:
                note_time = str(note_time)
            abc_notation.append(self.number_to_abc(note) + note_time)
        print "ABC to write:",abc_notation
        
        context = {}
        context['title'] = title
        context['created_on'] = created_on.strftime('%c')
        context['melody'] = " ".join(abc_notation)
        # Sanity check...
        score = Template(self.TEMPLATE)
        score = score.substitute(context)
        
        f = open(title + ".ly","wb")
        f.write(score)
        f.close()
    
    def number_to_abc(self,number):
        if number == 0:
            return 'r'
        octave = (number+9) // 12
        note = '%s' % (self.keys_s[number%12])
        if octave > 4:
            for i in range(octave-4):
                note += "'"
        elif octave < 4:
            for i in range(4 - octave):
                note += ","
        return note
