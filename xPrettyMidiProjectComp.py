import pretty_midi
import random

pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

time = 0
notes = ['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
isARepeat = True
lastNote = "H"

while time < 60:
    while isARepeat:
        noteName = notes[random.randint(0, 6)]
        if noteName == lastNote:
            isARepeat = True
        else:
            isARepeat = False

    note_number = pretty_midi.note_name_to_number(noteName)
    length = 2 + (.125 * random.randint(0, 32))
    print(length)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=(time + length))
    cello.notes.append(note)

    lastNote = noteName
    isARepeat = True
    time = time + length

pm.instruments.append(cello)
pm.write('output.mid')
