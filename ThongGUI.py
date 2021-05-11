import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import MidiFileDecoder
import MidiFileStreamer
from MidiFileDecoder import NoteArray
from MidiFileDecoder import NoteOnTimeArray
from MidiFileDecoder import NoteOffTimeArray
from MidiFileDecoder import NoteOnNumArray
from MidiFileDecoder import NoteOffNumArray

# Use tkinter
root = tk.Tk()

# Set window title
root.title('Thongophone')

# Set window size
root.geometry("500x300")

def chooseFile(event=None):
    # Create global variable
    global midiFile
    # Show files with .mid extension
    filename = filedialog.askopenfilename(filetypes =[('MIDI Files', '.mid')])
    # Set label to the choosen file
    songLabel = Label(root,
                      text=os.path.basename(os.path.realpath(filename)),
                      fg="black",
                      font=("Helvetica", 10))
    # Place label
    songLabel.place(relx=0.35, rely=0.105, anchor='nw')
    # Set variable to the midi file name
    midiFile = songLabel.cget("text")

# Create a button that uses the UplaodAction function
chooseButton = tk.Button(root, text='Choose File...', command=chooseFile)
chooseButton.place(relx=0.17, rely=0.1, anchor='nw')

# Set flag to true
is_on = True

# Create live play label
liveLabel = Label(root,
                 text="Play Live:",
                 fg="black",
                 font=("Helvetica", 12))

# Place label
liveLabel.place(relx=0.05, rely=0.5, anchor='nw')

# Create song label
startSongLabel = Label(root,
                 text="Play Song:",
                 fg="black",
                 font=("Helvetica", 12))
# Place label
startSongLabel.place(relx=0.05, rely=0.3, anchor='nw')

# Create file label
fileLabel = Label(root,
                 text="Songs:",
                 fg="black",
                 font=("Helvetica", 12))

# Place label
fileLabel.place(relx=0.05, rely=0.1, anchor='nw')

def onOff():
    # Create global variable
    global is_on
    # Determine if button is on or off
    if is_on:
        # Set button text to On
        fileButton.config(text='On')
        root.update()
        # Call function to play selected file
        RPiMain()
        # set flag to false
        is_on = False
    else:
        # Set button text to Off
        fileButton.config(text='Off')
        return
        # set flag to true
        is_on = True

# Create file button
fileButton = tk.Button(root, text='Off', command=onOff)
# Place button
fileButton.place(relx=0.23, rely=0.3, anchor='nw')

def RPiMain():
    # Pass the selected midi file to the MIDI file decoder
    MidiFileDecoder.MidiFileDecoder(str(midiFile))
    # Stream the selected midi file
    MidiFileStreamer.MidiStreamer(NoteArray, NoteOnTimeArray, NoteOffTimeArray, NoteOnNumArray)

from subprocess import Popen

def startLive():
    # create global variable
    global live
    # open LiveMidiDecoder.py
    live = Popen(["python", "LiveMidiDecoder.py"])


def stopLive():
    # close LiveMidiDecoder.py
    live.terminate()

# Create start and stop buttons for live play and link them to
# the startLive and stopLive functions
startLiveButton = tk.Button(root, text="Play",command=startLive)
stopLiveButton = tk.Button(root, text="Stop",command=stopLive)

# Place buttons at location on the window
startLiveButton.place(relx=0.23, rely=0.5, anchor='nw')
stopLiveButton.place(relx=0.33, rely=0.5, anchor='nw')

root.mainloop()





