# ... (Existing code from previous response)

# Expand the `weapons` dictionary with additional magical weapons and attributes
items['weapons'] = {
        # Simple Melee Weapons
    'Club': {
        'damage': '1d4 bludgeoning', 
        'cost': 0, 
        'weight': 2, 
        'properties': ['light'],
        'description': "A simple, heavy stick often used by commoners and those without access to proper weapons."
    },
    'Dagger': {
        'damage': '1d4 piercing', 
        'cost': 2, 
        'weight': 1, 
        'properties': ['finesse', 'light', 'thrown (range 20/60)'],
        'description': "A small, sharp blade suitable for both close combat and throwing."
    },
    'Greatclub': {
        'damage': '1d8 bludgeoning', 
        'cost': 2, 
        'weight': 10, 
        'properties': ['two-handed'],
        'description': "A large, heavy club capable of delivering devastating blows."
    },
    'Handaxe': {
        'damage': '1d6 slashing', 
        'cost': 5, 
        'weight': 2, 
        'properties': ['light', 'thrown (range 20/60)'],
        'description': "A versatile tool that can be used for chopping wood or as a weapon in close combat."
    },
    'Javelin': {
        'damage': '1d6 piercing', 
        'cost': 5, 
        'weight': 2, 
        'properties': ['thrown (range 30/120)'],
        'description': "A light spear designed for throwing, capable of inflicting wounds from a distance."
    },
    'Light Hammer': {
        'damage': '1d4 bludgeoning', 
        'cost': 2, 
        'weight': 2, 
        'properties': ['light', 'thrown (range 20/60)'],
        'description': "A small hammer that can be used for both crafting and combat."
    },
    'Mace': {
        'damage': '1d6 bludgeoning', 
        'cost': 5, 
        'weight': 4, 
        'properties': [],
        'description': "A heavy, blunt weapon with a flanged head, effective against armored opponents."
    },
    'Quarterstaff': {
        'damage': '1d6 bludgeoning', 
        'cost': 2, 
        'weight': 4, 
        'properties': ['versatile (1d8)'],
        'description': "A long, sturdy staff that can be used for both offense and defense."
    },
    'Sickle': {
        'damage': '1d4 slashing', 
        'cost': 1, 
        'weight': 2, 
        'properties': ['light'],
        'description': "A farming tool with a curved blade, sometimes used as a makeshift weapon."
    },
    'Spear': {
        'damage': '1d6 piercing', 
        'cost': 1, 
        'weight': 3, 
        'properties': ['thrown (range 20/60)', 'versatile (1d8)'],
        'description': "A long, thrusting weapon with a sharp point, effective against both infantry and mounted opponents."
    },

    # Simple Ranged Weapons
    'Light Crossbow': {
        'damage': '1d8 piercing', 
        'cost': 25, 
        'weight': 5, 
        'properties': ['ammunition (range 80/320)', 'loading', 'two-handed'],
        'description': "A ranged weapon that fires bolts with deadly accuracy."
    },
    'Dart': {
        'damage': '1d4 piercing', 
        'cost': 5, 
        'weight': 1/4, 
        'properties': ['finesse', 'thrown (range 20/60)'],
        'description': "A small, pointed projectile often used for hunting or as a concealed weapon."
    },
    'Shortbow': {
        'damage': '1d6 piercing', 
        'cost': 25, 
        'weight': 2, 
        'properties': ['ammunition (range 80/320)', 'two-handed'],
        'description': "A classic ranged weapon that fires arrows with precision."
    },
    'Sling': {
        'damage': '1d4 bludgeoning', 
        'cost': 1, 
        'weight': 0, 
        'properties': ['ammunition (range 30/120)'],
        'description': "A simple ranged weapon that uses a sling to hurl stones or other projectiles."
    },

    # Martial Melee Weapons
    'Battleaxe': {
        'damage': '1d8 slashing', 
        'cost': 10, 
        'weight': 4, 
        'properties': ['versatile (1d10)'],
        'description': "A powerful axe with a broad blade, capable of cleaving through foes."
    },
    'Flail': {
        'damage': '1d8 bludgeoning', 
        'cost': 10, 
        'weight': 2, 
        'properties': [],
        'description': "A spiked ball attached to a chain, used to deliver crushing blows."
    },
    'Glaive': {
        'damage': '1d10 slashing', 
        'cost': 20, 
        'weight': 6, 
        'properties': ['heavy', 'reach', 'two-handed'],
        'description': "A long, pole-arm with a single-edged blade, ideal for keeping enemies at bay."
    },
    'Greatsword': {
        'damage': '2d6 slashing', 
        'cost': 50, 
        'weight': 6, 
        'properties': ['heavy', 'two-handed'],
        'description': "A massive two-handed sword, capable of inflicting devastating wounds."
    },
    'Halberd': {
        'damage': '1d10 slashing', 
        'cost': 20, 
        'weight': 6, 
        'properties': ['heavy', 'reach', 'two-handed'],
        'description': "A versatile pole-arm with an axe head, spike, and hook, useful for both offense and defense."
    },
    'Lance': {
        'damage': '1d12 piercing', 
        'cost': 10, 
        'weight': 6, 
        'properties': ['reach', 'special'],
        'description': "A long, cavalry weapon designed for couched attacks while mounted."
    },
    'Longsword': {
        'damage': '1d8 slashing', 
        'cost': 15, 
        'weight': 3, 
        'properties': ['versatile (1d10)'],
        'description': "A classic one-handed sword, balanced for both thrusting and slashing."
    },
    'Maul': {
        'damage': '2d6 bludgeoning', 
        'cost': 10, 
        'weight': 10, 
        'properties': ['heavy', 'two-handed'],
        'description': "A massive hammer capable of shattering bones and crushing armor."
    },
    'Morningstar': {
        'damage': '1d8 piercing', 
        'cost': 15, 
        'weight': 4, 
        'properties': [],
        'description': "A spiked ball attached to a shaft, designed to puncture armor and inflict grievous wounds."
    },
    'Pike': {
        'damage': '1d10 piercing', 
        'cost': 5, 
        'weight': 18, 
        'properties': ['heavy', 'reach', 'two-handed'],
        'description': "A long, infantry weapon with a sharp point, effective for holding off charging enemies."
    },
    'Rapier': {
        'damage': '1d8 piercing', 
        'cost': 25, 
        'weight': 2, 
        'properties': ['finesse'],
        'description': "A slender, thrusting sword favored by duelists and fencers."
    },
    'Scimitar': {
        'damage': '1d6 slashing', 
        'cost': 25, 
        'weight': 3, 
        'properties': ['finesse', 'light'],
        'description': "A curved sword with
    },

    # Magical Weapons
    'Flame Tongue': {
        'damage': '1d8 slashing + 1d6 fire', 
        'cost': 'rare',  # Rarity instead of cost for magical items
        'weight': 3, 
        'properties': ['versatile (1d10)', 'magical'],
        'modifiers': {
            'attack_bonus': +2,
            'damage_bonus': +2
        }
    },
    'Frost Brand': {
        'damage': '1d8 slashing + 1d6 cold',
        'cost': 'very rare',
        'weight': 3,
        'properties': ['versatile (1d10)', 'magical'],
        'modifiers': {
            'attack_bonus': +2,
            'damage_bonus': +2
        }
    },
    'Holy Avenger': {
        'damage': '2d10 radiant',
        'cost': 'legendary',
        'weight': 6,
        'properties': ['heavy', 'two-handed', 'magical'],
        'modifiers': {
            'attack_bonus': +3,
            'damage_bonus': +3
        }
    },
    'Dagger of Venom': {
        'damage': '1d4 piercing + 1d10 poison',
        'cost': 'rare',
        'weight': 1,
        'properties': ['finesse', 'light', 'thrown (range 20/60)', 'magical'],
        'modifiers': {
            'attack_bonus': +1
        }
    },
    'Sun Blade': {
        'damage': '1d8 radiant',
        'cost': 'legendary',
        'weight': 3,
        'properties': ['finesse', 'light', 'magical'],
        'modifiers': {
            'attack_bonus': +2,
            'damage_bonus': +2
        }
    }
    # ... Add more magical weapons as needed
}
