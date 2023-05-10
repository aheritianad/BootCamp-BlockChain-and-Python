from bcbcpy import __author__


from bcbcpy.math.arithmetic import digits, base2int

from typing import Tuple
import random
import json

__all__ = [
    "C2I",
    "I2C",
    "txt2int",
    "int2txt",
    "obj2txt",
    "txt2obj",
    "add_noises",
    "remove_noises",
    "TOTAL_CHAR",
]

TOTAL_CHAR = 97

C2I = {
    "\t": 0,
    "\n": 1,
    " ": 2,
    "!": 3,
    '"': 4,
    "#": 5,
    "$": 6,
    "%": 7,
    "&": 8,
    "'": 9,
    "(": 10,
    ")": 11,
    "*": 12,
    "+": 13,
    ",": 14,
    "-": 15,
    ".": 16,
    "/": 17,
    "0": 18,
    "1": 19,
    "2": 20,
    "3": 21,
    "4": 22,
    "5": 23,
    "6": 24,
    "7": 25,
    "8": 26,
    "9": 27,
    ":": 28,
    ";": 29,
    "<": 30,
    "=": 31,
    ">": 32,
    "?": 33,
    "@": 34,
    "A": 35,
    "B": 36,
    "C": 37,
    "D": 38,
    "E": 39,
    "F": 40,
    "G": 41,
    "H": 42,
    "I": 43,
    "J": 44,
    "K": 45,
    "L": 46,
    "M": 47,
    "N": 48,
    "O": 49,
    "P": 50,
    "Q": 51,
    "R": 52,
    "S": 53,
    "T": 54,
    "U": 55,
    "V": 56,
    "W": 57,
    "X": 58,
    "Y": 59,
    "Z": 60,
    "[": 61,
    "\\": 62,
    "]": 63,
    "^": 64,
    "_": 65,
    "`": 66,
    "a": 67,
    "b": 68,
    "c": 69,
    "d": 70,
    "e": 71,
    "f": 72,
    "g": 73,
    "h": 74,
    "i": 75,
    "j": 76,
    "k": 77,
    "l": 78,
    "m": 79,
    "n": 80,
    "o": 81,
    "p": 82,
    "q": 83,
    "r": 84,
    "s": 85,
    "t": 86,
    "u": 87,
    "v": 88,
    "w": 89,
    "x": 90,
    "y": 91,
    "z": 92,
    "{": 93,
    "|": 94,
    "}": 95,
    "~": 96,
}

I2C = {
    0: "\t",
    1: "\n",
    2: " ",
    3: "!",
    4: '"',
    5: "#",
    6: "$",
    7: "%",
    8: "&",
    9: "'",
    10: "(",
    11: ")",
    12: "*",
    13: "+",
    14: ",",
    15: "-",
    16: ".",
    17: "/",
    18: "0",
    19: "1",
    20: "2",
    21: "3",
    22: "4",
    23: "5",
    24: "6",
    25: "7",
    26: "8",
    27: "9",
    28: ":",
    29: ";",
    30: "<",
    31: "=",
    32: ">",
    33: "?",
    34: "@",
    35: "A",
    36: "B",
    37: "C",
    38: "D",
    39: "E",
    40: "F",
    41: "G",
    42: "H",
    43: "I",
    44: "J",
    45: "K",
    46: "L",
    47: "M",
    48: "N",
    49: "O",
    50: "P",
    51: "Q",
    52: "R",
    53: "S",
    54: "T",
    55: "U",
    56: "V",
    57: "W",
    58: "X",
    59: "Y",
    60: "Z",
    61: "[",
    62: "\\",
    63: "]",
    64: "^",
    65: "_",
    66: "`",
    67: "a",
    68: "b",
    69: "c",
    70: "d",
    71: "e",
    72: "f",
    73: "g",
    74: "h",
    75: "i",
    76: "j",
    77: "k",
    78: "l",
    79: "m",
    80: "n",
    81: "o",
    82: "p",
    83: "q",
    84: "r",
    85: "s",
    86: "t",
    87: "u",
    88: "v",
    89: "w",
    90: "x",
    91: "y",
    92: "z",
    93: "{",
    94: "|",
    95: "}",
    96: "~",
}


def int2txt(num: int):
    b = TOTAL_CHAR
    txt = ""
    for d in digits(num, b):
        txt += I2C[d]
    return txt


def txt2int(text: str):
    b = TOTAL_CHAR
    digits_base = [C2I[ch] for ch in text]
    nb = base2int(digits_base, b)
    return nb


def obj2txt(obj: object, indent: int = 4, separators: Tuple[str, str] | None = None):
    return json.dumps(obj, indent=indent, separators=separators)


def txt2obj(text: str):
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        obj = text

    return obj


def add_noises(message: str):
    noisy_message = ""
    noises = list(C2I.keys())
    for c in message:
        noise = random.choice(noises)
        noisy_message += c + noise
    return noisy_message


def remove_noises(noisy_message: str):
    clean_message = noisy_message[::2]
    return clean_message
