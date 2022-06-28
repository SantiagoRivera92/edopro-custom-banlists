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
		"Astrograph Sorcerer"
		]
additionalSemiLimited = []
additionalUnlimited = [
	"Diamond Dire Wolf",
	"Number S39: Utopia the Lightning", 
	"Gladiator Beast Augustus", 
	"Gladiator Beast Retiari", 
	"Gladiator Beast Gyzarus",
	"Test Panther",
	"Gladiator Beast Andabata",
	"Gladiator Beast Domitianus",
	"Koa'ki Meiru Urnight",
	"Shiranui Spectralsword",
	"Vision HERO Vyon",
	"Shiranui Shogunsaga",
	"Traptrix Myrmeleo",
	"Traptrix Dionaea",
	"Traptrix Mantis",
	"Ghostrick Alucard",
	"Brotherhood of the Fire Fist - Bear",
	"Shiranui Sunsaga",
	"Necrovalley Throne",
	"Wind-Up Zenmaines",
	"Heroic Challenger - Assault Halberd",
	"Evolzar Dolkka",
	"Gachi Gachi Gantetsu",
	"Number 101: Silent Honor ARK",
	"Master Hyperion",
	"The Agent of Miracles - Jupiter",
	"The Agent of Mystery - Earth",
	"The Agent of Life - Neptune",
	"The Executor of the Underworld - Pluto",
	"Protector of The Agents - Moon",
	"The Sacred Waters in the Sky",
	"Salamangreat Spinny",
	"Salamangreat Balelynx",
	"Salamangreat Circle",
	"Bujin Hiruko",
	"Bujin Hirume",
	"Bujin Mikazuchi",
	"Bujingi Peacock",
	"Bujin Yamato",
	"Bujingi Crow",
	"Bujingi Hare",
	"Bujin Arasuda",
	"Bujingi Quilin",
	"Bujingi Crane",
	"Bujintei Susanowo",
	"Bujintei Kagutsuchi",
	"Bujincarnation",
	"Springans Ship - Exblowrer",
	"Springans Merrymaker",
	"Springans Watch",
	"Great Sand Sea - Gold Golgonda",
	"Pacifis, the Phantasm City",
	"Phantasm Spiral Battle",
	"Marincess Blue Slug",
	"Marincess Coral Anemone",
	"U.A. Hyper Stadium",
	"Altergeist Meluseek",
	"Battlin' Boxer Lead Yoke",
	"Digital Bug Rhinosebus",
	"Impcantation Candoll",
	"Impcantation Chalislime",
	"Infinitrack Trencher",
	"Infinitrack Anchor Drill",
	"Infinitrack River Stormer",
	"Infinitrack Goliath",
	"Heavy Forward",
	"Koa'ki Meiru Maximus",
	"Koa'ki Meiru Wall",
	"Iron Core Specimen Lab",
	"Starlight Road",
	"Magical Musketeer Wild",
	"Magical Musketeer Calamity",
	"Magical Musketeer Starfire",
	"Magical Musketeer Kidbrave",
	"Magical Musketeer Doc",
	"Magical Musketeer Caspar",
	"Magical Musket - Steady Hands",
	"Magical Musket - Cross-Domination",
	"Magical Musket - Desperado",
	"Magical Musket - Dancing Needle",
	"Magical Musket - Fiendish Deal",
	"Magical Musket - Last Stand",
	"Gladiator Beast Noxious",
	"Megalith Ophiel",
	"Mermail Abyssleed",
	"Mermail Abyssmegalo",
	"Mermail Abyssteus",
	"Mermail Abyssturge",
	"Mermail Abysspike",
	"Mermail Abyssmander",
	"Mermail Abysslinde",
	"Mermail Abyssgunde",
	"Mermail Abyssgaios",
	"Mermail Abyssalacia",
	"Mermail Abysstrite",
	"Abyss-squall",
	"Abyss-sphere",
	"Myutant Arsenal",
	"Myutant Mist",
	"Myutant Beast",
	"Myutant ST-46",
	"Myutant M-05",
	"Myutant Synthesis",
	"Myutant Evolution Lab",
	"Gladiator Rejection",
	"Abyss Shark",
	"Crystal Shark",
	"Double Fin Shark",
	"Valiant Shark Lancer",
	"Beautunaful Princess",
	"Silent Sea Nettle",
	"Bahamut Shark",
	"Number 37: Hope Woven Dragon Spider Shark",
	"Number 70: Malevolent Sin",
	"Number 47: Nightmare Shark",
	"Satellarknight Rigel",
	"Satellarknight Altair",
	"Satellarknight Sirius",
	"Satellarknight Deneb",
	"Satellarknight Alsahm",
	"Stellarknight Triverr",
	"Stellarknight Delteros",
	"Satellarknight Skybridge",
	"Tellarknight Genesis",
	"Stellarnova Alpha",
	"The Phantom Knights of Break Sword",
	"Time Thief Adjuster",
	"Time Thief Temporwhal",
	"Time Thief Double Barrel",
	"Time Thief Perpetua",
	"Thunder Dragonduo",
	"Thunder Dragondark",
	"Thunder Dragonroar",
	"Thunder Dragonhawk",
	"Thunder Dragon Thunderstormech",
	"Some Summer Summoner",
	"Batteryman Industrial Strength",
	"Batteryman Fuel Cell",
	"Vampire Voivode",
	"Vampire Vamp",
	"Vampire Duke",
	"Vampire Sorcerer",
	"Vampire Ghost",
	"Crimson Knight Vampire Bram",
	"Vampire Fascinator",
	"Vampire Takeover",
	"Vampire Sucker",
	"Wattgiraffe",
	"Watthydra",
	"Wattchimera",
	"Wattcastle",
	"Suanni, Fire of the Yang Zing",
	"Bi'an, Earth of the Yang Zing",
	"Bixi, Water of the Yang Zing",
	"Jiaotu, Darkness of the Yang Zing",
	"Pulao, Wind of the Yang Zing",
	"Chiwen, Light of the Yang Zing",
	"Yang Zing Path",
	"Yang Zing Creation",
	"Beat, Bladesman Fur Hire",
	"Filo, Messenger Fur Hire",
	"Folgo, Justice Fur Hire",
	"XX-Saber Gardestrike",
	"XX-Saber Garsem",
	"XX-Saber Emmersblade",
	"XX-Saber Darksoul",
	"XX-Saber Gottoms",
	"XX-Saber Hyunlei",
	"Saber Slash",
	"Gottoms' Second Call",
	"Saber Vault",
	"Saber Hole",
	"Karakuri Muso mdl 818 \"Haipa\"",
	"Karakuri Bushi mdl 6318 \"Muzanichiha\"",
	"Karakuri Ninja mdl 339 \"Sazank\"",
	"Karakuri Merchant mdl 177 \"Inashichi\"",
	"Karakuri Barrel mdl 96 \"Shinkuro\"",
	"Karakuri Shogun mdl 00 \"Burei\"",
	"Karakuri Super Shogun mdl 00N \"Bureibu\"",
	"Shiranui Squire",
	"Gadarla, the Mystery Dust Kaiju",
	"Gameciel, the Sea Turtle Kaiju",
	"Kumongous, the Sticky String Kaiju",
	"Blackwing - Simoon the Poison Wind",
	"Blackwing - Kris the Crack of Dawn",
	"Blackwing - Gale the Whirlwind",
	"Blackwing - Vayu the Emblem of Honor",
	"Blackwing Armor Master",
	"Assault Blackwing - Raikiri the Rain Shower",
	"Blackwing - Silverwind the Ascendant",
	"Assault Blackwing - Onimaru the Divine Thunder",
	"Orient Dragon",
	"Stardust Charge Warrior",
	"Thought Ruler Archfiend",
	"Mist Wurm",
	"Virtual World Beast - Jiujiu",
	"Virtual World Phoenix - Fanfan",
	"Fabled Andwraith",
	"Chronomaly City Babylon",
	"Chronomaly Crystal Chrononaut",
	"Number 36: Chronomaly Chateau Huyuk",
	"Chronomaly Gordian Knot",
	"Chronomaly Crystal Skull",
	"Chronomaly Cabrera Trebuchet",
	"Chronomaly Colossal Head",
	"Chronomaly Magella Globe",
	"Chronomaly Aztec Mask Golem",
	"Chronomaly Mud Golem",
	"Chronomaly Nebra Disk",
	"Chronomaly Tula Guardian",
	"Chronomaly Sol Monolith",
	"Triamid Sphinx",
	"Triamid Master",
	"Triamid Hunter",
	"Triamid Cruiser",
	"Triamid Kingolem",
	"Triamid Pulse",
	"Alpha The Electromagnet Warrior",
	"Beta The Electromagnet Warrior",
	"Gamma The Electromagnet Warrior",
	"Berserkion the Electromagna Warrior",
	"Magnet Induction",
	"Reptilianne Vaskii",
	"Reptilianne Melusine",
	"Reptilianne Ramifications",
	"Gallant Granite",
	"Mecha Phantom Beast Dracossack",
	"PSY-Framelord Zeta",
	"Star Eater",
	"Celestial Observatory",
	"Yellow Dragon Ninja",
	"White Dragon Ninja",
	"Twilight Ninja Jogen",
	"Red Dragon Ninja",
	"Blue Dragon Ninja",
	"Yellow Ninja",
	"Ninja Grandmaster Hanzo",
	"Twilight Ninja Kagen",
	"Blade Armor Ninja",
	"Elemental HERO The Shining",
	"Elemental HERO Nova Master",
	"Ninja Grandmaster Saizo",
	"Hidden Village of Ninjitsu Arts",
	"Armor Ninjitsu Art of Rust Mist",
	"Ninjitsu Art of Duplication",
	"Ninjitsu Art of Mirage-Transformation",
	"Speedroid Rubberband Plane",
	"Hi-Speedroid Kitedrake",
	"Hi-Speedroid Hagoita",
	"Speedroid Scratch",
	"Speedroid Wheel",
	"Speedroid Dupligate",
	"Clear Wing Fast Dragon",
	"Clear Wing Synchro Dragon",
	"Fluffal Dog",
	"Fluffal Penguin",
	"Fluffal Owl",
	"Frightfur Wolf",
	"Frightfur Tiger",
	"Frightfur Sabre-Tooth",
	"Frightfur Kraken",
	"Suture Rebirth",
	"Evilswarm Ketos",
	"Evilswarm Castor",
	"Evilswarm Kerykeion",
	"Evilswarm Ophion",
	"Evilswarm Ouroboros",
	"Evilswarm Bahamut",
	"Constellar Pollux",
	"Constellar Caduceus",
	"Constellar Sombre",
	"Constellar Ptolemy M7",
	"Constellar Omega",
	"Wind-Up Shark",
	"Wind-Up Magician",
	"Wind-Up Rabbit",
	"Wind-Up Rat",
	"Wind-Up Arsenal Zenmaioh",
	"Wind-Up Zenmaintenance",
	"Inzektor Giga-Mantis",
	"Inzektor Hopper",
	"Inzektor Exa-Beetle",
	"Inzektor Exa-Stag",
	"Zektrike Kou-ou",
	"Artifact Sanctum",
	"Worm King",
	"Worm Zero",
	"Tindangle Dholes",
	"Tindangle Jhrelth",
	"Fusion Destiny",
	"Gladiator Beast Nerokius",
	"Dark Honest",
	"Starry Knight Rayel",
	"Starry Knight Flamel",
	"Starry Knight Astel",
	"Starry Knight Balefire",
	"Starry Knight Ceremony",
	"Starry Knight Sky",
	"Starry Knight Blast",
	"Starry Knight Arrival",
	"Starry Night, Starry Dragon",
	"Rookie Warrior Lady",
	"Grapha, Dragon Lord of Dark World",
	"Snoww, Unlight of Dark World",
	"Ceruli, Guru of Dark World",
	"Shafu, the Wheeled Mayakashi",
	"Tsukahagi, the Poisonous Mayakashi",
	"Dakki, the Graceful Mayakashi",
	"Hajun, the Winged Mayakashi",
	"Gashadokuro, the Skeletal Mayakashi",
	"Yoko, the Graceful Mayakashi",
	"Tengu, the Winged Mayakashi",
	"Tsuchigumo, the Poisonous Mayakashi",
	"Oboro-Guruma, the Wheeled Mayakashi",
	"Mayakashi Return",
	"Mayakashi Winter",
	"Mayakashi Metamorphosis",
	"Mayakashi Mayhem",
	"U.A. Midfielder",
	"U.A. Playmaker",
	"U.A. Blockbacker",
	"U.A. Goalkeeper",
	"U.A. Mighty Slugger",
	"U.A. Turnover Tactics",
	"S-Force Pla-Tina",
	"S-Force Gravitino",
	"S-Force Orrafist",
	"S-Force Edge Razor",
	"S-Force Rappa Chiyomaru",
	"S-Force Retroactive",
	"S-Force Justify",
	"S-Force Bridgehead",
	"S-Force Chase",
	"Lyrilusc - Assembled Nightingale",
	"Lyrilusc - Beryl Canary",
	"Lyrilusc - Recital Starling",
	"Legendary Six Samurai - Kageki",
	"Shien's Smoke Signal",
	"Windaar, Sage of Gusto",
	"Caam, Serenity of Gusto",
	"Pilica, Descendant of Gusto",
	"Gusto Squirro",
	"Daigusto Eguls",
	"Daigusto Sphreez",
	"Daigusto Laplampilica",
	"Daigusto Gulldos",
	"Daigusto Falcos",
	"Daigusto Phoenix",
	"Contact with Gusto",
	"Divine Wind of Mist Valley",
	"Genex Ally Birdman",
	"Chaos Valkyria",
	"Phantom Skyblaster",
	"Metaverse",
	"Time Seal",
	"Yata-Garasu",
	"Draco Face-Off",
	"Lightpulsar Dragon",
	"Darkflare Dragon",
	"Dragunity Knight - Vajrayana",
	"Dragunity Arma Gram",
	"Therion Charge",
	"Adamancipator Analyzer",
	"Adamancipator Seeker",
	"Glow-Up Bulb",
	"Tiras, Keeper of Genesis",
	"Adreus, Keeper of Armageddon",
	"Hieratic Seal of Convocation",
	"Hieratic Dragon King of Atum",
	"Divine Dragon Knight Felgrand",
	"Hieratic Sun Dragon Overlord of Heliopolis",
	"Divine Dragon Lord Felgrand",
	"Skeletal Dragon Felgrand",
	"Revived King Ha Des",
	"Immortal Dragon",
	"Glow-Up Bloom",
	"Vampire Fraulein",
	"Missus Radiant",
	"Hip Hoshiningen",
	"Proxy Dragon",
	"Wee Witch's Apprentice",
	"Greatfly",
	"Linkmail Archfiend",
	"Darkness Metal, the Dragon of Dark Steel",
	"Rasterliger",
	"Dark Armed, the Dragon of Annihilation",
	"Downerd Magician",
	"Hot Red Dragon Archfiend",
	"Hot Red Dragon Archfiend Bane",
	"Wandering King Wildwind",
	"Artifact Durendal",
	"Gaia Drake, the Universal Force",
	"Gishki Chain",
	"Gishki Psychelone",
	"Evigishki Tetrogre",
	"Evigishki Levianima",
	"Evigishki Soul Ogre",
	"Gishki Zielgigas",
	"Evigishki Merrowgeist",
	"Micro Coder",
	"Encode Talker",
	"Powercode Talker",
	"Decode Talker Extended",
	"Shootingcode Talker",
	"Excode Talker",
	"Talkback Lancer",
	"Code Talker",
	"Code Generator",
	"Magician of Hope",
	"Comics Hero King Arthur",
	"Heavy Armored Train Ironwolf",
	"Infernal Flame Vixen",
	"Queen Dragun Djinn",
	"Number 106: Giant Hand",
	"Starliege Paladynamo",
	"Lightning Chidori",
	"Atomic Scrap Dragon",
	"Stardust Chronicle Spark Dragon",
	"Scrap Twin Dragon",
	"Windwitch - Diamond Bell",
	"Samurai Destroyer",
	"Windwitch - Winter Bell",
	"Arcanite Magician",
	"HTS Psyhemuth",
	"Metaphys Horus",
	"Armades, Keeper of Boundaries",
	"Vortex the Whirlwind",
	"Crusadia Maximus",
	"Crusadia Magius",
	"Crusadia Revival",
	"Windwitch - Freeze Bell",
	"Windwitch - Crystal Bell",
	"Windwitch Chimes",
	"Nordic Smith Ivaldi",
	"Nordic Beast Gullinbursti",
	"Nordic Relic Hlidskjalf",
	"Galaxy Knight",
	"Photon Wyvern",
	"Photon Advancer",
	"Photon Orbital",
	"Photon Alexandra Queen",
	"Starliege Lord Galaxion",
	"Starliege Photon Blast Dragon",
	"Galaxy Expedition",
	"Hyper Galaxy",
	"Galaxy-Eyes Solflare Dragon",
	"Majespecter Toad - Ogama",
	"Majespecter Raccoon - Bunbuku",
	"Majespecter Cat - Nekomata",
	"Majespecter Cyclone",
	"Majesty's Pegasus",
	"Majespecter Tornado",
	"Majespecter Supercell",
	"Gold Gadget",
	"Silver Gadget",
	"T.G. Screw Serpent",
	"T.G. Metal Skeleton",
	"T.G. Gear Zombie",
	"T.G. Drill Fish",
	"T.G. Blade Blaster",
	"Shooting Star Dragon T.G. EX",
	"T.G. Halberd Cannon",
	"T.G. Star Guardian",
	"T.G. Trident Launcher",
	"TGX3-DX2",
	"Vendread Houndhorde",
	"Vendread Core",
	"Revendread Executor",
	"Revendread Slayer",
	"Vendread Chimera",
	"Vendread Charge",
	"Vendread Nights",
	"Vendread Reunion",
	"Vendread Revolution",
	"Vendread Reorigin",
	"Cyber Revsystem",
	"Cyber Eternity Dragon",
	"Cyber Dragon Herz",
	"Number 64: Ronin Raccoon Sandayu",
	"Fire King Avatar Yaksha",
	"Fire King Avatar Arvata",
	"Fire King High Avatar Garunix",
	"Onslaught of the Fire Kings",
	"Star Seraph Scepter",
	"Star Seraph Scale",
	"Star Seraph Sovereignty",
	"Elementsaber Lapauila Mana",
	"Elementsaber Molehu",
	"Elementsaber Lapauila",
	"Elementsaber Nalu",
	"Elementsaber Makani",
	"Palace of the Elemental Lords",
	"Elemental Training",
	"Pyrorex the Elemental Lord",
	"Umbramirage the Elemental Lord",
	"Grandsoil the Elemental Lord",
	"Edea the Heavenly Squire",
	"Eidos the Underworld Squire",
	"Pantheism of the Monarchs",
	"Thestalos the Mega Monarch",
	"Granmarg the Mega Monarch",
	"Seleglare the Luminous Lunar Dragon",
	"High Priestess of Prophecy",
	"Fool of Prophecy",
	"Temperance of Prophecy",
	"Hierophant of Prophecy",
	"Spellbook Library of the Crescent",
	"Spellbook of the Master",
	"Spellbook of Eternity",
	"Spellbook of Fate",
	"Spellbook Star Hall",
	"Spellbook of Life",
	"The Grand Spellbook Tower",
	"Shiranui Spectralsword Shade",
	"Jet Synchron",
	"Whitebeard, the Plunder Patroll Helm",
	"Redbeard, the Plunder Patroll Matey",
	"Plunder Patroll Shipyarrrd",
	"Plunder Patroll Booty",
	"Ancient Warriors - Ambitious Cao De",
	"Ancient Warriors - Rebellious Lu Feng",
	"Ancient Warriors - Valiant Zhang De",
	"Ancient Warriors - Masterful Sun Mou",
	"Ancient Warriors - Graceful Zhou Gong",
	"Ancient Warriors - Virtuous Liu Xuan",
	"Ancient Warriors - Ingenious Zhuge Kong",
	"Ancient Warriors - Eccentric Lu Jing",
	"Ancient Warriors Saga - Three Visits",
	"Ancient Warriors Saga - Sun-Liu Alliance",
	"Ancient Warriors Saga - Defense of Changban",
	"War Rock Bashileos",
	"War Rock Meteoragon",
	"War Rock Gactos",
	"War Rock Wento",
	"War Rock Fortia",
	"War Rock Dignity",
	"War Rock Spirit",
	"Mecha Phantom Beast Kalgriffin",
	"Mecha Phantom Beast Aerosguin",
	"Mecha Phantom Beast Blue Impala",
	"Mecha Phantom Beast Turtletracer",
	"Mecha Phantom Beast Warbluran",
	"Mecha Phantom Beast O-Lion",
	"Mecha Phantom Beast Concoruda",
	"Scramble!! Scramble!!",
	"Do a Barrel Roll",
	"Noble Knight Artorigus",
	"Ignoble Knight of Black Laundsallyn",
	"Noble Knight Eachtar",
	"Noble Knight Pellinore",
	"Noble Knight Gawayn",
	"Noble Knight Peredur",
	"Noble Knight Drystan",
	"Noble Knight Iyvanne",
	"Noble Knight Medraut",
	"Noble Knight Borz",
	"Noble Knight Bedwyr",
	"Noble Knight Gwalchavad",
	"Noble Knight Brothers",
	"Noble Knight Custennin",
	"Noble Knight's Shield-Bearer",
	"Merlin",
	"Horse of the Floral Knights",
	"Noble Knight's Spearholder",
	"Gwenhwyfar, Queen of Noble Arms",
	"Infernoble Knight - Roland",
	"Lady of the Lake",
	"Ignoble Knight of High Laundsallyn",
	"Sacred Noble Knight of King Artorigus",
	"Artorigus, King of the Noble Knights",
	"Sacred Noble Knight of King Custennin",
	"Heritage of the Chalice",
	"Last Chapter of the Noble Knights",
	"Glory of the Noble Knights",
	"Noble Arms of Destiny",
	"Noble Arms - Excaliburn",
	"Noble Knights of the Round Table",
	"Avalon",
	"\"Infernoble Arms - Durendal\"",
	"\"Infernoble Arms - Joyeuse\"",
	"Vector Pendulum, the Dracoverlord",
	"Reflection of Endymion",
	"Supreme King Gate Zero",
	"Supreme King Gate Infinity",
	"Oafdragon Magician",
	"Dinomist Rex",
	"Performapal Dag Daggerman",
	"Lector Pendulum, the Dracoverlord",
	"Luster Pendulum, the Dracoslayer",
	"Dinomist Pteran",
	"Performapal Gentrude",
	"Performapal Celestial Magician",
	"Purple Poison Magician",
	"Performapal Parrotrio",
	"Pendulumucho",
	"Tuning Magician",
	"Koa'ki Meiru Crusader",
	"Mecha Phantom Beast Megaraptor",
	"Laval Judgment Lord",
	"Laval Warrior",
	"Laval Archer",
	"Laval Miller",
	"Laval Coatl",
	"Soaring Eagle Above the Searing Land",
	"Laval Stennon",
	"Lavalval Salamander",
	"Laval the Greater",
	"Lavalval Dragon",
	"Lavalval Ignis",
	"Vylon Hept",
	"Vylon Stigma",
	"Vylon Charger",
	"Vylon Cube",
	"Vylon Sphere",
	"Vylon Omega",
	"Vylon Alpha",
	"Vylon Epsilon",
	"Vylon Sigma",
	"Vylon Delta",
	"Vylon Disigma",
	"Vylon Polytope",
	"Vylon Material",
	"Gem-Knight Crystal",
	"Gem-Knight Alexandrite",
	"Gem-Knight Emerald",
	"Gem-Armadillo",
	"Gem-Knight Lady Brilliant Diamond",
	"Gem-Knight Zirconia",
	"Gem-Knight Prismaura",
	"Gem-Knight Citrine",
	"Gem-Knight Ruby",
	"Gem-Knight Topaz",
	"Gem-Knight Aquamarine",
	"Gem-Knight Phantom Quartz",
	"Absorb Fusion",
	"Gem-Enhancement",
	"Zuijin of the Ice Barrier",
	"Winds Over the Ice Barrier",
	"Brionac, Dragon of the Ice Barrier",
	"Gungnir, Dragon of the Ice Barrier",
	"Dewloren, Tiger King of the Ice Barrier",
	"Jurrac Titano",
	"Jurrac Herra",
	"Jurrac Velo",
	"Jurrac Iguanon",
	"Jurrac Meteor",
	"Jurrac Giganoto",
	"Jurrac Velphito",
	"Naturia Eggplant",
	"Naturia Cherries",
	"Naturia Gaiastrio",
	"Landoise's Luminous Moss",
	"Naturia Sacred Tree",
	"Genex Solar",
	"Genex Army",
	"Genex Ally Reliever",
	"Genex Furnace",
	"R-Genex Ultimum",
	"Genex Ally Bellflame",
	"Genex Ally Powercell",
	"Genex Turbine",
	"Genex Ally Remote",
	"R-Genex Overseer",
	"Locomotion R-Genex",
	"Genex Ally Axel",
	"Thermal Genex",
	"Vindikite R-Genex",
	"Genex Ally Triforce",
	"Windmill Genex",
	"Genex Ally Triarm",
	"Hydro Genex",
	"Geo Genex",
	"Steelswarm Hercules",
	"Steelswarm Longhorn",
	"Steelswarm Caucastag",
	"Steelswarm Girastag",
	"Steelswarm Moth",
	"Steelswarm Sting",
	"Steelswarm Caller",
	"Steelswarm Scout",
	"Steelswarm Origin",
	"Infestation Wave"
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
	"Gladiator Beast Tamer Editor", 
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
	"Gladiator Beast Essedarii",
	"Sky Cavalry Centaurea",
	"Psychic Wheeleder",
	"SPYRAL Super Agent",
	"SPYRAL Tough",
	"SPYRAL Resort",
	"SPYGAL Misty",
	"SPYRAL GEAR - Big Red",
	"SPYRAL MISSION - Assault",
	"SPYRAL GEAR - Utility Wire",
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
	"Brotherhood of the Fire Fist - Rooster",
	"Brotherhood of the Fire Fist - Gorilla",
	"Brotherhood of the Fire Fist - Dragon",
	"Brotherhood of the Fire Fist - Kirin",
	"Brotherhood of the Fire Fist - Cardinal",
	"Brotherhood of the Fire Fist - Tiger King",
	"Brotherhood of the Fire Fist - Lion Emperor",
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
	outfile.write("Please note if a card is not here, it is subject to normal Common Charity legality\n\n")
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
	outfile.write("\n\n###### [Back home](index)")

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