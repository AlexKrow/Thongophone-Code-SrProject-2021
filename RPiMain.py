import MidiFileDecoder
import MidiFileStreamer

from MidiFileDecoder import NoteArray
from MidiFileDecoder import NoteOnTimeArray
from MidiFileDecoder import NoteOffTimeArray
from MidiFileDecoder import NoteOnNumArray


# This is the main function for the MidiFileDecoder:
# Asks the user for a midifile name to be played, then takes that string and sends it to MidiFileDecoder.py to be decoded.  
# Next, the arrays from MidiFileDecoder.py are sent to MidiFileStreamer.py to be streamed to the proper Microcontrollers.
# After song is done playing, program terminates.  
# Note: RPiMain.py is incorporated into ThongGUI.py

#Author: Alexander Croll

def RPiMain():
    MidiFileName = input("Enter Midi File Name: ")

    MidiFileDecoder.MidiFileDecoder(MidiFileName)

    print("Playing...")
    MidiFileStreamer.MidiStreamer(NoteArray, NoteOnTimeArray, NoteOffTimeArray, NoteOnNumArray)


# End main function

RPiMain()
