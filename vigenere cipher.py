#!/usr/bin/env python3

import string

alphabet = string.ascii_lowercase


def get_keyword_index(keyword):
    keyword_index = []
    for character in keyword:
        if character in alphabet:
            keyword_index.append(alphabet.index(character))
    return keyword_index


def vigenere(message, keyword_index, direction):
    shift_value_index = 0
    result = ""

    for character in message:
        if character in alphabet:
            character_value = alphabet.index(character)
            current_shift_value = keyword_index[shift_value_index]
            new_value = (character_value + direction * current_shift_value) % 26
            result += alphabet[new_value]
            shift_value_index = (shift_value_index + 1) % len(keyword_index)
        else:
            result += character

    return result


def main():
    mode = ""
    while mode not in ("en", "de"):
        mode = input("Encrypt (en) or decrypt (de)?\t").lower().strip()

    message = input("Secret message\t").lower()
    keyword = input("Keyword?\t").lower()

    keyword_index = get_keyword_index(keyword)

    if not keyword_index:
        print("keyword invalid try again")
        return

    direction = 1 if mode == "en" else -1
    output = vigenere(message, keyword_index, direction)

    if mode == "en":
        print("Encrypted text:\t" + output)
    else:
        print("Decrypted text:\t" + output)


if __name__ == "__main__":
    main()
