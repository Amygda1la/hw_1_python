def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    new_keyword = keyword
    if len(plaintext) > len(keyword):
        shift_key = 0
        while len(plaintext) != len(new_keyword):
            new_keyword += new_keyword[shift_key]
            shift_key += 1
    for i in range(0, len(plaintext)):
        start = 65 if plaintext[i].isupper() else 97
        if plaintext[i].isalpha():
            shift = ord(new_keyword[i].lower()) - 97
            ciphertext += chr((ord(plaintext[i]) - start + shift) % 26 + start)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    new_keyword = keyword
    if len(ciphertext) > len(keyword):
        shift_key = 0
        while len(ciphertext) != len(new_keyword):
            new_keyword += new_keyword[shift_key]
            shift_key += 1
    for i in range(0, len(ciphertext)):
        start = 65 if ciphertext[i].isupper() else 97
        if ciphertext[i].isalpha():
            shift = ord(new_keyword[i].lower()) - 97
            plaintext += chr((ord(ciphertext[i]) - start - shift) % 26 + start)
        else:
            plaintext += ciphertext[i]
    return plaintext
