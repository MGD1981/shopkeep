import letter_dct from reference.data
from random import choice, randint

def create_human_name():
	"""Generates a random name based on rules."""
	
	name_chars = []
	syllables = randint(1, 3)
	for syllable in xrange(syllables):
		start_with = choice(['consonant', 'vowel'])
		if start_with == 'vowel':
			name_chars += choice(letter_dct['vowel start'])
			name_chars += choice(letter_dct['consonant end'])
		if start_with == 'consonant':
			if randint(0, 1) == 0:
				name_chars += choice(letter_dct['consonant start'])
				name_chars += choice(letter_dct['vowel mid'])
			else:
				name_chars += choice(letter_dct['consonant start'])
				name_chars += choice(letter_dct['vowel mid'])
				name_chars += choice(letter_dct['consonant end'])
		
	
	name = ''.join(name_chars)
	return name.capitalize()