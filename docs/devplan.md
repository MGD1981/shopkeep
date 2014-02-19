Shopkeep Development Plan
=========================

#Main Ideas

- Player owns and operates a shop in a town in a medieval fantasy setting a la D&D.
- Shop will procure/create weapons and possibly armor -- possibly expanding to other things in the future.
- Heroes and would-be heroes will make transactions at shop.
- Off-screen, heroes will adventure at various locations which may or may not contain treasure.  Death of a hero will add his/her inventory to that location's treasure.
- Keeping the number of transactions small will keep it manageable and keep the player interested in them.  Expanding to a megastore style will be boring without a fun management system.  Imagine throngs of villagers coming in selling their everyday garden herbs in the shop's apothecary section.
- Items will have detailed descriptions and histories of ownership, kills (or in the case of armor, notable saves-from-death), etc.
- Stats (i.e. strength, dex, etc.) do not change.  There are no experience levels.  But heroes may develop familiarity with both a specific item and also with a generic item type.
- Will start coding just weapons, leaving a framework for expansion.
- Tile-based sprites.  Will have a designer create these; will start with CP437 on my own.
- Interactions with other shops in town (e.g. order wood from woodcutter); towns may not always have every kind of shop.
- Raw material shops have dynamic inventory dependent on world activity; may need resource sites along with adventure sites.
- Becoming self-sufficient may anger neglected shops, who could attempt to rob/damange player's shop; player could hire guards.
- Humorous hate-thy-neighbor relationship with neighboring apothecary.
- Ability to auto-transact by setting buy/sell rules; easy method to view/query rules.
- Magic (and cursed!) weapons.
- Large government commissions at wartime (not very profitable, but war loss can have serious consequences).
- Small government commissions (e.g. whip for judiciary punishment)
- Daily herald tells of news events (like adventurers being found dead or slaying a big enemy)


#Potential Future (post v1)

- Physical shop with limited capacity, ability to expand space, storage, functionality (i.e. purchasing a forge)
- Potential for shoplifting, robberies, need to hire guards
- Create CP437 sprite system (OpenGL, like Dwarf Fortress?)
- Build weapons based on components in addition to templates (e.g. long oak hilt, long curved steel blade, 2" joint)
	(more specific e.g.: axe head would be composed of heel, beard, bit, toe, cheek, eye, butt; haft composed of shoulder, belly, grip, throat, knob)


#To Do

- Create console-based dev menu for shop actions to act as starting point (make sure will be able to translate into a graphical system)
- Create mapping system and system to display map (ANSI, possibly to be replaced with real graphics)
	- How big should shop grid be?
	- Movable view when player gets close to screen boundary
- Determine turn-based or time-based system (mixed?)
	- If motion every tick, how responsive will keyboard movement be?
	- Time passes at motion, or when sitting at counter and pressing button?
- Flesh out concept of adventure locations
- Flesh out concept of resource locations
- Flesh out concept of new hero generation
- Create list of weapon types/classes/components/materials
- Devise town representation and system of player-town interaction
- Devise appraisal system to determine player's ability to determine worth/magic


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
	

#Town Shops

- Hunter (purchase raw leather/sinew/rawhide/bone)
- Farmer (puchase raw cotton/cannibis/silk)
- Textile Mill (create new linen/hemp/silk components)
- Mine (purchase raw metal ore / gems)
- Smelter (melt down metal items / ore)
- Blacksmith (create new metal components)
- Lumberjack (purchase raw wood)
- Woodcutter (create new wood components)
- Carpenter (expand shop, purchase furniture)
- Quarry (purchase raw stone)
- Stonemason (create new stone components)
- Jeweler (adorn items)
- Enchanter (enchant items)
- Priest (remove curses)


#Shop Furnishings

- Walls
- Doors?
- Counter?  Or just one fixed one?
- Display Case
- Weapon Rack
- Barrel (for parts)
- Chest
- Safe?
- Decorations? (decor could affect repeat business)


#Item Types

##Weapons

###Basic Qualities

- Unique ID Hash
- Class (e.g. sword, axe, etc.)
- Type (e.g. falchion, warhammer, etc.)
- Weight
- Materials (% for each?  For each component?)
- Joint quality (per joint; 0 = break at joint) (e.g. quality of lugs where axe head meets haft)
- Sharpness (possible null)
- Grip
- Durability (upon breaking, splits into component materials)
- Balance


###Materials (items may be made of more than one)

- Leather (e.g. whip, sling)
	- Cow
	- Goat
	- Deer
	- Horse
	- Bear
- Fiber (e.g. bow)
	- Linen
	- Hemp
	- Sinew
	- Silk
	- Rawhide
- Wood (e.g. spear, club)
	- Hickory
	- Ash
	- Oak
	- Pine
- Stone (e.g. tomahawk, sling bullet)
	- Granite
	- Marble
- Metal
	- Copper
	- Bronze (alloy)
	- Silver
	- Gold
	- Iron
	- Steel (alloy)
	- Mithril
	- Adamantium (alloy)

###Classes/Types/Components/Possible Materials

- Swords
	- Shortsword (1H)
		- Hilt
			- Wood, Stone, Metal
		- Blade
			- Metal
		- Scabbard
			- Leather, Wood, Metal
	- Longsword (2H)
		- Hilt
			- Wood, Stone, Metal
		- Blade
			- Metal
		- Scabbard
			- Leather, Wood, Metal
- Bludgeons
	- Club (1/2H)
		- Body
			- Wood
		- Head (optional)
			- Stone, Metal
	- Warhammer (1H)
		- Handle
			- Wood
		- Head
			- Stone, Metal
- Axes
	- Greataxe (2H)
		- Haft
			- Wood
		- Blade
			- Metal
- Bows
	- Shortbow (2H)
		- Upper Limb
			- Wood
		- Lower Limb
			- Wood
		- Bow String
			- Fiber
- Lashers
	- Whip (1H)
		- Hilt
			- Leather, Wood
		- Chord
			- Leather
		- Tail(s)
			- Leather, Metal
	- Flail (1H)
		- Handle
			- Wood
		- Chain(s)
			- Metal
		- Head(s)
			- Metal