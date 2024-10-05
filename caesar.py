def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    shift = 3
    # caesar_dict_gen = {chr(i): i for i  in range(ord('a'),ord('z'))}
    caesar_dict = {
        "a": 97,
        "b": 98,
        "c": 99,
        "d": 100,
        "e": 101,
        "f": 102,
        "g": 103,
        "h": 104,
        "i": 105,
        "j": 106,
        "k": 107,
        "l": 108,
        "m": 109,
        "n": 110,
        "o": 111,
        "p": 112,
        "q": 113,
        "r": 114,
        "s": 115,
        "t": 116,
        "u": 117,
        "v": 118,
        "w": 119,
        "x": 97 - shift,
        "y": 98 - shift,
        "z": 99 - shift,
    }
    for ch in plaintext:
        if caesar_dict.get(ch.lower(), 0):
            if ch.isupper():
                ciphertext += chr(caesar_dict[ch.lower()] + shift).upper()
            else:
                ciphertext += chr(caesar_dict[ch] + shift)
        else:
            ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    plaintext = ""
    shift = 3
    # caesar_dict_gen = {i+shift: chr(i) for i  in range(97,123)}
    caesar_dict = {
        100: "a",
        101: "b",
        102: "c",
        103: "d",
        104: "e",
        105: "f",
        106: "g",
        107: "h",
        108: "i",
        109: "j",
        110: "k",
        111: "l",
        112: "m",
        113: "n",
        114: "o",
        115: "p",
        116: "q",
        117: "r",
        118: "s",
        119: "t",
        120: "u",
        121: "v",
        122: "w",
        97: "x",
        98: "y",
        99: "z",
    }
    for ch in ciphertext:
        if caesar_dict.get(ord(ch.lower()), 0):
            if ch.isupper():
                plaintext += caesar_dict[ord(ch.lower())].upper()
            else:
                plaintext += caesar_dict[ord(ch)]
        else:
            plaintext += ch
    return plaintext
