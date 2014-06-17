import pysynth
import datetime
from string import Template
import subprocess

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
            $staves
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
                tempoWholesPerMinute = #(ly:make-moment 130 4)
            }
        }
        \layout {}
    }
    """
    STAFF_TEMPLATE = """
        \\new Staff
        {
            \set Staff.midiInstrument = #"$instrument"
            \\time 4/4
            \clef treble
            {
                $melody
            }
            \\addlyrics { $lyrics }
        }
    """
    keys_s = ('a', 'ais', 'b', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis')
    def write(self,melodies, title):
        created_on = datetime.datetime.today()
        staves = []
        instruments = ['piano','cello']
        for i in range(len(melodies)):
            melody = melodies[i]
            instrument = instruments[i]
            abc_notation = []
            lyrics = []
            
            # keep a running time total for inserting bars
            running_time = 0
            
            for i in range(len(melody)):
                if isinstance(melody[i],tuple):
                    note = melody[i][0]
                    note_time = melody[i][1]
                else:
                    note = melody[i]
                    note_time = 4
                if note_time > 0:
                    running_time += 1.0/note_time
                else:
                    running_time += 1.0/abs(note_time) + (1.0/abs(note_time))/2.0
                if note_time < 0:
                    note_time = str(abs(note_time)) + "."
                else:
                    note_time = str(note_time)
                lyrics.append(" ".join(melody[i][2]))
                abc_notation.append(self.number_to_abc(note) + note_time)
                if running_time >= 1:
                    running_time = 0
                    abc_notation.append('\\bar ""')
            print "ABC to write:",abc_notation
            staff = Template(self.STAFF_TEMPLATE)
            staves.append(staff.substitute({'melody':" ".join(abc_notation),'instrument':instrument,'lyrics':" ".join(lyrics)}))
        # Print out combined and separate music
        for i in range(len(staves)):
            # First
            context = {}
            context['title'] = title + " Part " + str(i)
            context['created_on'] = created_on.strftime('%c')
            context['staves'] = staves[i]
            score = Template(self.TEMPLATE)
            score = score.substitute(context)
            f = open(title + "_" + created_on.strftime('%m-%d-%H%M%S') + "_PART" + str(i) + ".ly","wb")
            f.write(score)
            f.close()
            print f.name
            subprocess.call("lilypond " + f.name,shell=True)
        # Combined
        context = {}
        context['title'] = title
        context['created_on'] = created_on.strftime('%c')
        context['staves'] = " ".join(staves)
        score = Template(self.TEMPLATE)
        score = score.substitute(context)
        f = open(title + "_" + created_on.strftime('%m-%d-%H%M%S')+ "_COMBINED_"  + ".ly","wb")
        f.write(score)
        f.close()
        print f.name
        subprocess.call("lilypond " + f.name,shell=True)
    
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
