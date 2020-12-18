import pretty_midi
import random
import decimal

#creates a full composition drawing from notes in a certain key over the full range
#specify quanity of notes and length of piece

pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for each in range(10000):
    noteName = (notes[random.randint(0, 6)] + str(random.randint(2,6)))
    note_number = pretty_midi.note_name_to_number(noteName)
    start = float(decimal.Decimal(random.randrange(0, 60000))/100) #600 seconds = 10 min
    note = pretty_midi.Note(velocity=(random.randint(0, 127)), 
                            pitch=note_number, 
                            start=start, 
                            end=float(decimal.Decimal(random.randrange(int(start), 60000))/100))
    cello.notes.append(note)

pm.instruments.append(cello)
pm.write('outputs.mid')
