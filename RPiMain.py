import MidiFileDecoder
import MidiFileStreamer

from MidiFileDecoder import NoteArray
from MidiFileDecoder import NoteOnTimeArray
from MidiFileDecoder import NoteOffTimeArray
from MidiFileDecoder import NoteOnNumArray


# This is the main function for the MidiFileDecoder:
# It is an endless loop in which:
# Asks the user for a midi file (by filename)
# Plays the file
#   IF NOT FOUND, print an error message and continue
# After playing is done, loop again
# LOOP TERMINATES if the user types 'quit'

def RPiMain():
    MidiFileName = input("Enter Midi File Name: ")

    MidiFileDecoder.MidiFileDecoder(MidiFileName)

    print("Playing...")
    MidiFileStreamer.MidiStreamer(NoteArray, NoteOnTimeArray, NoteOffTimeArray, NoteOnNumArray)


# End main function

RPiMain()
