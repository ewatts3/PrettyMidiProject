import pretty_midi
import decimal

pm = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)

#C4
one = pretty_midi.Note(velocity=100,
                        pitch=60,
                        start=0,
                        end=5)
#no bend needed

two = pretty_midi.Note(velocity=100,
                       pitch=62,
                       start=5,
                       end=10)
twoPitchBend = pretty_midi.PitchBend(1394, 5)
twoPitchBendRevert = pretty_midi.PitchBend(-1394, 10)

three = pretty_midi.Note(velocity=100,
                       pitch=64,
                       start=10,
                       end=15)
threePitchBend = pretty_midi.PitchBend(2870, 10)
threePitchBendRevert = pretty_midi.PitchBend(-2870, 15)

five = pretty_midi.Note(velocity=100,
                       pitch=67,
                       start=15,
                       end=20)
fivePitchBend = pretty_midi.PitchBend(1517, 15)
fivePitchBendRevert = pretty_midi.PitchBend(-1517, 20)

six = pretty_midi.Note(velocity=100,
                       pitch=69,
                       start=20,
                       end=25)
sixPitchBend = pretty_midi.PitchBend(2820, 20)
sixPitchBendRevert = pretty_midi.PitchBend(-2820, 25)

eight = pretty_midi.Note(velocity=100,
                       pitch=72,
                       start=25,
                       end=30)
eightPitchBend = pretty_midi.PitchBend(451, 25)
eightPitchBendRevert = pretty_midi.PitchBend(-451, 30)

cello.notes.append(one)
cello.notes.append(two)
cello.notes.append(three)
cello.notes.append(five)
cello.notes.append(six)
cello.notes.append(eight)
cello.pitch_bends.append(twoPitchBend)
cello.pitch_bends.append(twoPitchBendRevert)
cello.pitch_bends.append(threePitchBend)
cello.pitch_bends.append(threePitchBendRevert)
cello.pitch_bends.append(fivePitchBend)
cello.pitch_bends.append(fivePitchBendRevert)
cello.pitch_bends.append(sixPitchBend)
cello.pitch_bends.append(sixPitchBendRevert)
cello.pitch_bends.append(eightPitchBend)
cello.pitch_bends.append(eightPitchBendRevert)

#time = 0

#for each in range(0, 8191):
#    cello.pitch_bends.append(pretty_midi.PitchBend(each, time))
#    time = time + .03

# We'll just do a 1-semitone pitch ramp up
#n_steps = 512
#bend_range = 8192#2
#for time, pitch in zip(np.linspace(1.5, 2.3, n_steps), range(0, bend_range, bend_range)): #//n_steps
#    cello.pitch_bends.append(pretty_midi.PitchBend(pitch, time))

#attempting to create a single ascending scale in Slendro tuning

pm.instruments.append(cello)
pm.write('output.mid')