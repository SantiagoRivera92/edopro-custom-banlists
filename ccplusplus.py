import urllib.request, json, operator
from datetime import datetime
header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
			'AppleWebKit/537.11 (KHTML, like Gecko) '
			'Chrome/23.0.1271.64 Safari/537.11',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'}
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
request = urllib.request.Request(url, None, header)

additionalForbidden = [
		"There Can Be Only One",
		"Artifact Scythe",
		"Moulinglacia the Elemental Lord"
		]
additionalLimited = [
		"Daigusto Emeral",
		"Trishula, Dragon of the Ice Barrier",
		"Redox, Dragon Ruler of Boulders",
		"Tidal, Dragon Ruler of Waterfalls",
		"Blaster, Dragon Ruler of Infernos",
		"Tempest, Dragon Ruler of Storms",
		"Astrograph Sorcerer",
		"Gladiator Beast Tamer Editor",
		"SPYRAL Resort",
		"Witchcrafter Creation"
		]
additionalSemiLimited = []
additionalUnlimited = [
	"\"Infernoble Arms - Durendal\"",
	"\"Infernoble Arms - Joyeuse\"",
	"Absorb Fusion",
	"Abyss Shark",
	"Abyss-sphere",
	"Abyss-squall",
	"Adamancipator Analyzer",
	"Adamancipator Seeker",
	"Adreus, Keeper of Armageddon",
	"Alpha The Electromagnet Warrior",
	"Alich, Malebranche of the Burning Abyss",
	"Altergeist Meluseek",
	"Ancient Warriors - Ambitious Cao De",
	"Ancient Warriors - Eccentric Lu Jing",
	"Ancient Warriors - Graceful Zhou Gong",
	"Ancient Warriors - Ingenious Zhuge Kong",
	"Ancient Warriors - Masterful Sun Mou",
	"Ancient Warriors - Rebellious Lu Feng",
	"Ancient Warriors - Valiant Zhang De",
	"Ancient Warriors - Virtuous Liu Xuan",
	"Ancient Warriors Saga - Defense of Changban",
	"Ancient Warriors Saga - Sun-Liu Alliance",
	"Ancient Warriors Saga - Three Visits",
	"Arcanite Magician",
	"Armades, Keeper of Boundaries",
	"Armor Ninjitsu Art of Rust Mist",
	"Artifact Durendal",
	"Artifact Sanctum",
	"Artorigus, King of the Noble Knights",
	"Assault Blackwing - Onimaru the Divine Thunder",
	"Assault Blackwing - Raikiri the Rain Shower",
	"Atomic Scrap Dragon",
	"Avalon",
	"Bahamut Shark",
	"Barbar, Malebranche of the Burning Abyss",
	"Batteryman Fuel Cell",
	"Batteryman Industrial Strength",
	"Battlin' Boxer Lead Yoke",
	"Beast Striker",
	"Beat, Bladesman Fur Hire",
	"Beautunaful Princess",
	"Berserkion the Electromagna Warrior",
	"Beta The Electromagnet Warrior",
	"Bi'an, Earth of the Yang Zing",
	"Bixi, Water of the Yang Zing",
	"Blackwing - Gale the Whirlwind",
	"Blackwing - Kris the Crack of Dawn",
	"Blackwing - Silverwind the Ascendant",
	"Blackwing - Simoon the Poison Wind",
	"Blackwing - Vayu the Emblem of Honor",
	"Blackwing Armor Master",
	"Blade Armor Ninja",
	"Blue Dragon Ninja",
	"Brionac, Dragon of the Ice Barrier",
	"Brotherhood of the Fire Fist - Bear",
	"Brotherhood of the Fire Fist - Cardinal",
	"Brotherhood of the Fire Fist - Dragon",
	"Brotherhood of the Fire Fist - Gorilla",
	"Brotherhood of the Fire Fist - Kirin",
	"Brotherhood of the Fire Fist - Lion Emperor",
	"Brotherhood of the Fire Fist - Rooster",
	"Brotherhood of the Fire Fist - Tiger King",
	"Bujin Arasuda",
	"Bujin Hiruko",
	"Bujin Hirume",
	"Bujin Mikazuchi",
	"Bujin Yamato",
	"Bujincarnation",
	"Bujingi Crane",
	"Bujingi Crow",
	"Bujingi Hare",
	"Bujingi Peacock",
	"Bujingi Quilin",
	"Bujintei Kagutsuchi",
	"Bujintei Susanowo",
	"Caam, Serenity of Gusto",
	"Cagna, Malebranche of the Burning Abyss",
	"Calcab, Malebranche of the Burning Abyss",
	"Celestial Observatory",
	"Ceruli, Guru of Dark World",
	"Chaos Valkyria",
	"Chiwen, Light of the Yang Zing",
	"Chow Sai the Ghost Stopper",
	"Chronomaly Aztec Mask Golem",
	"Chronomaly Cabrera Trebuchet",
	"Chronomaly City Babylon",
	"Chronomaly Colossal Head",
	"Chronomaly Crystal Chrononaut",
	"Chronomaly Crystal Skull",
	"Chronomaly Gordian Knot",
	"Chronomaly Magella Globe",
	"Chronomaly Mud Golem",
	"Chronomaly Nebra Disk",
	"Chronomaly Sol Monolith",
	"Chronomaly Tula Guardian",
	"Clear Wing Fast Dragon",
	"Clear Wing Synchro Dragon",
	"Code Generator",
	"Code Talker",
	"Comics Hero King Arthur",
	"Constellar Caduceus",
	"Constellar Omega",
	"Constellar Pollux",
	"Constellar Ptolemy M7",
	"Constellar Sombre",
	"Contact with Gusto",
	"Crimson Knight Vampire Bram",
	"Crusadia Magius",
	"Crusadia Maximus",
	"Crusadia Revival",
	"Crystal Shark",
	"Cyber Dragon Herz",
	"Cyber Eternity Dragon",
	"Cyber Revsystem",
	"Daigusto Eguls",
	"Daigusto Falcos",
	"Daigusto Gulldos",
	"Daigusto Laplampilica",
	"Daigusto Phoenix",
	"Daigusto Sphreez",
	"Dakki, the Graceful Mayakashi",
	"Dante, Pilgrim of the Burning Abyss",
	"Dark Armed, the Dragon of Annihilation",
	"Dark Honest",
	"Darkflare Dragon",
	"Darkness Metal, the Dragon of Dark Steel",
	"Decode Talker Extended",
	"Dewloren, Tiger King of the Ice Barrier",
	"Diamond Dire Wolf",
	"Digital Bug Rhinosebus",
	"Dinomist Pteran",
	"Dinomist Rex",
	"Divine Dragon Knight Felgrand",
	"Divine Dragon Lord Felgrand",
	"Divine Wind of Mist Valley",
	"Do a Barrel Roll",
	"Double Fin Shark",
	"Downerd Magician",
	"Draco Face-Off",
	"Draghig, Malebranche of the Burning Abyss",
	"Dragunity Arma Gram",
	"Dragunity Knight - Vajrayana",
	"Edea the Heavenly Squire",
	"Eidos the Underworld Squire",
	"Elemental HERO Nova Master",
	"Elemental HERO Sunrise",
	"Elemental HERO The Shining",
	"Elemental Training",
	"Elementsaber Lapauila",
	"Elementsaber Lapauila Mana",
	"Elementsaber Makani",
	"Elementsaber Molehu",
	"Elementsaber Nalu",
	"Encode Talker",
	"Evigishki Levianima",
	"Evigishki Merrowgeist",
	"Evigishki Soul Ogre",
	"Evigishki Tetrogre",
	"Evilswarm Bahamut",
	"Evilswarm Castor",
	"Evilswarm Kerykeion",
	"Evilswarm Ketos",
	"Evilswarm Ophion",
	"Evilswarm Ouroboros",
	"Evolzar Dolkka",
	"Excode Talker",
	"Fabled Andwraith",
	"Filo, Messenger Fur Hire",
	"Fire King Avatar Arvata",
	"Fire King Avatar Yaksha",
	"Fire King High Avatar Garunix",
	"Fire Lake of the Burning Abyss",
	"Fluffal Dog",
	"Fluffal Owl",
	"Fluffal Penguin",
	"Folgo, Justice Fur Hire",
	"Fool of Prophecy",
	"Frightfur Kraken",
	"Frightfur Sabre-Tooth",
	"Frightfur Tiger",
	"Frightfur Wolf",
	"Fusion Destiny",
	"Gachi Gachi Gantetsu",
	"Gadarla, the Mystery Dust Kaiju",
	"Gaia Drake, the Universal Force",
	"Galaxy Expedition",
	"Galaxy Knight",
	"Galaxy-Eyes Solflare Dragon",
	"Gallant Granite",
	"Gameciel, the Sea Turtle Kaiju",
	"Gamma The Electromagnet Warrior",
	"Gashadokuro, the Skeletal Mayakashi",
	"Gem-Armadillo",
	"Gem-Enhancement",
	"Gem-Knight Alexandrite",
	"Gem-Knight Aquamarine",
	"Gem-Knight Citrine",
	"Gem-Knight Crystal",
	"Gem-Knight Emerald",
	"Gem-Knight Lady Brilliant Diamond",
	"Gem-Knight Phantom Quartz",
	"Gem-Knight Prismaura",
	"Gem-Knight Ruby",
	"Gem-Knight Topaz",
	"Gem-Knight Zirconia",
	"Genex Ally Axel",
	"Genex Ally Bellflame",
	"Genex Ally Birdman",
	"Genex Ally Powercell",
	"Genex Ally Reliever",
	"Genex Ally Remote",
	"Genex Ally Triarm",
	"Genex Ally Triforce",
	"Genex Army",
	"Genex Furnace",
	"Genex Solar",
	"Genex Turbine",
	"Geo Genex",
	"Ghostrick Alucard",
	"Gishki Chain",
	"Gishki Psychelone",
	"Gishki Zielgigas",
	"Gladiator Beast Andabata",
	"Gladiator Beast Augustus",
	"Gladiator Beast Domitianus",
	"Gladiator Beast Essedarii",
	"Gladiator Beast Gyzarus",
	"Gladiator Beast Nerokius",
	"Gladiator Beast Noxious",
	"Gladiator Beast Retiari",
	"Gladiator Rejection",
	"Glory of the Noble Knights",
	"Glow-Up Bloom",
	"Glow-Up Bulb",
	"Gold Gadget",
	"Good & Evil in the Burning Abyss",
	"Gottoms' Second Call",
	"Grandsoil the Elemental Lord",
	"Granmarg the Mega Monarch",
	"Grapha, Dragon Lord of Dark World",
	"Great Sand Sea - Gold Golgonda",
	"Greatfly",
	"Gungnir, Dragon of the Ice Barrier",
	"Gusto Squirro",
	"Gwenhwyfar, Queen of Noble Arms",
	"Hajun, the Winged Mayakashi",
	"Heavy Armored Train Ironwolf",
	"Heavy Forward",
	"Heritage of the Chalice",
	"Heroic Challenger - Assault Halberd",
	"Hi-Speedroid Hagoita",
	"Hi-Speedroid Kitedrake",
	"Hidden Village of Ninjitsu Arts",
	"Hieratic Dragon King of Atum",
	"Hieratic Seal of Convocation",
	"Hieratic Sun Dragon Overlord of Heliopolis",
	"Hierophant of Prophecy",
	"High Priestess of Prophecy",
	"Hip Hoshiningen",
	"Horse of the Floral Knights",
	"Hot Red Dragon Archfiend",
	"Hot Red Dragon Archfiend Bane",
	"HTS Psyhemuth",
	"Hydro Genex",
	"Hyper Galaxy",
	"Ignoble Knight of Black Laundsallyn",
	"Ignoble Knight of High Laundsallyn",
	"Immortal Dragon",
	"Impcantation Candoll",
	"Impcantation Chalislime",
	"Infernal Flame Vixen",
	"Infernoble Knight - Roland",
	"Infestation Wave",
	"Infinitrack Anchor Drill",
	"Infinitrack Goliath",
	"Infinitrack River Stormer",
	"Infinitrack Trencher",
	"Inzektor Exa-Beetle",
	"Inzektor Exa-Stag",
	"Inzektor Giga-Mantis",
	"Inzektor Hopper",
	"Iron Core Specimen Lab",
	"Jet Synchron",
	"Jiaotu, Darkness of the Yang Zing",
	"Jurrac Giganoto",
	"Jurrac Herra",
	"Jurrac Iguanon",
	"Jurrac Meteor",
	"Jurrac Titano",
	"Jurrac Velo",
	"Jurrac Velphito",
	"Karakuri Barrel mdl 96 \"Shinkuro\"",
	"Karakuri Bushi mdl 6318 \"Muzanichiha\"",
	"Karakuri Merchant mdl 177 \"Inashichi\"",
	"Karakuri Muso mdl 818 \"Haipa\"",
	"Karakuri Ninja mdl 339 \"Sazank\"",
	"Karakuri Shogun mdl 00 \"Burei\"",
	"Karakuri Super Shogun mdl 00N \"Bureibu\"",
	"King of the Beasts",
	"Koa'ki Meiru Crusader",
	"Koa'ki Meiru Maximus",
	"Koa'ki Meiru Urnight",
	"Koa'ki Meiru Wall",
	"Kozmo Dark Destroyer",
	"Kozmo Dark Eclipser",
	"Kozmo Dark Planet",
	"Kozmo DOG Fighter",
	"Kozmo Farmgirl",
	"Kozmo Forerunner",
	"Kozmo Goodwitch",
	"Kozmo Landwalker",
	"Kozmo Scaredy Lion",
	"Kozmo Sliprider",
	"Kozmo Soartroopers",
	"Kozmo Strawman",
	"Kozmo Tincan",
	"Kozmojo",
	"Kozmoll Dark Lady",
	"Kozmotown",
	"Kumongous, the Sticky String Kaiju",
	"Lady of the Lake",
	"Landoise's Luminous Moss",
	"Last Chapter of the Noble Knights",
	"Laval Archer",
	"Laval Coatl",
	"Laval Judgment Lord",
	"Laval Miller",
	"Laval Stennon",
	"Laval the Greater",
	"Laval Warrior",
	"Lavalval Dragon",
	"Lavalval Ignis",
	"Lavalval Salamander",
	"Lector Pendulum, the Dracoverlord",
	"Legendary Six Samurai - Kageki",
	"Libic, Malebranche of the Burning Abyss",
	"Lightning Chidori",
	"Lightpulsar Dragon",
	"Linkmail Archfiend",
	"Locomotion R-Genex",
	"Luster Pendulum, the Dracoslayer",
	"Lyrilusc - Assembled Nightingale",
	"Lyrilusc - Beryl Canary",
	"Lyrilusc - Recital Starling",
	"Magical Musket - Cross-Domination",
	"Magical Musket - Dancing Needle",
	"Magical Musket - Desperado",
	"Magical Musket - Fiendish Deal",
	"Magical Musket - Last Stand",
	"Magical Musket - Steady Hands",
	"Magical Musketeer Calamity",
	"Magical Musketeer Caspar",
	"Magical Musketeer Doc",
	"Magical Musketeer Kidbrave",
	"Magical Musketeer Starfire",
	"Magical Musketeer Wild",
	"Magician of Hope",
	"Magician's Restage",
	"Magnet Induction",
	"Majespecter Cat - Nekomata",
	"Majespecter Cyclone",
	"Majespecter Raccoon - Bunbuku",
	"Majespecter Supercell",
	"Majespecter Toad - Ogama",
	"Majespecter Tornado",
	"Majesty's Pegasus",
	"Malacoda, Netherlord of the Burning Abyss",
	"Marincess Blue Slug",
	"Marincess Coral Anemone",
	"Master Hyperion",
	"Mayakashi Mayhem",
	"Mayakashi Metamorphosis",
	"Mayakashi Return",
	"Mayakashi Winter",
	"Mecha Phantom Beast Aerosguin",
	"Mecha Phantom Beast Blue Impala",
	"Mecha Phantom Beast Concoruda",
	"Mecha Phantom Beast Dracossack",
	"Mecha Phantom Beast Kalgriffin",
	"Mecha Phantom Beast Megaraptor",
	"Mecha Phantom Beast O-Lion",
	"Mecha Phantom Beast Turtletracer",
	"Mecha Phantom Beast Warbluran",
	"Megalith Ophiel",
	"Merlin",
	"Mermail Abyssalacia",
	"Mermail Abyssgaios",
	"Mermail Abyssgunde",
	"Mermail Abyssleed",
	"Mermail Abysslinde",
	"Mermail Abyssmander",
	"Mermail Abyssmegalo",
	"Mermail Abysspike",
	"Mermail Abyssteus",
	"Mermail Abysstrite",
	"Mermail Abyssturge",
	"Metaphys Horus",
	"Metaverse",
	"Micro Coder",
	"Missus Radiant",
	"Mist Wurm",
	"Moja",
	"Myutant Arsenal",
	"Myutant Beast",
	"Myutant Evolution Lab",
	"Myutant M-05",
	"Myutant Mist",
	"Myutant ST-46",
	"Myutant Synthesis",
	"Naturia Cherries",
	"Naturia Eggplant",
	"Naturia Gaiastrio",
	"Naturia Sacred Tree",
	"Necrovalley Throne",
	"Ninja Grandmaster Hanzo",
	"Ninja Grandmaster Saizo",
	"Ninjitsu Art of Duplication",
	"Ninjitsu Art of Mirage-Transformation",
	"Noble Arms - Excaliburn",
	"Noble Arms of Destiny",
	"Noble Knight Artorigus",
	"Noble Knight Bedwyr",
	"Noble Knight Borz",
	"Noble Knight Brothers",
	"Noble Knight Custennin",
	"Noble Knight Drystan",
	"Noble Knight Eachtar",
	"Noble Knight Gawayn",
	"Noble Knight Gwalchavad",
	"Noble Knight Iyvanne",
	"Noble Knight Medraut",
	"Noble Knight Pellinore",
	"Noble Knight Peredur",
	"Noble Knight's Shield-Bearer",
	"Noble Knight's Spearholder",
	"Noble Knights of the Round Table",
	"Nordic Beast Gullinbursti",
	"Nordic Relic Hlidskjalf",
	"Nordic Smith Ivaldi",
	"Number 36: Chronomaly Chateau Huyuk",
	"Number 37: Hope Woven Dragon Spider Shark",
	"Number 47: Nightmare Shark",
	"Number 64: Ronin Raccoon Sandayu",
	"Number 70: Malevolent Sin",
	"Number 101: Silent Honor ARK",
	"Number 106: Giant Hand",
	"Number S39: Utopia the Lightning",
	"Oafdragon Magician",
	"Oboro-Guruma, the Wheeled Mayakashi",
	"Onslaught of the Fire Kings",
	"Orient Dragon",
	"Pacifis, the Phantasm City",
	"Palace of the Elemental Lords",
	"Pantheism of the Monarchs",
	"Pendulumucho",
	"Performapal Celestial Magician",
	"Performapal Dag Daggerman",
	"Performapal Gentrude",
	"Performapal Parrotrio",
	"Phantasm Spiral Battle",
	"Phantom Skyblaster",
	"Photon Advancer",
	"Photon Alexandra Queen",
	"Photon Orbital",
	"Photon Wyvern",
	"Pilica, Descendant of Gusto",
	"Plunder Patroll Booty",
	"Plunder Patroll Shipyarrrd",
	"Possessed Partnerships",
	"Powercode Talker",
	"Protector of The Agents - Moon",
	"Proxy Dragon",
	"PSY-Framelord Zeta",
	"Pulao, Wind of the Yang Zing",
	"Purple Poison Magician",
	"Pyrorex the Elemental Lord",
	"Queen Dragun Djinn",
	"R-Genex Overseer",
	"R-Genex Ultimum",
	"Rasterliger",
	"Red Dragon Ninja",
	"Redbeard, the Plunder Patroll Matey",
	"Reeshaddoll Wendi",
	"Reflection of Endymion",
	"Reptilianne Melusine",
	"Reptilianne Ramifications",
	"Reptilianne Vaskii",
	"Revendread Executor",
	"Revendread Slayer",
	"Revived King Ha Des",
	"Rookie Warrior Lady",
	"Rubic, Malebranche of the Burning Abyss",
	"S-Force Bridgehead",
	"S-Force Chase",
	"S-Force Edge Razor",
	"S-Force Gravitino",
	"S-Force Justify",
	"S-Force Orrafist",
	"S-Force Pla-Tina",
	"S-Force Rappa Chiyomaru",
	"S-Force Retroactive",
	"Saber Hole",
	"Saber Slash",
	"Saber Vault",
	"Sacred Noble Knight of King Artorigus",
	"Sacred Noble Knight of King Custennin",
	"Salamangreat Balelynx",
	"Salamangreat Circle",
	"Salamangreat Spinny",
	"Samurai Destroyer",
	"Satellarknight Alsahm",
	"Satellarknight Altair",
	"Satellarknight Deneb",
	"Satellarknight Rigel",
	"Satellarknight Sirius",
	"Satellarknight Skybridge",
	"Scarm, Malebranche of the Burning Abyss",
	"Scramble!! Scramble!!",
	"Scrap Twin Dragon",
	"Seleglare the Luminous Lunar Dragon",
	"Shafu, the Wheeled Mayakashi",
	"Shien's Smoke Signal",
	"Shiranui Shogunsaga",
	"Shiranui Spectralsword",
	"Shiranui Spectralsword Shade",
	"Shiranui Squire",
	"Shiranui Sunsaga",
	"Shooting Star Dragon T.G. EX",
	"Shootingcode Talker",
	"Silent Sea Nettle",
	"Silver Gadget",
	"Skeletal Dragon Felgrand",
	"Snoww, Unlight of Dark World",
	"Soaring Eagle Above the Searing Land",
	"Some Summer Summoner",
	"Speedroid Dupligate",
	"Speedroid Rubberband Plane",
	"Speedroid Scratch",
	"Speedroid Wheel",
	"Spellbook Library of the Crescent",
	"Spellbook of Eternity",
	"Spellbook of Fate",
	"Spellbook of Life",
	"Spellbook of the Master",
	"Spellbook Star Hall",
	"Spirit Charmers",
	"Springans Merrymaker",
	"Springans Ship - Exblowrer",
	"Springans Watch",
	"SPYGAL Misty",
	"SPYRAL GEAR - Big Red",
	"SPYRAL GEAR - Utility Wire",
	"SPYRAL MISSION - Assault",
	"SPYRAL Super Agent",
	"SPYRAL Tough",
	"Star Eater",
	"Star Seraph Scale",
	"Star Seraph Scepter",
	"Star Seraph Sovereignty",
	"Stardust Charge Warrior",
	"Stardust Chronicle Spark Dragon",
	"Starliege Lord Galaxion",
	"Starliege Paladynamo",
	"Starliege Photon Blast Dragon",
	"Starlight Road",
	"Starry Knight Arrival",
	"Starry Knight Astel",
	"Starry Knight Balefire",
	"Starry Knight Blast",
	"Starry Knight Ceremony",
	"Starry Knight Flamel",
	"Starry Knight Rayel",
	"Starry Knight Sky",
	"Starry Night, Starry Dragon",
	"Steelswarm Caller",
	"Steelswarm Caucastag",
	"Steelswarm Girastag",
	"Steelswarm Hercules",
	"Steelswarm Longhorn",
	"Steelswarm Moth",
	"Steelswarm Origin",
	"Steelswarm Scout",
	"Steelswarm Sting",
	"Stellarknight Delteros",
	"Stellarknight Triverr",
	"Stellarnova Alpha",
	"Suanni, Fire of the Yang Zing",
	"Supreme King Gate Infinity",
	"Supreme King Gate Zero",
	"Suture Rebirth",
	"T.G. Blade Blaster",
	"T.G. Drill Fish",
	"T.G. Gear Zombie",
	"T.G. Halberd Cannon",
	"T.G. Metal Skeleton",
	"T.G. Screw Serpent",
	"T.G. Star Guardian",
	"T.G. Trident Launcher",
	"Talkback Lancer",
	"Taotie, Shadow of the Yang Zing",
	"Tellarknight Genesis",
	"Temperance of Prophecy",
	"Tengu, the Winged Mayakashi",
	"Test Panther",
	"TGX3-DX2",
	"The Agent of Life - Neptune",
	"The Agent of Miracles - Jupiter",
	"The Agent of Mystery - Earth",
	"The Executor of the Underworld - Pluto",
	"The Grand Spellbook Tower",
	"The Phantom Knights of Break Sword",
	"The Sacred Waters in the Sky",
	"The Terminus of the Burning Abyss",
	"The Traveler and the Burning Abyss",
	"Therion Charge",
	"Thermal Genex",
	"Thestalos the Mega Monarch",
	"Thought Ruler Archfiend",
	"Thunder Dragon Thunderstormech",
	"Thunder Dragondark",
	"Thunder Dragonduo",
	"Thunder Dragonhawk",
	"Thunder Dragonroar",
	"Time Seal",
	"Time Thief Perpetua",
	"Time Thief Temporwhal",
	"Tindangle Dholes",
	"Tindangle Jhrelth",
	"Tiras, Keeper of Genesis",
	"Traptrix Dionaea",
	"Traptrix Mantis",
	"Traptrix Myrmeleo",
	"Triamid Cruiser",
	"Triamid Hunter",
	"Triamid Kingolem",
	"Triamid Master",
	"Triamid Pulse",
	"Triamid Sphinx",
	"Tsuchigumo, the Poisonous Mayakashi",
	"Tsukahagi, the Poisonous Mayakashi",
	"Tuning Magician",
	"Twilight Ninja Jogen",
	"Twilight Ninja Kagen",
	"U.A. Blockbacker",
	"U.A. Goalkeeper",
	"U.A. Hyper Stadium",
	"U.A. Midfielder",
	"U.A. Mighty Slugger",
	"U.A. Playmaker",
	"U.A. Turnover Tactics",
	"Umbramirage the Elemental Lord",
	"Valiant Shark Lancer",
	"Vampire Duke",
	"Vampire Fascinator",
	"Vampire Fraulein",
	"Vampire Ghost",
	"Vampire Sorcerer",
	"Vampire Sucker",
	"Vampire Takeover",
	"Vampire Vamp",
	"Vampire Voivode",
	"Vector Pendulum, the Dracoverlord",
	"Vendread Charge",
	"Vendread Chimera",
	"Vendread Core",
	"Vendread Houndhorde",
	"Vendread Nights",
	"Vendread Reorigin",
	"Vendread Reunion",
	"Vendread Revolution",
	"Vindikite R-Genex",
	"Virtual World Beast - Jiujiu",
	"Virtual World Phoenix - Fanfan",
	"Vision HERO Vyon",
	"Vortex the Whirlwind",
	"Vylon Alpha",
	"Vylon Charger",
	"Vylon Cube",
	"Vylon Delta",
	"Vylon Disigma",
	"Vylon Epsilon",
	"Vylon Hept",
	"Vylon Material",
	"Vylon Omega",
	"Vylon Polytope",
	"Vylon Sigma",
	"Vylon Sphere",
	"Vylon Stigma",
	"Wandering King Wildwind",
	"War Rock Bashileos",
	"War Rock Dignity",
	"War Rock Fortia",
	"War Rock Gactos",
	"War Rock Meteoragon",
	"War Rock Spirit",
	"War Rock Wento",
	"Wattcastle",
	"Wattchimera",
	"Wattgiraffe",
	"Watthydra",
	"Wee Witch's Apprentice",
	"White Dragon Ninja",
	"Whitebeard, the Plunder Patroll Helm",
	"Wind-Up Arsenal Zenmaioh",
	"Wind-Up Magician",
	"Wind-Up Rabbit",
	"Wind-Up Rat",
	"Wind-Up Shark",
	"Wind-Up Zenmaines",
	"Wind-Up Zenmaintenance",
	"Windaar, Sage of Gusto",
	"Windmill Genex",
	"Winds Over the Ice Barrier",
	"Windwitch - Crystal Bell",
	"Windwitch - Diamond Bell",
	"Windwitch - Freeze Bell",
	"Windwitch - Winter Bell",
	"Windwitch Chimes",
	"Witchcrafter Bystreet",
	"Witchcrafter Collaboration",
	"Witchcrafter Draping",
	"Witchcrafter Edel",
	"Witchcrafter Haine",
	"Witchcrafter Holiday",
	"Witchcrafter Masterpiece",
	"Witchcrafter Pittore",
	"Witchcrafter Potterie",
	"Witchcrafter Scroll",
	"Witchcrafter Shmietta",
	"Witchcrafter Unveiling",
	"Worm King",
	"Worm Zero",
	"Xtra HERO Dread Decimator",
	"Xtra HERO Infernal Devicer",
	"XX-Saber Darksoul",
	"XX-Saber Emmersblade",
	"XX-Saber Gardestrike",
	"XX-Saber Garsem",
	"XX-Saber Gottoms",
	"XX-Saber Hyunlei",
	"Yang Zing Creation",
	"Yang Zing Path",
	"Yata-Garasu",
	"Yellow Dragon Ninja",
	"Yellow Ninja",
	"Yoko, the Graceful Mayakashi",
	"Zektrike Kou-ou",
	"Zuijin of the Ice Barrier"
	]

