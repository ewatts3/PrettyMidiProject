import pretty_midi
import random
import decimal

pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
accidentals = ['b', '#']
accidental = 1

for each in range(2500):
    accidental = random.randint(0, 19)
    if accidental is not 0:
        noteName = (notes[random.randint(0, 6)] + str(random.randint(2,6)))
    else:
        noteName = (notes[random.randint(0, 6)] + accidentals[random.randint(0, 1)] + str(random.randint(2,6)))
    note_number = pretty_midi.note_name_to_number(noteName)
    start = float(decimal.Decimal(random.randrange(0, 60000))/100) #600 seconds = 10 min
    note = pretty_midi.Note(velocity=(random.randint(0, 127)), 
                            pitch=note_number, 
                            start=start, 
                            end=float(decimal.Decimal(random.randrange(int(start), 60000))/100))
    cello.notes.append(note)

#an attempt to create a full piece that primarily draws from a key but adds some accidentals
#specify length of piece and number of notes

pm.instruments.append(cello)
pm.write('output.mid')

