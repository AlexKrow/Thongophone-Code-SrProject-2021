import pygame
from pygame import midi

import serial

# Show MIDI devices
def print_devices():
    for n in range(pygame.midi.get_count()):
        print(n, pygame.midi.get_device_info(n))

# Get input from MIDI device and define MIDI messages
def readInput(input_device):
    while True:
        # If MIDI input
        if input_device.poll():
            event = input_device.read(1)[0]
            data = event[0]
            note_number = data[1]
            note_status = data[0]


            # Note On
            if (note_status) == 144:
            # Our octave 2 starts at note 45 instead of 33. So it is technically starting at octave 3, if we look at a
            # note number chart. So we check for octave 2, 1, 0, -1, in addtion to 3 for the sake of rounding.
            # ------- Octave 2 --------
                # Note A
                if (note_number) == 33 or (note_number) == 45 or (note_number) == 9 or (note_number) == 21:
                    # send A to serial port 2
                    ser2.write(b'A')
                # Note A#
                elif (note_number) == 34 or (note_number) == 46 or (note_number) == 10 or (note_number) == 22:
                    # send H to serial port 2
                    ser2.write(b'H')
                # Note B
                elif (note_number) == 35 or (note_number) == 47 or (note_number) == 11 or (note_number) == 23:
                    # send B to serial port 2
                    ser2.write(b'B')
                # Note C
                elif (note_number) == 36 or (note_number) == 48 or (note_number) == 0 or (note_number) == 12 or (note_number) == 24:
                    # send C to serial port 2
                    ser2.write(b'C')
                # Note C#
                elif (note_number) == 37 or (note_number) == 49 or (note_number) == 1 or (note_number) == 13 or (note_number) == 25:
                    # send I to serial port 2
                    ser2.write(b'I')
                # Note D
                elif (note_number) == 38 or (note_number) == 50 or (note_number) == 2 or (note_number) == 14 or (note_number) == 26:
                    # send D to serial port 2
                    ser2.write(b'D')
                # Note D#
                elif (note_number) == 39 or (note_number) == 51 or (note_number) == 3 or (note_number) == 15 or (note_number) == 27:
                    # send J to serial port 2
                    ser2.write(b'J')
                # Note E
                elif (note_number) == 40 or (note_number) == 52 or (note_number) == 4 or (note_number) == 16 or (note_number) == 28:
                    # send E to serial port 2
                    ser2.write(b'E')
                # Note F
                elif (note_number) == 41 or (note_number) == 53 or (note_number) == 5 or (note_number) == 17 or (note_number) == 29:
                    # send F to serial port 2
                    ser2.write(b'F')
                # Note F#
                elif (note_number) == 42 or (note_number) == 54 or (note_number) == 6 or (note_number) == 18 or (note_number) == 30:
                    # send K to serial port 2
                    ser2.write(b'K')
                # Note G
                elif (note_number) == 43 or (note_number) == 55 or (note_number) == 7 or (note_number) == 19 or (note_number) == 31:
                    # send G to serial port 2
                    ser2.write(b'G')
                # Note G#
                elif (note_number) == 44 or (note_number) == 56 or (note_number) == 8 or (note_number) == 20 or (note_number) == 32:
                    # send L to serial port 2
                    ser2.write(b'L')
            # Our octave 3 starts at 57 which is technically octave 4
            # ------- Octave 3 --------
                # Note A
                elif (note_number) == 57:
                    # send A to serial port 3
                    ser3.write(b'A')
                # Note A#
                elif (note_number) == 58:
                    # send H to serial port 3
                    ser3.write(b'H')
                # Note B
                elif (note_number) == 59:
                    # send B to serial port 3
                    ser3.write(b'B')
                # Note C
                elif (note_number) == 60:
                    # send C to serial port 3
                    ser3.write(b'C')
                # Note C#
                elif (note_number) == 61:
                    # send I to serial port 3
                    ser3.write(b'I')
                # Note D
                elif (note_number) == 62:
                    # send D to serial port 3
                    ser3.write(b'D')
                # Note D#
                elif (note_number) == 63:
                    # send J to serial port 3
                    ser3.write(b'J')
                # Note E
                elif (note_number) == 64:
                    # send E to serial port 3
                    ser3.write(b'E')
                # Note F
                elif (note_number) == 65:
                    # send F to serial port 3
                    ser3.write(b'F')
                # Note F#
                elif (note_number) == 66:
                    # send K to serial port 3
                    ser3.write(b'K')
                # Note G
                elif (note_number) == 67:
                    # send G to serial port 3
                    ser3.write(b'G')
                # Note G#
                elif (note_number) == 68:
                    # send L to serial port 3
                    ser3.write(b'L')

            # Our octave 4 starts at 69 so technically octave 5. We are checking for octave 6, 7, 8, 9, in addition to 5 for the sake
            # of rounding.
            # ------- Octave 4 --------
                #Note A
                elif (note_number) == 69 or (note_number) == 105 or (note_number) == 117 or (note_number) == 81 or (note_number) == 93:
                    # send A to serial port 4
                    ser4.write(b'A')
                # Note A#
                elif (note_number) == 70 or (note_number) == 106 or (note_number) == 118 or (note_number) == 82 or (note_number) == 94:
                    # send H to serial port 4
                    ser4.write(b'H')
                # Note B
                elif (note_number) == 71 or (note_number) == 107 or (note_number) == 119 or (note_number) == 83 or (note_number) == 95:
                    # send B to serial port 4
                    ser4.write(b'B')
                # Note C
                elif (note_number) == 72 or (note_number) == 108 or (note_number) == 84 or (note_number) == 96:
                    # send C to serial port 4
                    ser4.write(b'C')
                # Note C#
                elif (note_number) == 73 or (note_number) == 109 or (note_number) == 121 or (note_number) == 85 or (note_number) == 97:
                    # send I to serial port 4
                    ser4.write(b'I')
                # Note D
                elif (note_number) == 74 or (note_number) == 110 or (note_number) == 122 or (note_number) == 86 or (note_number) == 98:
                    # send D to serial port 4
                    ser4.write(b'D')
                # Note D#
                elif (note_number) == 75 or (note_number) == 111 or (note_number) == 123 or (note_number) == 87 or (note_number) == 99:
                    # send J to serial port 4
                    ser4.write(b'J')
                # Note E
                elif (note_number) == 76 or (note_number) == 112 or (note_number) == 124 or (note_number) == 88 or (note_number) == 100:
                    # send E to serial port 4
                    ser4.write(b'E')
                # Note F
                elif (note_number) == 77 or (note_number) == 113 or (note_number) == 125 or (note_number) == 89 or (note_number) == 101:
                    # send F to serial port 4
                    ser4.write(b'F')
                # Note F#
                elif (note_number) == 78 or (note_number) == 114 or (note_number) == 126 or (note_number) == 90 or (note_number) == 102:
                    # send K to serial port 4
                    ser4.write(b'K')
                # Note G
                elif (note_number) == 79 or (note_number) == 115 or (note_number) == 127 or (note_number) == 91 or (note_number) == 103:
                    # send G to serial port 4
                    ser4.write(b'G')
                # Note G#
                elif (note_number) == 80 or (note_number) == 116 or (note_number) == 92 or (note_number) == 104:
                    # send L to serial port 4
                    ser4.write(b'L')

            # Note Off
            if (note_status) == 128:
                # Our octave 2 starts at note 45 instead of 33. So it is technically starting at octave 3, if we look at a
                # note number chart. So we check for octave 2, 1, 0, -1, in addtion to 3 for the sake of rounding.
                # ------- Octave 2 --------
                #Note A
                if (note_number) == 33 or (note_number) == 45 or (note_number) == 9 or (note_number) == 21:
                    # send a to serial port 2
                    ser2.write(b'a')
                # Note A#
                elif (note_number) == 34 or (note_number) == 46 or (note_number) == 10 or (note_number) == 22:
                    # send h to serial port 2
                    ser2.write(b'h')
                # Note B
                elif (note_number) == 35 or (note_number) == 47 or (note_number) == 11 or (note_number) == 23:
                    # send b to serial port 2
                    ser2.write(b'b')
                # Note C
                elif (note_number) == 36 or (note_number) == 48 or (note_number) == 0 or (note_number) == 12 or (note_number) == 24:
                    # send c to serial port 2
                    ser2.write(b'c')
                # Note C#
                elif (note_number) == 37 or (note_number) == 49 or (note_number) == 1 or (note_number) == 13 or (note_number) == 25:
                    # send i to serial port 2
                    ser2.write(b'i')
                # Note D
                elif (note_number) == 38 or (note_number) == 50 or (note_number) == 2 or (note_number) == 14 or (note_number) == 26:
                    # send d to serial port 2
                    ser2.write(b'd')
                # Note D#
                elif (note_number) == 39 or (note_number) == 51 or (note_number) == 3 or (note_number) == 15 or (note_number) == 27:
                    # send j to serial port 2
                    ser2.write(b'j')
                # Note E
                elif (note_number) == 40 or (note_number) == 52 or (note_number) == 4 or (note_number) == 16 or (note_number) == 28:
                    # send e to serial port 2
                    ser2.write(b'e')
                # Note F
                elif (note_number) == 41 or (note_number) == 53 or (note_number) == 5 or (note_number) == 17 or (note_number) == 29:
                    # send f to serial port 2
                    ser2.write(b'f')
                # Note F#
                elif (note_number) == 42 or (note_number) == 54 or (note_number) == 6 or (note_number) == 18 or (note_number) == 30:
                    # send k to serial port 2
                    ser2.write(b'k')
                # Note G
                elif (note_number) == 43 or (note_number) == 55 or (note_number) == 7 or (note_number) == 19 or (note_number) == 31:
                    # send g to serial port 2
                    ser2.write(b'g')
                # Note G#
                elif (note_number) == 44 or (note_number) == 56 or (note_number) == 8 or (note_number) == 20 or (note_number) == 32:
                    # send l to serial port 2
                    ser2.write(b'l')
                # Our octave 3 starts at 57 which is technically octave 4
                # ------- Octave 3 --------
                # Note A
                elif (note_number) == 57:
                    # send a to serial port 3
                    ser3.write(b'a')
                # Note A#
                elif (note_number) == 58:
                    # send h to serial port 3
                    ser3.write(b'h')
                # Note B
                elif (note_number) == 59:
                    # send b to serial port 3
                    ser3.write(b'b')
                # Note C
                elif (note_number) == 60:
                    # send c to serial port 3
                    ser3.write(b'c')
                # Note C#
                elif (note_number) == 61:
                    # send i to serial port 3
                    ser3.write(b'i')
                # Note D
                elif (note_number) == 62:
                    # send d to serial port 3
                    ser3.write(b'd')
                # Note D#
                elif (note_number) == 63:
                    # send j to serial port 3
                    ser3.write(b'j')
                # Note E
                elif (note_number) == 64:
                    # send e to serial port 3
                    ser3.write(b'e')
                # Note F
                elif (note_number) == 65:
                    # send f to serial port 3
                    ser3.write(b'f')
                # Note F#
                elif (note_number) == 66:
                    # send k to serial port 3
                    ser3.write(b'k')
                # Note G
                elif (note_number) == 67:
                    # send g to serial port 3
                    ser3.write(b'g')
                # Note G#
                elif (note_number) == 68:
                    # send l to serial port 3
                    ser3.write(b'l')
                # Our octave 4 starts at 69 so technically octave 5. We are checking for octave 6, 7, 8, 9, in addition to 5 for the sake
                # of rounding.
                # ------- Octave 4 --------
                # Note A
                elif (note_number) == 69 or (note_number) == 105 or (note_number) == 117 or (note_number) == 81 or (note_number) == 93:
                    # send a to serial port 4
                    ser4.write(b'a')
                # Note A#
                elif (note_number) == 70 or (note_number) == 106 or (note_number) == 118 or (note_number) == 82 or (note_number) == 94:
                    # send h to serial port 4
                    ser4.write(b'h')
                # Note B
                elif (note_number) == 71 or (note_number) == 107 or (note_number) == 119 or (note_number) == 83 or (note_number) == 95:
                    # send b to serial port 4
                    ser4.write(b'b')
                # Note C
                elif (note_number) == 72 or (note_number) == 108 or (note_number) == 84 or (note_number) == 96:
                    # send c to serial port 4
                    ser4.write(b'c')
                # Note C#
                elif (note_number) == 73 or (note_number) == 109 or (note_number) == 121 or (note_number) == 85 or (note_number) == 97:
                    # send i to serial port 4
                    ser4.write(b'i')
                # Note D
                elif (note_number) == 74 or (note_number) == 110 or (note_number) == 122 or (note_number) == 86 or (note_number) == 98:
                    # send d to serial port 4
                    ser4.write(b'd')
                # Note D#
                elif (note_number) == 75 or (note_number) == 111 or (note_number) == 123 or (note_number) == 87 or (note_number) == 99:
                    # send j to serial port 4
                    ser4.write(b'j')
                # Note E
                elif (note_number) == 76 or (note_number) == 112 or (note_number) == 124 or (note_number) == 88 or (note_number) == 100:
                    # send e to serial port 4
                    ser4.write(b'e')
                # Note F
                elif (note_number) == 77 or (note_number) == 113 or (note_number) == 125 or (note_number) == 89 or (note_number) == 101:
                    # send f to serial port 4
                    ser4.write(b'f')
                # Note F#
                elif (note_number) == 78 or (note_number) == 114 or (note_number) == 126 or (note_number) == 90 or (note_number) == 102:
                    # send k to serial port 4
                    ser4.write(b'k')
                # Note G
                elif (note_number) == 79 or (note_number) == 115 or (note_number) == 127 or (note_number) == 91 or (note_number) == 103:
                    # send g to serial port 4
                    ser4.write(b'g')
                # Note G#
                elif (note_number) == 80 or (note_number) == 116 or (note_number) == 92 or (note_number) == 104:
                    # send l to serial port 4
                    ser4.write(b'l')


if __name__ == '__main__':
    pygame.midi.init()
    print_devices()
    # Recieve data from specified ports and flush buffer
    ser2 = serial.Serial('/dev/ttyUSB2', 9600, timeout=1)
    ser2.flush()
    ser3 = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser3.flush()
    ser4 = serial.Serial('/dev/ttyUSB', 9600, timeout=1)
    ser4.flush()
    #Device ID
    my_input = pygame.midi.Input(3)
    #Read data from device
    readInput(my_input)