suspectList = [
	"\"Infernoble Arms - Durendal\"",
	"Abyss Shark",
	"Astrograph Sorcerer",
	"Brionac, Dragon of the Ice Barrier",
	"Clear Wing Fast Dragon",
	"Clear Wing Synchro Dragon",
	"Constellar Ptolemy M7",
	"Dakki, the Graceful Mayakashi",
	"Dark Armed the Dragon of Annihilation",
	"Divine Dragon Knight Felgrand",
	"Dragunity Arma Gram",
	"Evilswarm Ophion",
	"Fire King High Avatar Garunix",
	"Frightfur Kraken",
	"Frightfur Sabre-Tooth",
	"Galaxy-Eyes Solflare Dragon",
	"Gem-Knight Phantom Quartz",
	"Glow-Up Bloom",
	"Grapha, Dragon Lord of Dark World",
	"Hi-Speedroid Hagoita",
	"Hieratic Dragon King of Atum",
	"Karakuri Shogn mdl 00 \"Burei\"",
	"Mecha Phantom Beast Dracossack",
	"Mermail Abyssteus",
	"Noble Knight Borz",
	"Noble Knight Medraut",
	"Performapal Celestial Magician",
	"Purple Poison Magician",
	"Reflection of Endymion",
	"Salamangreat Balelynx",
	"T.G. Trident Launcher",
	"Vampire Fraulein",
	"Vision HERO Vyon",
	"Vylon Cube",
	"Vylon Sphere",
	"Wandering King Wildwind",
	"Zektrike Kou-ou"
]

