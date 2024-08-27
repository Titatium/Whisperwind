from classes import *
from spells import *
from items import *

# NPC Data Structure
npcs = {
    # Whisperwind Inhabitants
    "Lily Rootwhistle": {
        "name": "Lily Rootwhistle",
        "description": "A kind and knowledgeable herbalist with a deep connection to the Feywood.",
        "race": "Half-Elf",
        "class": Herbalist(),  # Assuming Herbalist is a subclass of Character
        "level": 5,
        "stats": {"strength": 10, "dexterity": 14, "constitution": 12, "intelligence": 16, "wisdom": 15, "charisma": 13},
        "inventory": [
            items_data["Healing Potion"],
            items_data["Moonpetal"],
            items_data["Glowcap"]
        ],
        "gold": 30,
        "spells": [spells_data["Cure Wounds"], spells_data["Entangle"]],
        "backstory": "Lily grew up on the edge of the Feywood, learning the secrets of herbs and potions from her grandmother. She has a deep respect for nature and the Fey, and often acts as a mediator between the townsfolk and the forest's inhabitants."
    },
    "Barkeep": {
        "name": "Barkeep (Edgar Thistlebrew)",
        "description": "A jovial and welcoming dwarf with a knack for pouring the perfect pint.",
        "race": "Dwarf",
        "class": Commoner(), 
        "level": 3,
        "stats": {"strength": 12, "dexterity": 10, "constitution": 16, "intelligence": 13, "wisdom": 11, "charisma": 14},
        "inventory": [
            items_data["Ale"],
            items_data["Mead"],
            items_data["Whiskey"]
        ],
        "gold": 50,
        "backstory": "Edgar inherited the Gilded Tankard from his father and has been running it ever since. He's a friendly face to all who enter, always ready with a joke or a listening ear. He's also a keen observer, and knows most of the gossip in town."
    },
    "Old Silas": {
        "name": "Old Silas (Silas Stockwell)",
        "description": "A gruff and enigmatic old human who runs a curious shop filled with oddities.",
        "race": "Human",
        "class": Merchant(), 
        "level": 4,
        "stats": {"strength": 11, "dexterity": 12, "constitution": 13, "intelligence": 15, "wisdom": 14, "charisma": 10},
        "inventory": [
            items_data["Mysterious Locket"],
            items_data["Dusty Tome"],
            items_data["Ornate Dagger"]
        ],
        "gold": 100,
        "backstory": "Silas has been running his shop, Silas' Sundries, for as long as anyone can remember. He's a shrewd bargainer and a collector of strange and unusual items. Some say he has a connection to the Feywild, but he's not one to share his secrets easily."
    },
    "Mayor Elden Rootwhistle": {
        "name": "Mayor Elden Rootwhistle",
        "description": "A wise and respected halfling leader, dedicated to the well-being of Whisperwind.",
        "race": "Halfling",
        "class": Noble(), 
        "level": 6,
        "stats": {"strength": 8, "dexterity": 13, "constitution": 14, "intelligence": 16, "wisdom": 17, "charisma": 12},
        "inventory": [
            items_data["Signet Ring"],
            items_data["Scroll of Protection"]
        ],
        "gold": 200,
        "backstory": "Elden has been the mayor of Whisperwind for many years, guiding the town through good times and bad. He's a fair and just leader, always putting the needs of his people first. He's also a skilled diplomat, maintaining peaceful relations with the Feywood and its inhabitants."
    },
    "Thorgren Stonebeard": {
        "name": "Thorgren Stonebeard",
        "description": "A burly and battle-scarred dwarf blacksmith, renowned for his craftsmanship.",
        "race": "Dwarf",
        "class": Blacksmith(),  
        "level": 7,
        "stats": {"strength": 18, "dexterity": 12, "constitution": 17, "intelligence": 10, "wisdom": 13, "charisma": 9},
        "inventory": [
            items_data["Iron Warhammer"],
            items_data["Steel Ingot"],
            items_data["Mithril Ore"]
        ],
        "gold": 80,
        "backstory": "Thorgren learned his trade from his father and grandfather, carrying on a long family tradition of blacksmithing. He's a master of his craft, able to forge weapons and armor of exceptional quality. He's also a staunch defender of Whisperwind, always ready to lend his strength in times of need."
    },
    # Add more NPCs from Whisperwind here

    # Feywood Inhabitants
    "Elara the Satyr": {
        "name": "Elara",
        "description": "A gentle and musical satyr with a love for nature and a playful spirit.",
        "race": "Satyr",
        "class": Bard(), 
        "level": 4,
        "stats": {"strength": 10, "dexterity": 15, "constitution": 12, "intelligence": 13, "wisdom": 14, "charisma": 16},
        "inventory": [
            items_data["Pan Flute"],
            items_data["Charm of Animal Friendship"]
        ],
        "gold": 15,
        "spells": [spells_data["Charm Person"], spells_data["Disguise Self"]],
        "backstory": "Elara roams the Feywood, playing her flute and enchanting the forest with her music. She's a friend to all creatures, and her melodies can soothe even the most troubled hearts. She's also fiercely protective of her home and will defend it from any who threaten its harmony."
    },
    "Oberon, the Archfey": {
        "name": "Oberon",
        "description": "The majestic and enigmatic ruler of the Feywood, a being of immense power and wisdom.",
        "race": "Fey",
        "class": Archfey(),  # Custom class for powerful Fey beings
        "level": 15,
        "stats": {"strength": 16, "dexterity": 20, "constitution": 18, "intelligence": 22, "wisdom": 20, "charisma": 24},
        "inventory": [
            items_data["Heartstone"],
            items_data["Moonstone Scepter"]
        ],
        "gold": 1000,
        "spells": [spells_data["Wish"], spells_data["Teleport"], spells_data["Shapechange"]],
        "backstory": "Oberon is the lord of the Feywood, a realm of dreams and magic. He is both benevolent and capricious, delighting in beauty and mischief. He watches over his domain with a careful eye, ensuring the balance between nature and the Fey is maintained."
    },
    "The Raven": {
        "name": "The Raven",
        "description": "A shadowy figure shrouded in mystery, their motives and true identity unknown.",
        "race": "Unknown",
        "class": Shadowcaster(),  # Custom class for a magic-user focused on shadows and illusions
        "level": 10,
        "stats": {"strength": 12, "dexterity": 18, "constitution": 14, "intelligence": 18, "wisdom": 16, "charisma": 12},
        "inventory": [],
        "gold": 500,
        "spells": [spells_data["Darkness"], spells_data["Invisibility"], spells_data["Phantasmal Force"]],
        "backstory": "The Raven is a newcomer to the Feywood, their arrival coinciding with the recent disturbances. They seem to be manipulating events from the shadows, their goals shrouded in secrecy. Some whisper that they seek to disrupt the balance of the Feywild and claim its power for their own."
    }
    # Add more Feywood inhabitants here (e.g., dryads, sprites, pixies, etc.)
}