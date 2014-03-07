import letter_dct from reference.data
from random import choice, randint

def create_monster_name():
	"""Generates a random name based on rules."""
	
	name_chars = []
	start_with = choice(['consonant', 'vowel'])
	if start_with == 'vowel':
		name_chars += choice(letter_dct['m_vowel start'])
		name_chars += choice(letter_dct['m_consonant end'])
	if start_with == 'consonant':
		if randint(0, 1) == 0:
			name_chars += choice(letter_dct['m_consonant start'])
			name_chars += choice(letter_dct['m_vowel mid'])
		else:
			name_chars += choice(letter_dct['m_consonant start'])
			name_chars += choice(letter_dct['m_vowel mid'])
			name_chars += choice(letter_dct['m_consonant end'])
	name = ''.join(name_chars)
	return name.capitalize()
	
	
def create_human_name():
	"""Generates a name with more stringent rules."""
	
	name_chars = []
	start_with = choice(['consonant', 'vowel'])
	if start_with == 'vowel':
		name_chars += choice(letter_dct['h_vowel start'])
		name_chars += choice(letter_dct['h_consonant end'])
	if start_with == 'consonant':
		if randint(0, 1) == 0:
			name_chars += choice(letter_dct['h_consonant start'])
			name_chars += choice(letter_dct['h_vowel mid'])
		else:
			name_chars += choice(letter_dct['h_consonant start'])
			name_chars += choice(letter_dct['h_vowel mid'])
			name_chars += choice(letter_dct['h_consonant end'])
	name = ''.join(name_chars)
	return name.capitalize()
		