considering = [
	"Paleozoic Opabinia", 
	"Paleozoic Anomalocaris",
	"Raidraptor - Tribute Lanius", 
	"Raidraptor - Strangle Lanius", 
	"Raider's Wing", 
	"Raidraptor - Necro Vulture", 
	"Raidraptor - Fiend Eagle", 
	"Raidraptor - Blaze Falcon", 
	"Raidraptor - Stranger Falcon",
	"Raidraptor - Revolution Falcon - Air Raid",
	"Raidraptor - Arsenal Falcon",
	"Raidraptor - Satellite Cannon Falcon",
	"Raidraptor - Final Fortress Falcon",
	"Rank-Up-Magic Soul Shave Force",
	"Rank-Up-Magic Raid Force",
	"Raidraptor - Call",
	"Rank-Up-Magic Skip Force",
	"Rank-Up-Magic Revolution Force",
	"Rank-Up-Magic Doom Double Force",
	"Phantom Knights' Rank-Up-Magic Force",
	"Raidraptor Replica",
	"Sky Cavalry Centaurea",
	"Psychic Wheeleder",
	"Reactor Slime",
	"Obelisk the Tormentor",
	"Slifer the Sky Dragon",
	"Egyptian God Slime",
	"The Winged Dragon of Ra",
	"Guardian Slime",
	"Ancient Chant",
	"Blaze Cannon",
	"Millennium Revelation",
	"Thunderforce Attack",
	"Fist of Fate",
	"Uria, Lord of Searing Flames",
	"Armityle the Chaos Phantasm",
	"Dimension Fusion Destruction",
	"Cerulean Skyfire",
	"Hyper Blaze",
	"Hamon, Lord of Striking Thunder",
	"Raviel, Lord of Phantasms",
	"Raviel, Lord of Phantasms - Shimmering Scraper",
	"Machina Metalcruncher",
	"Machina Air Raider",
	"Machina Possesstorage",
	"Machina Redeployment",
	"Super Express Bullet Train",
	"Fire Formation - Gyokkou",
	"Lyrilusc - Promenade Thrush",
	"Number F0: Utopic Future Slash",
	"Totem Bird",
	"Soul of Silvermountain",
	"Gunkan Suship Uni-class Super-Dreadnought",
]

