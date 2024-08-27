from object import Object

# Global armor data dictionary
items_data['armor'] = {}

class Armor(Object):
    """Represents an armor item in the game."""

    def __init__(self, name, description, ac_base, dexterity_cap=None, strength_requirement=None, stealth_disadvantage=False, magical_properties=None):
        super().__init__(name, description, "armor", True)  # Armor is equippable
        self.slot = "armor"  # All armor goes in the "armor" slot
        self.ac_base = ac_base
        self.dexterity_cap = dexterity_cap
        self.strength_requirement = strength_requirement
        self.stealth_disadvantage = stealth_disadvantage
        self.magical_properties = magical_properties or []

    def get_ac(self, character):
        """Calculates the armor's actual AC based on the character's stats."""
        dex_modifier = character.get_ability_modifier("dexterity")
        if self.dexterity_cap:
            dex_modifier = min(dex_modifier, self.dexterity_cap)
        return self.ac_base + dex_modifier

    def can_equip(self, character):
        """Checks if the character meets the requirements to equip this armor."""
        if self.strength_requirement and character.get_ability_score("strength") < self.strength_requirement:
            return False
        return True

    def equip(self, character):
        """Equips the armor to the character, replacing any existing armor."""
        if not self.can_equip(character):
            print(f"You are not strong enough to wear the {self.name}.")
            return

        if character.equipped_armor:
            character.unequip_armor()

        character.equipped_armor = self
        print(f"You equipped the {self.name}.")

    def unequip(self, character):
        """Unequips the armor from the character."""
        if character.equipped_armor == self:
            character.equipped_armor = None
            print(f"You unequipped the {self.name}.")

# Define armor types
items_data['armor'].update({
    "Padded": {
        'name': "Padded Armor",
        'description': "Thick layers of quilted cloth offer minimal protection but ample comfort for long journeys.",
        'ac_base': 11,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': False
    },
    "Leather": {
        'name': "Leather Armor",
        'description': "Cured leather provides decent protection without hindering movement too much.",
        'ac_base': 11 + 2,  # Example of adding a bonus to the base AC
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': False
    },
    "Studded Leather": {
        'name': "Studded Leather Armor",
        'description': "Leather armor reinforced with metal studs, offering improved protection.",
        'ac_base': 12 + 2,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': False
    },
    "Hide": {
        'name': "Hide Armor",
        'description': "Toughened animal hides provide reliable protection, though somewhat restrictive.",
        'ac_base': 12,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': True
    },
    "Chain Shirt": {
        'name': "Chain Shirt",
        'description': "A shirt of interlocking metal rings, offering good protection with moderate mobility.",
        'ac_base': 13 + 2,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': True
    },
    "Scale Mail": {
        'name': "Scale Mail",
        'description': "Overlapping metal scales sewn onto leather, providing solid defense but limiting agility.",
        'ac_base': 14 + 2,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': True
    },
    "Breastplate": {
        'name': "Breastplate",
        'description': "A fitted metal chest plate, offering substantial protection without sacrificing too much mobility.",
        'ac_base': 14 + 2,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': True
    },
    "Half Plate": {
        'name': "Half Plate",
        'description': "Metal plates covering the torso and upper legs, providing excellent protection but hindering movement.",
        'ac_base': 15 + 2,
        'dexterity_cap': 0,  # No dexterity bonus beyond base AC
        'strength_requirement': 15,
        'stealth_disadvantage': True
    },
    "Full Plate": {
        'name': "Full Plate",
        'description': "A complete suit of articulated metal plates, offering the utmost protection at the cost of agility.",
        'ac_base': 18,
        'dexterity_cap': 0,
        'strength_requirement': 15,
        'stealth_disadvantage': True
    },
    "Elven Chain": {  # Example of a magical armor
        'name': "Elven Chain",
        'description': "Finely crafted elven chainmail, imbued with magic to enhance agility and stealth.",
        'ac_base': 13 + 2,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': False,  # No stealth disadvantage
        'magical_properties': ["Enhanced Agility"]  # Example magical property
    },
    "Mithril Breastplate": {  # Another example of magical armor
        'name': "Mithril Breastplate",
        'description': "A lightweight breastplate forged from rare mithril, offering exceptional protection and freedom of movement.",
        'ac_base': 16,
        'dexterity_cap': None,
        'strength_requirement': None,
        'stealth_disadvantage': False,
        'magical_properties': ["Mithril Resilience"]
    }
})

# Function to create an Armor object from data
def armor_from_data(armor_data):
    """Creates an Armor object from the provided data."""
    return Armor(
        armor_data['name'],
        armor_data['description'],
        armor_data['ac_base'],
        armor_data.get('dexterity_cap'),
        armor_data.get('strength_requirement'),
        armor_data.get('stealth_disadvantage', False),
        armor_data.get('magical_properties')
    )