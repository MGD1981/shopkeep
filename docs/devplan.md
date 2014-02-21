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
- New resource or adventure sites may be discovered or come into existence (e.g. depleted/abandoned mine may become dungeon).
- Becoming self-sufficient may anger neglected shops, who could attempt to rob/damange player's shop; player could hire guards.
- Humorous hate-thy-neighbor relationship with neighboring apothecary?
- Ability to auto-transact by setting buy/sell rules; easy method to view/query rules.
- Magic (and cursed!) weapons.  "Curses" are just maleficial magic.
- Large government commissions at wartime (not very profitable, but war loss can have serious consequences).
- Small government commissions (e.g. whip for judiciary punishment)
- Daily herald tells of news events (like adventurers being found dead or slaying a big enemy)
- Try to keep minimal personal apotheosis, but town may improve based in part on player's actions.
- Player able to haggle and potentially deceive customers (e.g. convince someone that a cursed sword is actually magically bless and worth more than normal, or once belonged to an historical figure).  Charisma stat?
- Weapons based more on real life/history than D&D?


#Potential Future (post v1)

- Physical shop with limited capacity, ability to expand space, storage, functionality (i.e. purchasing a forge)
- Potential for shoplifting, robberies, need to hire guards
- Create CP437 sprite system (OpenGL, like Dwarf Fortress?)
- Build weapons based on components in addition to templates (e.g. long oak hilt, long curved steel blade, 2" joint)
	(more specific e.g.: axe head would be composed of heel, beard, bit, toe, cheek, eye, butt; haft composed of shoulder, belly, grip, throat, knob)
- World map which shows adventure, resource locations, etc.
- Option to choose a starting town based on world map
	- Potential sites have different surrounding known resource & adventure sites, and different pre-existing shops.
- Ability to move around town to go to other shops, etc.
	- Dynamically growing town
	- Museum of legendary heroes, which may house the weapons of retired/slain adventurers (if they don't come back to the shop)


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
	- Class?  (e.g. thieves would loot dungeons and run [and try to steal from shop], fighters would battle more)
	- Size
	- Personality (may not include in v1, but may be vital for gullibility)

- Variables
	- Weapon Class Familiarity (value for each class) - affects combat, possibly appraisal
	- Weapon Type Familiarity (value for each type) - affects combat, possibly appraisal
	- Specific Weapon Familiarity (value for each weapon ever wielded)
	- Impression of shopkeep
	- Impression of shop
	- Gullibility?
	- Guile?
	
	
#Player Traits
	There should be no general reputation -- just an impression specific to each shopper, which may be shared.
	There should be no gullibility/guile, as these are choices made by the player.

- Constants
	- Name?  Or leave as generic "shopkeep"?
	- Sex?  Or leave genderless?  Or female?	

- Variables
	- Charisma?  If so, should it be constant or variable?  Should it have separate facets (e.g. appearance, language skill, etc.)?
	- Appraisal ability?  If so, should it be constant or variable?  Appraisal ability for each weapon? Class? Material? Magic type?


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
- Dispeller (remove enhantments)


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
(using http://en.wikipedia.org/wiki/List_of_medieval_weapons -- TODO: filter to ~1400)

- Daggers/Knives
	- Baselard
	- Cinquedea
	- Ear dagger
	- Großes Messer
	- Katar
	- Mercygiver
	- Poniard
	- Rondel
	- Scramasax
	- Sgian
	- Stiletto
	- Dirk
	- Anelace
	- Parrying Dagger
	- Seax
	- Sai

- Swords
	- Arming sword
	- Shortsword (1H)
		- Hilt
			- Wood, Stone, Metal
		- Blade
			- Metal
		- Scabbard
			- Leather, Wood, Metal
	- Zweihander
	- Claymore
	- Longsword (2H)
		- Hilt
			- Wood, Stone, Metal
		- Blade
			- Metal
		- Scabbard
			- Leather, Wood, Metal
	- Broadsword
	- Falchion
	- Flamberge
	- Sabre
	- Katana

- Blunt/Cleaving Weapons
	- Battle axe (2H)
		- Haft
			- Wood
		- Blade
			- Metal
	- Club (1/2H)
		- Body
			- Wood
		- Head (optional)
			- Stone, Metal
	- Flail (1H)
		- Handle
			- Wood
		- Chain(s)
			- Metal
		- Head(s)
			- Metal
	- Mace
	- Flanged mace
	- Pernach
	- Shestopyor
	- Maul
	- Morning star
	- Quarterstaff
	- War hammer (1H)
		- Handle
			- Wood
		- Head
			- Stone, Metal
	- Bec de Corbin
	- Horseman's pick
	- Bludgeon

- Polearms
	- Bardiche
	- Bill
	- Glaive
	- Guisarme
	- Halberd
	- Lance
	- Lochaber Axe
	- Lucerne hammer
	- Man catcher
	- Military fork, the weaponized Pitchfork
	- Partisan
	- Pike
	- Plançon a picot
	- Ranseur
	- Sovnya
	- Spetum
	- Swordstaff
	- Voulge
	- War-scythe
	- War hammer (2H)

- Ranged (separate into thrown/drawn?)
	- Bombard
	- Longbow (2H)
		- Upper Limb
			- Wood
		- Lower Limb
			- Wood
		- Bow String
			- Fiber)
	- Recurve bow
	- Arbalest
	- Ballista
	- Repeating crossbow
	- Sling
	- Francisca
	- Nzappa zap
	- Tomahawk
	- Throwing Spear
	- Shuriken
	- Chakram
	- Culverin
	- Musket
	
- Lashers
    - Whip (1H)
		- Hilt
			- Leather, Wood
		- Chord
			- Leather
		- Tail(s)
			- Leather, Metal

