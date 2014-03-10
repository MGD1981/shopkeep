from reference_data import letter_dct
from random import choice, randint

def create_name(name_type='human'):
    """Generates a random name based on rules."""

    if name_type == 'human':
        syllables = randint(1, 2)
    if name_type == 'monster':
        syllables = randint(1, 3)
    name_chars = []
    for x in xrange(syllables):
        start_with = choice(['consonant', 'vowel'])
        if start_with == 'vowel':
            name_chars += choice(letter_dct[name_type]['vowel start'])
            name_chars += choice(letter_dct[name_type]['consonant end'])
        if start_with == 'consonant':
            if randint(0, 1) == 0:
                name_chars += choice(letter_dct[name_type]['consonant start'])
                name_chars += choice(letter_dct[name_type]['vowel mid'])
            else:
                name_chars += choice(letter_dct[name_type]['consonant start'])
                name_chars += choice(letter_dct[name_type]['vowel mid'])
                name_chars += choice(letter_dct[name_type]['consonant end'])

    return ''.join(name_chars).capitalize()
