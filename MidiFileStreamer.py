from mido import MidiFile
import time
import serial
import MidiFileDecoder
from MidiFileDecoder import NoteArray
from MidiFileDecoder import NoteOnTimeArray
from MidiFileDecoder import NoteOffTimeArray
from MidiFileDecoder import NoteOnNumArray


# This function streams DECODED midi messages to the Octave Select function
# Imagine that this file simulates a real person sending MIDI feed to the system

# Loop:
# Use NoteOnNumArray and NoteOffNumArray to determine what octave (microcontroller) to send data to
# Read NoteOn/Off Time
# After given amount of sleep time (different per note), send character out to respective
#  microcontroller

def MidiStreamer(NoteArray, NoteOnTimeArray, NoteOffTimeArray, NoteOnNumArray):
    # counters:
    # NoteOnNumArray
    y = 0
    # NoteOnTimeArray
    w = 0
    # NoteOffTimeArray
    x = 0

    # for debugging
    Octave = 0

    for i in range(len(NoteArray)):
        # end of track
        if NoteArray[i] == 6969:
            print(":::Done playing:::")
            # uc32.close()
            break

        # Octave 2 (lowest octave)
        elif 45 <= NoteOnNumArray[y] < 57:
            Octave = 2
            # uc32 = serial.Serial('USB0', 9600, timeout=0.1)
            # if not uc32.isOpen():
            # uc32.open()
            # uc32.flush()

        # Octave 3 (middle octave)
        elif 57 <= NoteOnNumArray[y] < 69:
            Octave = 3
            # uc32 = serial.Serial('USB1', 9600, timeout=0.1)
            # if not uc32.isOpen():
            # uc32.open()
            # uc32.flush()

        # Octave 4 (highest octave)
        elif 45 <= NoteOnNumArray[y] < 57:
            Octave = 4
            # uc32 = serial.Serial('USB2', 9600, timeout=0.1)
            # if not uc32.isOpen():
            # uc32.open()
            # uc32.flush()

        if NoteArray[i].isupper():
            sleeptime = NoteOnTimeArray[w]
            w += 1
            time.sleep(sleeptime)
            print("Octave: ", Octave, "Note: ", NoteArray[i])
            # uc32.write(NoteArray[i].encode())
            continue

        elif NoteArray[i].islower():
            sleeptime = NoteOffTimeArray[x]
            x += 1
            y += 1
            time.sleep(sleeptime)
            print("Octave: ", Octave, "Note: ", NoteArray[i])
            # uc32.write(NoteArray[i].encode())


# End MidiFileStreamer

