class CharacterClass:
    def __init__(self, name, hit_die, primary_abilities, weapon_proficiencies, armor_proficiencies=None, tool_proficiencies=None, saving_throw_proficiencies=None, skill_choices=None, starting_equipment=None, special_abilities=None):
        self.name = name
        self.hit_die = hit_die
        self.primary_abilities = primary_abilities
        self.weapon_proficiencies = weapon_proficiencies
        self.armor_proficiencies = armor_proficiencies or []
        self.tool_proficiencies = tool_proficiencies or []
        self.saving_throw_proficiencies = saving_throw_proficiencies or []
        self.skill_choices = skill_choices or []
        self.starting_equipment = starting_equipment or []
        self.special_abilities = special_abilities or []  # New attribute for special abilities

# Warrior
warrior = CharacterClass(
    "Warrior",
    10,  # d10 hit die
    ["Strength", "Constitution"],
    ["Simple", "Martial"],
    armor_proficiencies=["Light", "Medium", "Heavy", "Shields"],
    special_abilities=[
        {"name": "Second Wind", "description": "Regain hit points equal to 1d10 + your warrior level."},
        {"name": "Action Surge", "description": "Take an additional action on your turn."}
    ]
)

# Mage
mage = CharacterClass(
    "Mage",
    6,  # d6 hit die
    ["Intelligence", "Wisdom"],
    ["Simple"],
    saving_throw_proficiencies=["Intelligence", "Wisdom"],
    special_abilities=[
        {"name": "Spellcasting", "description": "Cast arcane spells using your Intelligence modifier."},
        {"name": "Arcane Recovery", "description": "Regain a number of spell slots after a short rest."}
    ]
)

# Rogue
rogue = CharacterClass(
    "Rogue",
    8,  # d8 hit die
    ["Dexterity", "Charisma"],
    ["Simple", "Thieves' Tools"],
    armor_proficiencies=["Light"],
    special_abilities=[
        {"name": "Sneak Attack", "description": "Deal extra damage when you have advantage on an attack."},
        {"name": "Cunning Action", "description": "Use a bonus action to Dash, Disengage, or Hide."}
    ]
)

# Ranger (Mentioned in whisperwindstory.txt)
ranger = CharacterClass(
    "Ranger",
    10,  # d10 hit die
    ["Dexterity", "Wisdom"],
    ["Simple", "Martial"],
    armor_proficiencies=["Light", "Medium", "Shields"],
    special_abilities=[
        {"name": "Favored Enemy", "description": "Gain advantage on attacks against a chosen type of creature."},
        {"name": "Natural Explorer", "description": "Navigate and survive in the wilderness with ease."}
    ]
)

# Paladin (Mentioned in whisperwindstory.txt)
paladin = CharacterClass(
    "Paladin",
    10,  # d10 hit die
    ["Strength", "Charisma"],
    ["Simple", "Martial"],
    armor_proficiencies=["Light", "Medium", "Heavy", "Shields"],
    special_abilities=[
        {"name": "Divine Smite", "description": "Expend a spell slot to deal extra radiant damage."},
        {"name": "Lay on Hands", "description": "Heal yourself or others using your pool of healing power."}
    ]
)

# Create the list of available classes
available_classes = [warrior, mage, rogue, ranger, paladin]