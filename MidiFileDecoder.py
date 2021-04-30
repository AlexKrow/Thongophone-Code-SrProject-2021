import mido
from mido import MidiFile
from ThongNote import ThongNote

# MidiFileDecoder.py:
# This function decodes midi messages into useful data for MidiFileStreamer.py
# Outputs:
# Array of NoteOn/Off Numbers (used by streamer)
# Array of Note On/Off times (used by the streamer)
# Array of characters to be sent to the microcontrollers

# char. array to be sent to microcontrollers
NoteArray = []

# used for timing and routing data in MidiFileStreamer
DTimeArray = []

# Intermidiary arrays, used only in this file
NoteOnNumArray = []
NoteOffNumArray = []
NoteOnTimeArray = []
NoteOffTimeArray = []


def MidiFileDecoder(MidiFileName):
    global tempo
    mid = MidiFile(MidiFileName, clip=True)

    # tempo is needed for converting bpm (beats per minute) into seconds
    for msg in mid.tracks[0]:
        if msg.type == 'set_tempo':
            tempo = msg.tempo

    # Determining note numbers and characters to send when note-on
    for msg in mid.tracks[1]:
        if msg.type == 'note_on':
            NoteNum = msg.note

            # round notes into Thongophone range
            while True:
                if 45 <= NoteNum <= 80:
                    break
                elif NoteNum < 45:
                    NoteNum = NoteNum + 12
                    continue
                elif NoteNum > 80:
                    NoteNum = NoteNum - 12
                    continue

            # this array is used to determine which USB port to output to
            NoteOnNumArray.append(NoteNum)

            # using ThongNote class to connect a note number to a character
            # to send to the microcontroller
            TNInstance = ThongNote()
            NoteOn = TNInstance.NumtoNoteOn(NoteNum)
            NoteArray.append(NoteOn)

            # add note on time to NoteOnTimeArray to use for timing
            NoteOnTime = msg.time
            NoteOnTime = mido.tick2second(NoteOnTime, mid.ticks_per_beat, tempo)
            NoteOnTime = float(NoteOnTime)
            NoteOnTimeArray.append(NoteOnTime)

        # note-off events, same idea as note-on events
        elif msg.type == 'note_off':
            NoteNum = msg.note

            # rounding into range
            while True:
                if 45 <= NoteNum <= 80:
                    break
                elif NoteNum < 45:
                    NoteNum = NoteNum + 12
                    continue
                elif NoteNum > 80:
                    NoteNum = NoteNum - 12
                    continue

            NoteOffNumArray.append(NoteNum)

            TNInstance2 = ThongNote()
            NoteOff = TNInstance2.NumtoNoteOff(NoteNum)
            NoteArray.append(NoteOff)

            # Add note off time like note on
            NoteOffTime = msg.time
            NoteOffTime = mido.tick2second(NoteOffTime, mid.ticks_per_beat, tempo)
            NoteOffTime = float(NoteOffTime)
            NoteOffTimeArray.append(NoteOffTime)

        else:
            continue

    # random values for the end of track
    NoteArray.append(6969)
    DTimeArray.append(0)


# End MidiFileDecoder

