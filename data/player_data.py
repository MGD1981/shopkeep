import random
import entities

def get_new_player():
	player = {
        'location': [0, 0],
        'coins': 0,
        'appraisal skill': {
            'wood': 0,
            'fiber': 0,
            'stone': 0,
            'leather': 0,
            'metal': 0
        }
    }

	return player