#(C) is common, (SP) is Short Print, (SSP) is Super Short Print, (DNPR) is Duel Terminal common
legalRarities = ['(C)', '(SP)', '(SSP)', '(DNPR)']

#Banlist status
banned = 'Banned'
limited = 'Limited'
semi = 'Semi-Limited'

#YGOPRODECK API keys
data = 'data'
card_sets = 'card_sets'
banlist_info = 'banlist_info'
ban_tcg = 'ban_tcg'
rarity_code = 'set_rarity_code'
card_images = 'card_images'
cardType = 'type'

#Token stuff
token = 'Token'

#My keys
name = 'name'
cardId = 'id'
status = 'status'

#Filename for banlist file
banlistFilename = 'banlist/cc++.lflist.conf'
siteFilename ='site/plus/banlist.md'
consideringFilename ='site/plus/considering.md'

#Card arrays
siteCards = []
simpleCards = [] # List of all TCG legal cards for banlist generation
ocgCards = [] # List of all OCG exclusive cards for banlist generation.

def printAdditionalArrays():
	print("Did I misspell something?")
	print("Additional forbidden cards:")
	print(additionalForbidden)
	print("Additional limited cards:")
	print(additionalLimited)
	print("Additional semi-limited cards:")
	print(additionalSemiLimited)
	print("Additional unlimited cards:")
	print(additionalUnlimited)

