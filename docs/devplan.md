Shopkeep Development Plan
=========================

#Main Ideas

- Player owns and operates a shop in a town in a medieval fantasy setting a la D&D.
- Shop will procure/create weapons and armor -- possibly expanding to other things in the future.
- Heroes and would-be heroes will make transactions at shop.
- Off-screen, heroes will adventure at various locations which may or may not contain treasure.  Death of a hero will add his/her inventory to that location's treasure.
- Keeping the number of transactions small will keep it manageable and keep the player interested in them.  Expanding to a megastore style will be boring without a fun management system.  Imagine throngs of villagers coming in selling their everyday garden herbs in the shop's apothecary section.
- Items will have detailed descriptions and histories of ownership, kills (or in the case of armor, notable saves-from-death), etc.
- Stats (i.e. strength, dex, etc.) do not change.  There are no experience levels.  But heroes may develop familiarity with both a specific item and also with a generic item type.
- Will start coding just weapons, leaving a framework for expansion.
- Tile-based sprites.  Will have a designer create these; will start with CP437 on my own.

#Potential Future (post v1)

- Physical shop with limited capacity, ability to expand space, storage, functionality (i.e. purchasing a forge)
- Potential for shoplifting, robberies, need to hire guards
- Create CP437 sprite system (OpenGL, like Dwarf Fortress?)


#To Do

- Create console-based dev menu for shop actions to act as starting point (make sure will be able to translate into a graphical system)
- Determine turn-based or time-based system (mixed?)
- Flesh out concept of adventure locations
- Flesh out concept of new hero generation
- Create list of weapon types
- Create list of weapon classes


#Hero Traits

- Constants
	- Name
	- Date of Birth
	- Sex
	- Race
	- Class
	- Size
	- Personality (may not include in v1)

- Variables
	- Weapon Class Familiarity (value for each class)
	- Weapon Type Familiarity (value for each type)
	- Specific Weapon Familiarity (value for each weapon ever wielded)
	


#Item Types

##Weapons

###Materials (items may be made of more than one)

- Leather (e.g. whip, sling)
- Gut (e.g. bow)
- Wood (e.g. spear, club)
- Stone (e.g. tomahawk, sling bullet)
- Copper
- Bronze
- Silver
- Gold
- Iron
- Steel
- Mithril
- Adamantium


###Basic Qualities

- Unique ID Hash
- Class (e.g. 1-handed slashing, 2-handed bludgeon, etc.)
- Type (e.g. falchion, warhammer, etc.)
- Weight
- Sharpness (possible null)
- Grip
- Durability (upon breaking, splits into component materials)
- Balance

