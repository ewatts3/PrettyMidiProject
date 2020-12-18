import pretty_midi
import decimal

pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

note = pretty_midi.Note(velocity=100,
                        pitch=55,
                        start=0,
                        end=30)
cello.notes.append(note)
#cello.pitch_bends.append(pretty_midi.PitchBend(8191, 5))

time = 0

for each in range(0, 8191):
    cello.pitch_bends.append(pretty_midi.PitchBend(each, time))
    time = time + .03

# We'll just do a 1-semitone pitch ramp up
#n_steps = 512
#bend_range = 8192#2
#for time, pitch in zip(np.linspace(1.5, 2.3, n_steps), range(0, bend_range, bend_range)): #//n_steps
#    cello.pitch_bends.append(pretty_midi.PitchBend(pitch, time))

#learning how to pitch bend

pm.instruments.append(cello)
pm.write('output.mid')

