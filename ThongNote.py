# ThongNote.py:
# This class takes in midi note numbers and based on that number, returns a single character to MidiFileDecoder.py to be sent to the Microcontrollers.

class ThongNote:
    # empty char for ThongNote.note
    note = ''

    def NumtoNoteOn(self, NoteNum):
        # Im using a case/switch statement to map a NoteNum
        # to a char.  This char will be sent to the MC
        # switcher is faster than a bunch of if/else statements

        switcher = {
            # C:
            0: 'C',
            12: 'C',
            24: 'C',
            36: 'C',
            48: 'C',
            60: 'C',
            72: 'C',
            84: 'C',
            96: 'C',
            108: 'C',

            # C#:
            1: 'I',
            13: 'I',
            25: 'I',
            37: 'I',
            49: 'I',
            61: 'I',
            73: 'I',
            85: 'I',
            97: 'I',

            # D:
            2: 'D',
            14: 'D',
            26: 'D',
            38: 'D',
            50: 'D',
            62: 'D',
            74: 'D',
            86: 'D',
            98: 'D',

            # D#:
            3: 'J',
            15: 'J',
            27: 'J',
            39: 'J',
            51: 'J',
            63: 'J',
            75: 'J',
            87: 'J',
            99: 'J',

            # E:
            4: 'E',
            16: 'E',
            28: 'E',
            40: 'E',
            52: 'E',
            64: 'E',
            76: 'E',
            88: 'E',
            100: 'E',

            # F:
            5: 'F',
            17: 'F',
            29: 'F',
            41: 'F',
            53: 'F',
            65: 'F',
            77: 'F',
            89: 'F',
            101: 'F',

            # F#:
            6: 'K',
            18: 'K',
            30: 'K',
            42: 'K',
            54: 'K',
            66: 'K',
            78: 'K',
            90: 'K',
            102: 'K',

            # G:
            7: 'G',
            19: 'G',
            31: 'G',
            43: 'G',
            55: 'G',
            67: 'G',
            79: 'G',
            91: 'G',
            103: 'G',

            # G#:
            8: 'L',
            20: 'L',
            32: 'L',
            44: 'L',
            56: 'L',
            68: 'L',
            80: 'L',
            92: 'L',
            104: 'L',

            # A:
            9: 'A',
            21: 'A',
            33: 'A',
            45: 'A',
            57: 'A',
            69: 'A',
            81: 'A',
            93: 'A',
            105: 'A',

            # A#:
            10: 'H',
            22: 'H',
            34: 'H',
            46: 'H',
            58: 'H',
            70: 'H',
            82: 'H',
            94: 'H',
            106: 'H',

            # B:
            11: 'B',
            23: 'B',
            35: 'B',
            47: 'B',
            59: 'B',
            71: 'B',
            83: 'B',
            95: 'B',
            107: 'B',
        }
        # Z = no notes were picked from switcher statement
        noteOn = switcher.get(NoteNum, 'Z')
        return noteOn

    # same idea as NumtoNoteOn(above), but sending different chars
    def NumtoNoteOff(self, NoteNum):
        switcher = {
            # C:
            0: 'c',
            12: 'c',
            24: 'c',
            36: 'c',
            48: 'c',
            60: 'c',
            72: 'c',
            84: 'c',
            96: 'c',
            108: 'c',

            # C#:
            1: 'i',
            13: 'i',
            25: 'i',
            37: 'i',
            49: 'i',
            61: 'i',
            73: 'i',
            85: 'i',
            97: 'i',

            # D:
            2: 'd',
            14: 'd',
            26: 'd',
            38: 'd',
            50: 'd',
            62: 'd',
            74: 'd',
            86: 'd',
            98: 'd',

            # D#:
            3: 'j',
            15: 'j',
            27: 'j',
            39: 'j',
            51: 'j',
            63: 'j',
            75: 'j',
            87: 'j',
            99: 'j',

            # E:
            4: 'e',
            16: 'e',
            28: 'e',
            40: 'e',
            52: 'e',
            64: 'e',
            76: 'e',
            88: 'e',
            100: 'e',

            # F:
            5: 'f',
            17: 'f',
            29: 'f',
            41: 'f',
            53: 'f',
            65: 'f',
            77: 'f',
            89: 'f',
            101: 'f',

            # F#:
            6: 'k',
            18: 'k',
            30: 'k',
            42: 'k',
            54: 'k',
            66: 'k',
            78: 'k',
            90: 'k',
            102: 'k',

            # G:
            7: 'g',
            19: 'g',
            31: 'g',
            43: 'g',
            55: 'g',
            67: 'g',
            79: 'g',
            91: 'g',
            103: 'g',

            # G#:
            8: 'l',
            20: 'l',
            32: 'l',
            44: 'l',
            56: 'l',
            68: 'l',
            80: 'l',
            92: 'l',
            104: 'l',

            # A:
            9: 'a',
            21: 'a',
            33: 'a',
            45: 'a',
            57: 'a',
            69: 'a',
            81: 'a',
            93: 'a',
            105: 'a',

            # A#:
            10: 'h',
            22: 'h',
            34: 'h',
            46: 'h',
            58: 'h',
            70: 'h',
            82: 'h',
            94: 'h',
            106: 'h',

            # B:
            11: 'b',
            23: 'b',
            35: 'b',
            47: 'b',
            59: 'b',
            71: 'b',
            83: 'b',
            95: 'b',
            107: 'b',
        }
        # Z = no notes were picked from switcher statement
        noteOff = switcher.get(NoteNum, 'z')
        return noteOff
