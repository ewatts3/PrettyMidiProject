import pretty_midi
import random
import decimal

#creates a full composition drawing from all notes over the full range
#specify quanity of notes and length of piece

pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
accidentals = ['', 'b', '#']

for each in range(2500):
    #noteName = (notes[random.randint(0, 6)] + accidentals[random.randint(0, 2)] + str(random.randint(2,6)))
    #note_number = pretty_midi.note_name_to_number(noteName)
    start = float(decimal.Decimal(random.randrange(0, 60000))/100)
    note = pretty_midi.Note(velocity=(random.randint(0, 127)), 
                            pitch=random.randint(0, 127), 
                            start=start, 
                            end=float(decimal.Decimal(random.randrange(int(start), 60000))/100))
    cello.notes.append(note)

pm.instruments.append(cello)
pm.write('output.mid')