#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Morse code decoder

https://www.codewars.com/kata/decode-the-morse-code/python
https://www.codewars.com/kata/decode-the-morse-code-advanced/python


When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is.
And in fact different
operators would transmit at different speed. An amateur person may need a few seconds to
transmit a single character, a skilled professional can transmit 60 words per minute,
and robotic transmitters may go way faster.

OK FOR REAL??  60 WPM??
https://morsecode.scphillips.com/translator.html

For this kata we assume the message receiving is performed automatically by the hardware
that checks the line periodically, and if the line is connected (the key at the remote
station is down), 1 is recorded, and if the line is not connected (remote key is up),
0 is recorded. After the message is fully received, it gets to you for decoding as a
string containing only symbols 0 and 1.
"""

from itertools import groupby
# This dictionary is supplied within the Codewars test suite.
MORSE_CODE = {
    '.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B',
    '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
    '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K',
    '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M',
    '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
    '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q',
    '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T',
    '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"',
    '-.--.': '(', '---..': '8', '...--': '3'
}


def find_mult(bits):
    """Finds least amount of occurrences of 0 or 1"""
    mult = len(bits)
    for group in groupby(bits, lambda b: int(b) % 2):
        mult = min(mult, len(list(group[1])))

    return mult

def decodeBits(bits):
    """Translate a string of 1's & 0's to dots and dashes"""
    bits = bits.strip('0')
    time_unit = find_mult(bits)
    translation_string = ""
    for key, group in groupby(bits, lambda b: int(b) % 2):
        if key == 1:
            group_len = len(list(group)) / time_unit
            translation_string += "." if group_len == 1 else "-"
        else:
            group_len = len(list(group)) / time_unit
            if group_len == 7:
                translation_string += "  "
            elif group_len == 3:
                translation_string += " "
    
    return translation_string
        


def decodeMorse(morse_code):
    morse = morse_code.strip().split(" ")
    translation = [MORSE_CODE[i] if i in MORSE_CODE else " " for i in morse]
    return " ".join("".join(translation).split())
