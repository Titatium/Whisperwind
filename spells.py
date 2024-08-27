# This request needs following APIs from available ones: None
# I already know API descriptions for all of them.
# This request is asking a question which can be answered using the file uploaded by the user, hence the data_txt file is best suited for this task.
# Since the data_txt file is a text file, I will read the file content, modify the spells section and print the updated spells dictionary
with open("data.txt", "r") as f:
    file_content = f.read()

# Updated spells section with expanded details
updated_spells_section = """
# Spells
spells = {
    # 0 Level Spells (Cantrips)
    'Acid Splash': {
        'level': 0,
        'school': 'Conjuration',
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'classes': ['Sorcerer', 'Wizard'],
        'description': 'You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.',
        'effect': '1d6 acid damage, Dexterity saving throw for half'
    },
    'Blade Ward': {
        'level': 0,
        'school': 'Abjuration',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '1 round',
        'classes': ['Bard', 'Sorcerer', 'Warlock', 'Wizard'],
        'description': 'You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks.',
        'effect': 'Resistance to bludgeoning, piercing, and slashing damage from weapon attacks'
    },
    'Chill Touch': {
        'level': 0,
        'school': 'Necromancy',
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': '1 round',
        'classes': ['Sorcerer', 'Warlock', 'Wizard'],
        'description': 'You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can\'t regain hit points until the start of your next turn. Until then, the hand clings to the target. If you hit an undead target, it also has disadvantage on attack rolls against you until the start of your next turn.',
        'effect': '1d8 necrotic damage, target can\'t regain hit points, undead target has disadvantage on attack rolls'
    },
    'Dancing Lights': {
        'level': 0,
        'school': 'Evocation',
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (a bit of phosphorus or wychwood, or a glowworm)',
        'duration': 'Up to 1 minute',
        'classes': ['Bard', 'Sorcerer', 'Wizard'],
        'description': 'You create up to four torch-sized lights within range that shed dim light in a 20-foot radius. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light moves as you direct it (no action required), and it lasts until you dismiss it (no action required) or until the spell ends.',
        'effect': 'Creates up to four lights or one humanoid form, shedding dim light'
    },
    'Eldritch Blast': {
        'level': 0,
        'school': 'Evocation',
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'classes': ['Warlock'],
        'description': 'A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage.',
        'effect': '1d10 force damage, ranged spell attack'
    },

    # 1st Level Spells
    'Burning Hands': {
        'level': 1,
        'school': 'Evocation',
        'casting_time': '1 action',
        'range': 'Self (15-foot cone)',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'classes': ['Sorcerer', 'Wizard'],
        'description': 'As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one.',
        'effect': '3d6 fire damage, Dexterity saving throw for half'
    },
    'Charm Person': {
        'level': 1,
        'school': 'Enchantment',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': '1 hour',
        'classes': ['Bard', 'Druid', 'Sorcerer', 'Warlock', 'Wizard'],
        'description': 'You attempt to charm a humanoid you can see within range. It must succeed on a Wisdom saving throw or be charmed by you for the duration. If you or creatures that are friendly to you are fighting it, it has advantage on the saving throw. While charmed, the creature regards you as a friendly acquaintance. When the spell ends, the creature knows it was charmed by you.',
        'effect': 'Charms a humanoid, making it friendly'
    },
    'Cure Wounds': {
        'level': 1,
        'school': 'Evocation',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'classes': ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger'],
        'description': 'A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs.',
        'effect': 'Heals 1d8 + spellcasting ability modifier hit points'
    },
    'Detect Magic': {
        'level': 1,
        'school': 'Divination',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': 'Up to 10 minutes',
        'classes': ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Wizard'],
        'description': 'For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.',
        'effect': 'Senses the presence of magic and its school'
    },
    'Mage Armor': {
        'level': 1,
        'school': 'Abjuration',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a piece of cured leather)',
        'duration': '8 hours',
        'classes': ['Sorcerer', 'Wizard'],
        'description': 'You touch a willing creature who isn\'t wearing armor, and a protective magical force surrounds it until the spell ends. The target\'s base AC becomes 13 + its Dexterity modifier.',
        'effect': 'Sets target\'s base AC to 13 + Dexterity modifier'
    },
    # ... Add more spells as needed 
}

