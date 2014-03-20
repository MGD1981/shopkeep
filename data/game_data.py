import entities
import reference_data as ref

def tick():
	"""Smallest game time amount passes."""
	
	#TODO: Capture mouse/keyboard actions
	#TODO: Display screen
	
	for site in entities.sites['object list']:
		site.tick()
		