def writeCardToBanlist(card, outfile):
	try:
		cardStatus = card.get(status)
		if cardStatus == -1:
			cardStatus = 0
		outfile.write("%d %d -- %s\n" % (card.get(cardId), cardStatus, card.get(name)))
	except TypeError:
		print(card)

def writeCardToSite(card, outfile):
	cardName = card.get(name)
	cardStatus = card.get(status)
	cardStatusAsText = "Unlimited"
	if (cardStatus == -1):
		cardStatusAsText = "Illegal"
	elif (cardStatus == 0):
		cardStatusAsText = "Forbidden"
	elif (cardStatus == 1):
		cardStatusAsText = "Limited"
	elif (cardStatus == 2):
		cardStatusAsText = "Semi-Limited"

	if cardName in suspectList:
		cardStatusAsText = "%s (!!)"%cardStatusAsText

	cardUrl = "https://db.ygoprodeck.com/card/?search=%s"%card.get(name).replace(" ", "%20").replace("&", "%26")		
	outfile.write("\n| [%s](%s) | %s |"%(card.get(name), cardUrl, cardStatusAsText))

def writeCardsToSite(cards, outfile):
	for card in sorted(cards, key=operator.itemgetter('status')):
		if card.get(status) > -1:
			writeCardToSite(card,outfile)

