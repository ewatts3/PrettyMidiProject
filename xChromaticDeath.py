import pretty_midi
#import random
#import decimal

pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

#start = 0

#for each in range(1, 999):
#    note = pretty_midi.Note(velocity=99, 
#                            pitch=pretty_midi.hz_to_note_number(float(each)), 
#                            start=start, 
#                           end=start + 1)
#    cello.notes.append(note)
#    start = start + 1

print(int(pretty_midi.hz_to_note_number(200)))
print(int(pretty_midi.hz_to_note_number(201)))
print(int(pretty_midi.hz_to_note_number(202)))
print(int(pretty_midi.hz_to_note_number(203)))
print(int(pretty_midi.hz_to_note_number(204)))
print(int(pretty_midi.hz_to_note_number(205)))
print(int(pretty_midi.hz_to_note_number(206)))
print(int(pretty_midi.hz_to_note_number(207)))
print(int(pretty_midi.hz_to_note_number(208)))
print(int(pretty_midi.hz_to_note_number(209)))
print(int(pretty_midi.hz_to_note_number(210)))

note = pretty_midi.Note(velocity=100, 
                        pitch=pretty_midi.hz_to_note_number(200), 
                        start=0, 
                        end=10)
cello.notes.append(note)
pm.instruments.append(cello)
#pm.write('output.mid')