import math

class note:
    baseFrequency=0
    octave=0
    letter=0
    length=0
    def __init__(self, o):
        self.octave = o
    def calculate(self, x):
        frequency = self.baseFrequency*(2**self.octave)
        length = round(1000/frequency, 3)
        global dl
        dl = round(length, 3)
        df = round(frequency, 3)
        output = f"{x}<x<={round(dl+x,3)}:{df},"
        notes_range.append(output)
        return output
        
class C(note):
    baseFrequency = 16.35
    letter = "C"  
class CHash(note):
    baseFrequency = 17.32
    letter = "C#"
class D(note):
    baseFrequency = 18.35
    letter = "D" 
class DHash(note):
    baseFrequency = 19.45
    letter = "D#"
class E(note):
    baseFrequency = 20.6
    letter = "E" 
class F(note):
    baseFrequency = 21.83
    letter = "F"  
class FHash(note):
    baseFrequency = 23.12
    letter = "F#"  
class G(note):
    baseFrequency = 24.5
    letter = "G"
class GHash(note):
    baseFrequency = 25.96
    letter = "G#"
class A(note):
    baseFrequency = 27.5
    letter = "A"
class AHash(note):
    baseFrequency = 29.14
    letter = "A#"
class B(note):
    baseFrequency = 30.87
    letter = "B"
 
def desmos_note(sound,x_value): 
    octave = int(sound[-1])
    note_sign = sound[:-1]
    print(note_sign)
    if (note_sign == "c"):
        c = C(octave)
        notes.update({note_sign+str(octave) : c.calculate(x_value)})
        return "c#" + str(octave)
    elif (note_sign == "c#"):
        cH = CHash(octave)
        notes.update({note_sign+str(octave) : cH.calculate(x_value)})
        return "d" + str(octave)
    elif (note_sign == "d"):
        d = D(octave)
        notes.update({note_sign+str(octave) : d.calculate(x_value)})
        return "d#" + str(octave)
    elif (note_sign == "d#"):
        dH = DHash(octave)
        notes.update({note_sign+str(octave) : dH.calculate(x_value)})
        return "e" + str(octave)
    elif (note_sign == "e"):
        e = E(octave)
        notes.update({note_sign+str(octave) : e.calculate(x_value)})
        return "f" + str(octave)
    elif (note_sign == "f"):
        f = F(octave)
        notes.update({note_sign+str(octave) : f.calculate(x_value)})
        return "f#" + str(octave)
    elif (note_sign == "f#"):
        fH = FHash(octave)
        notes.update({note_sign+str(octave) : fH.calculate(x_value)})
        return "g" + str(octave)
    elif (note_sign == "g"):
        g = G(octave)
        notes.update({note_sign+str(octave) : g.calculate(x_value)})
        return "g#" + str(octave)
    elif (note_sign == "g#"):
        gH = GHash(octave)
        notes.update({note_sign+str(octave) : gH.calculate(x_value)})
        return "a" + str(octave)
    elif (note_sign == "a"):
        a = A(octave)
        notes.update({note_sign+str(octave) : a.calculate(x_value)})
        return "a#" + str(octave)
    elif (note_sign == "a#"):
        aH = AHash(octave)
        notes.update({note_sign+str(octave) : aH.calculate(x_value)})
        return "b" + str(octave)
    elif (note_sign == "h" or note_sign =="b"):
        b = B(octave)
        notes.update({note_sign+str(octave) : b.calculate(x_value)})
        return "c" + str((octave+1))
    return 
  
def prep_notes(start,end):
    x=0
    global notes, notes_range
    notes = {}
    notes_range = ["0=x:0,"]
    
    while start != end:
        start = desmos_note(start,x)
        x=round(x+dl, 3)
    print(" ")
    # print("zakres nut >>")
    # print(notes)
    print("desmos input >>")
    print("Definition of diffrent notes frequencies from given range:   f(x) = {",end="")
    for a in range(len(notes_range)):
        print(f"{notes_range[a].strip("'")}",sep=",",end=" ")
        a+=1
    print("}",end="")
    print(" ")
          
def song_maker():
    print(" ")
    print("NOTE: THIS CALCULATOR TAKES NOTES IN LETTER NOTATION AND WITH THE OCTAVE NUMBER!!!")
    print("example: c2, e6, a#4, f#1")
    print(" ")
    start = input("""enter the start of the note ferquencies definition (the lowest used sound in the song):
    """)
    if start[:-1] == "h":
        octave = start[-1]
        start = "b" + octave 
    start = start.lower()
    end = input("""enter the note after the highest note used in the song:
    """)
    if end[:-1] == "h":
        octave = end[-1]
        end = "b" + octave 
    end = end.lower()
    prep_notes(start,end)  
    notes_output = [0]
    while 1:
        _input = input(
    """enter one or multiple notes separated with commas (',')
    -if u want to add additional brakes in between the sounds enter 'p'
    -if u want to end the input enter '0':
    """)
        _input = _input.lower()
        list = _input.split(",")
        for element in list:
            element = element.strip()
            if element == "p":
                notes_output.append(0)
        
            if element[:-1] == "h":
                octave = element[-1]
                element = "b" + octave 

            klucze = notes.keys()
            for k in klucze:
                if element == k: 
                    notes_output.append(float(notes[k][(notes[k].find("<="))+2:notes[k].find(":")]))
                    notes_output.append(0)
                    break
        if element == "0" or list[-1] == "0":
            break
    print(" ")
    print(f"List of note definitions:   a={notes_output}")
    a = ""
    x = len(notes_output)/300
    range_length = len(notes_output)/math.ceil(x)
    for i in range(math.ceil(x)):
        a += chr(105+i)
        if (i!= math.ceil(x)-1):
            a += "+"
    print(f"List of iterators:   a[{a}]")
    print(f"Tone function:   tone(f(a[{a}]))")  
    print(f"Total lenght of the list with notes:   {len(notes_output)} ")
    print(f"Length of smaller segments for iterator ranges:   {math.ceil(range_length)}")      
    print(" ")
  
  
song_maker() 


x = input("Hit Enter to Exit, or Input any other key to continue ")

if not x :
    print("Exiting the Program.")
    exit()