def writeConsideringCards(cards, outfile):
	for card in cards:
		if card.get(status) == -1:
			writeCardToSite(card,outfile)

def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity ++\"\n---")
	outfile.write("\n\n## Common Charity++ F&L List\n\n")
	outfile.write("Please note if a card is not here, it is subject to normal [Common Charity legality](/edopro-custom-banlists/site/ccbanlist)\n\n")
	outfile.write("[You can find the EDOPRO banlist here](https://drive.google.com/file/d/1-1HTHnYJyKyyBg94iAwFm-uNayfp0yyT/view?usp=sharing). Open the link, click on the three dots in the top right and then click Download.\n\n")
	outfile.write("The banlist file goes into the lflists folder in your EDOPRO installation folder. Assuming you use Windows, it usually is C:/ProjectIgnis/lflists\n\n")
	outfile.write("EDOPRO will not recognize a change in banlists while it is open. You will have to restart EDOPRO for the changes to be reflected.\n\n")
	outfile.write("Cards with (!!) after their status are considered potentially problematic and might get removed from the format in the future.\n\n")
	outfile.write("You can see a list of cards we're considering to introduce to the format [here](considering). Note this does not guarantee it ever makes it into CC++.\n\n")
	outfile.write("The philosophy of this format can be summarized in: No Extra Deck based omninegates and no Link 2 and below extension. Payoffs are kept at a level where you cannot make multiple negations turn 1, so decks are forced to prioritize follow-up and grind game.")
	outfile.write("\n\n| Card name | Status |")
	outfile.write("\n| :-- | :-- |")

def writeConsideringHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity ++\"\n---")
	outfile.write("\n\n## Common Charity++ Consideration List\n\n")
	outfile.write("None of these cards are legal, but they might be in the future.")
	outfile.write("\n\n| Card name | Status |")
	outfile.write("\n| :-- | :-- |")

def writeFooter(outfile):
	outfile.write("\n\n###### [Back home](/edopro-custom-banlists/site/index)")

def printSite():
	with open(siteFilename, 'w', encoding="utf-8") as siteFile:
		writeHeader(siteFile)
		writeCardsToSite(siteCards, siteFile)
		writeFooter(siteFile)
	with open(consideringFilename, 'w', encoding ="utf-8") as consideringFile:
		writeConsideringHeader(consideringFile)
		writeConsideringCards(siteCards, consideringFile)
		writeFooter(consideringFile)

def printBanlist():
	with open(banlistFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[CC++ Format]\n")
		outfile.write("!CC++ %s.%s\n\n" % (datetime.now().month, datetime.now().year))
		outfile.write("\n#OCG Cards\n\n")
		for card in ocgCards:
			writeCardToBanlist(card, outfile)
		outfile.write("\n#Regular Banlist\n\n")
		for card in simpleCards:
			writeCardToBanlist(card, outfile)

def generateArrays():
	with urllib.request.urlopen(request) as url:
		cards = json.loads(url.read().decode()).get(data)
		for card in cards:
			if card.get(card_sets) != None:
				images = card.get(card_images)
				banInfo = card.get(banlist_info)
				banTcg = 3
				if (banInfo == None):
					banTcg = 3	
				if (banInfo != None):
					banlistStatus = banInfo.get(ban_tcg)
					if (banlistStatus == None):
						banTcg = 3
					if (banlistStatus == banned):
						banTcg = 0
					if (banlistStatus == limited):
						banTcg = 1
					if (banlistStatus == semi):
						banTcg = 2

				cardSets = card.get(card_sets)
				hasCommonPrint = False
				for printing in cardSets:
					if printing.get(rarity_code) in legalRarities:
						hasCommonPrint = True

				if not hasCommonPrint:
					banTcg = -1

				cardName = card.get(name)
				pushToSite = False
				if cardName in additionalForbidden:
					if (banTcg != 0):
						banTcg = 0
						additionalForbidden.remove(cardName)
						pushToSite = True
				if cardName in additionalLimited:
					if (banTcg != 1):
						banTcg = 1
						additionalLimited.remove(cardName)
						pushToSite = True
				if cardName in additionalSemiLimited:
					if (banTcg != 2):
						banTcg = 2
						additionalSemiLimited.remove(cardName)
						pushToSite = True
				if cardName in additionalUnlimited:
					if (banTcg != 3):
						banTcg = 3
						additionalUnlimited.remove(cardName)
						pushToSite = True

				if cardName in considering:
					banTcg = -1
					considering.remove(cardName)
					pushToSite = True

				alreadyInSite = False
				for variant in images:
					simpleCard = {}
					simpleCard[name] = cardName
					simpleCard[status] = banTcg
					simpleCard[cardId] = variant.get(cardId)
					if not alreadyInSite:
						if pushToSite:
							siteCards.append(simpleCard)
						alreadyInSite = True
					if (banTcg<3):
						simpleCards.append(simpleCard)

			if (card.get(card_sets)) == None and card.get(cardType) != token:
				for variant in card.get(card_images):
					simpleCard = {}
					simpleCard[name] = cardName
					simpleCard[status] = -1
					variantCardId = variant.get(cardId)
					simpleCard[cardId] = variantCardId
					ocgCards.append(simpleCard)

generateArrays()
printBanlist()
printSite()
printAdditionalArrays()