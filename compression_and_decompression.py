# coding=utf-8

from enum import Enum

character_type_enum = Enum("CHARACTER_TYPE_ENUM", "number letter open_bracket close_bracket")

def decompress_string(input_string: str) -> str:
    """
    In this exercise, you're going to decompress a compressed string.

    Your input is a compressed string of the format number[string] and the decompressed output
    form should be the string written number times. For example:

    The input

    3[abc]4[ab]c

    Would be output as

    abcabcabcababababc

    Other rules
    Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

    One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

    Characters allowed as input include digits, small English letters and brackets [ ].

    Digits are only to represent amount of repetitions.

    Letters are just letters.

    Brackets are only part of syntax of writing repeated substring.

    Input is always valid, so no need to check its validity.

    Learning objectives This question gives you the chance to practice with strings, recursion,
    algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with
    better efficiency.


    :param input_string: the compressed string
    :return: the generated uncompressed string
    """

    output = ""
    current_number_string = ""
    decompression_depth = 0
    current_string_to_decompress = ""

    for current_character in input_string:

        current_character_type = identify_character(current_character)

        # Execute action depending on character type
        if current_character_type == character_type_enum.letter:
            if decompression_depth == 0:
                output += current_character
            else:
                current_string_to_decompress += current_character

        elif current_character_type == character_type_enum.number:
            current_number_string = current_character

        elif current_character_type == character_type_enum.open_bracket:
            decompression_depth += 1

        elif current_character_type == character_type_enum.close_bracket:
            for _ in range(int(current_number_string)):
                output += current_string_to_decompress
            current_string_to_decompress = ""
            decompression_depth -= 1

    return output


def identify_character(current_character: str) -> character_type_enum:
    """
    Checks whether the character is one of the four allowed types:
    [, ], number or letter

    :param current_character: the character to evaluate
    :return: the type of the character as an character_type_enum
    """
    if current_character == '[':
        current_character_type = character_type_enum.open_bracket
    elif current_character == ']':
        current_character_type = character_type_enum.close_bracket
    elif current_character.isdigit():
        current_character_type = character_type_enum.number
    else:
        current_character_type = character_type_enum.letter
    return current_character_type

