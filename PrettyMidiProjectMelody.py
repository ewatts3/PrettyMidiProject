import pretty_midi
import random

# Create a PrettyMIDI object
#cello_c_chord = pretty_midi.PrettyMIDI()
# Create an Instrument instance for a cello instrument
#cello_program = pretty_midi.instrument_name_to_program('Cello')
#cello = pretty_midi.Instrument(program=cello_program)
# Iterate over note names, which will be converted to note number later
#for note_name in ['C5', 'E5', 'G5']:
    # Retrieve the MIDI note number for this note name
#    note_number = pretty_midi.note_name_to_number(note_name)
    # Create a Note instance, starting at 0s and ending at .5s
#    note = pretty_midi.Note(
#        velocity=100, pitch=note_number, start=0, end=.5)
    # Add it to our cello instrument
#    cello.notes.append(note)
# Add the cello instrument to the PrettyMIDI object
#cello_c_chord.instruments.append(cello)
# Write out the MIDI data
#cello_c_chord.write('cello-C-chord.mid')

#############################################

#monophonic / one line / no repeats
pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

time = 0

notes = ['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C4']
isARepeat = True
lastNote = "H"

for each in range(480):
    while isARepeat:
        noteName = notes[random.randint(0, 6)]
        if noteName == lastNote:
            isARepeat = True
        else:
            isARepeat = False

    note_number = pretty_midi.note_name_to_number(noteName)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=(time + .125))
    cello.notes.append(note)

    lastNote = noteName
    isARepeat = True
    time = time + .125

pm.instruments.append(cello)
pm.write('output.mid')