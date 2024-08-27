import random

from utils import roll_dice
from items import items_data  # Assuming you have items defined in items.py or a similar file

class Monster:
    """Represents a monster in the game."""

    def __init__(self, name, hp, ac, strength, dexterity, constitution, 
                 intelligence, wisdom, charisma, xp, attacks, description, 
                 vulnerabilities=None, resistances=None, immunities=None,
                 loot_table=None, armor=None, weapons=None):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.xp = xp
        self.attacks = attacks
        self.description = description
        self.vulnerabilities = vulnerabilities or []
        self.resistances = resistances or []
        self.immunities = immunities or []
        self.loot_table = loot_table or []  # List of possible loot drops
        self.armor = armor  # Optional armor item
        self.weapons = weapons or []  # List of equipped weapons

    @classmethod
    def from_data(cls, monster_data):
        """Creates a Monster instance from a dictionary of monster data."""
        return cls(**monster_data)

    def is_alive(self):
        """Checks if the monster is still alive."""
        return self.current_hp > 0

    def take_damage(self, damage, damage_type):
        """Applies damage to the monster, considering vulnerabilities, resistances, and immunities.

        Args:
            damage: The amount of damage to inflict.
            damage_type: The type of damage (e.g., "fire", "piercing").
        """
        if damage_type in self.immunities:
            print(f"The {self.name} is immune to {damage_type} damage!")
            return

        if damage_type in self.resistances:
            damage //= 2
            print(f"The {self.name} resists the {damage_type} damage!")

        if damage_type in self.vulnerabilities:
            damage *= 2
            print(f"The {self.name} is vulnerable to {damage_type} damage!")

        # Consider armor protection
        if self.armor:
            damage -= self.armor.armor_class
            if damage < 0:
                damage = 0

        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            print(f"The {self.name} has been defeated!")

    def attack(self, target):
        """Performs an attack on the target.

        Args:
            target: The Character object being attacked.
        """
        # Choose a random attack or a specific one based on strategy (optional)
        attack = random.choice(self.attacks)
        
        # If the monster has weapons, use them for the attack
        if self.weapons:
            weapon = random.choice(self.weapons)
            attack_roll = roll_dice(1, 20) + self.get_modifier(attack["modifier"]) + weapon.attack_bonus
            damage_roll = roll_dice(*weapon.damage) + self.get_modifier(weapon.damage_modifier)
            damage_type = weapon.damage_type
        else:  # Use the monster's natural attack
            attack_roll = roll_dice(1, 20) + self.get_modifier(attack["modifier"])
            damage_roll = roll_dice(*attack["damage"])
            damage_type = attack["damage_type"]

        if attack_roll >= target.ac:
            target.take_damage(damage_roll, damage_type)
            print(f"The {self.name} {attack['verb']} {target.name} for {damage_roll} {damage_type} damage!")
        else:
            print(f"The {self.name}'s attack misses {target.name}!")

    def get_modifier(self, ability):
        """Gets the ability modifier for the given ability score.

        Args:
            ability: The ability score ("strength", "dexterity", etc.).

        Returns:
            The corresponding ability modifier.
        """
        return (getattr(self, ability) - 10) // 2

    def get_loot(self):
        """Generates loot dropped by the monster based on its loot table.

        Returns:
            A list of Item objects representing the dropped loot.
        """
        loot = []
        for item_name, drop_chance in self.loot_table.items():
            if random.random() < drop_chance:
                loot.append(Item.from_data(items_data[item_name]))
        return loot

# Example Monster Data (Expand this with more monsters)

monster_data = {
    "Goblin": {
        "name": "Goblin",
        "hp": 7,
        "ac": 15,
        "strength": 8,
        "dexterity": 14,
        "constitution": 10,
        "intelligence": 10,
        "wisdom": 8,
        "charisma": 8,
        "xp": 50,
        "attacks": [
            {"name": "Scimitar", "verb": "slashes at", "modifier": "dexterity", "damage": (1, 6), "damage_type": "slashing"},
            {"name": "Shortbow", "verb": "shoots an arrow at", "modifier": "dexterity", "damage": (1, 6), "damage_type": "piercing"}
        ],
        "description": "A small, green-skinned creature with sharp teeth and a mischievous grin. It wears ragged leather armor and carries a rusty scimitar.",
        "loot_table": {
            "Copper Pieces": 0.8,  # 80% chance to drop 1-6 copper pieces
            "Dagger": 0.2         # 20% chance to drop a dagger
        }
    },
    "Dire Wolf": {
        "name": "Dire Wolf",
        "hp": 37,
        "ac": 14,
        "strength": 17,
        "dexterity": 15,
        "constitution": 15,
        "intelligence": 3,
        "wisdom": 12,
        "charisma": 6,
        "xp": 200,
        "attacks": [
            {"name": "Bite", "verb": "bites", "modifier": "strength", "damage": (2, 6), "damage_type": "piercing"}
        ],
        "description": "A massive wolf with glowing red eyes and a powerful build. Its fur is matted and stained with blood.",
        "loot_table": {
            "Wolf Pelt": 0.5,
            "Silver Pieces": 0.3, 
            "Health Potion": 0.1
        }
    },
    "Kobold": {
        "name": "Kobold",
        "hp": 5,
        "ac": 12,
        "strength": 7,
        "dexterity": 15,
        "constitution": 9,
        "intelligence": 8,
        "wisdom": 7,
        "charisma": 8,
        "xp": 25,
        "attacks": [
            {"name": "Dagger", "verb": "stabs at", "modifier": "dexterity", "damage": (1, 4), "damage_type": "piercing"},
            {"name": "Sling", "verb": "hurls a stone at", "modifier": "dexterity", "damage": (1, 4), "damage_type": "bludgeoning"}
        ],
        "description": "A small, reptilian humanoid with scaly skin and glowing red eyes. It clutches a rusty dagger and a sling.",
        "loot_table": {
            "Copper Pieces": 0.9,  # 90% chance to drop 1-3 copper pieces
            "Sling Bullet": 0.3    # 30% chance to drop sling bullets
        }
    },
    "Pixie": {
        "name": "Pixie",
        "hp": 1,
        "ac": 15,
        "strength": 2,
        "dexterity": 15,
        "constitution": 8,
        "intelligence": 10,
        "wisdom": 10,
        "charisma": 13,
        "xp": 10,
        "attacks": [
            {"name": "Illusion", "verb": "casts an illusion on", "modifier": "intelligence", "damage": (0, 0), "damage_type": "psychic"}  # Non-damaging, potentially disorienting
        ],
        "description": "A tiny, winged humanoid with shimmering wings and mischievous eyes. It flits about playfully, leaving trails of sparkling dust.",
        "loot_table": {
            "Pixie Dust": 0.1
        }
    },
    "Dryad": {
        "name": "Dryad",
        "hp": 22,
        "ac": 11,
        "strength": 10,
        "dexterity": 12,
        "constitution": 14,
        "intelligence": 12,
        "wisdom": 15,
        "charisma": 14,
        "xp": 75,
        "attacks": [
            {"name": "Club", "verb": "strikes with a club", "modifier": "strength", "damage": (1, 6), "damage_type": "bludgeoning"},
            {"name": "Entangle", "verb": "casts Entangle on", "modifier": "wisdom", "damage": (0, 0), "damage_type": "none"}  # Restricting movement
        ],
        "description": "A beautiful humanoid with bark-like skin and leafy hair. She is deeply connected to the forest and fiercely protective of its inhabitants.",
        "loot_table": {
            "Acorn of Farsight": 0.05,  # Rare drop
            "Healing Herbs": 0.3
        }
    },
    "Bugbear": {
        "name": "Bugbear",
        "hp": 27,
        "ac": 16,
        "strength": 15,
        "dexterity": 14,
        "constitution": 13,
        "intelligence": 8,
        "wisdom": 11,
        "charisma": 9,
        "xp": 125,
        "attacks": [
            {"name": "Morningstar", "verb": "swings a morningstar at", "modifier": "strength", "damage": (1, 8), "damage_type": "piercing"},
            {"name": "Surprise Attack", "verb": "ambushes", "modifier": "dexterity", "damage": (2, 6), "damage_type": "piercing"}  # Higher damage if the target hasn't acted yet
        ],
        "description": "A hulking, goblinoid creature with shaggy fur and a cruel expression. It wields a heavy morningstar and enjoys surprising its prey.",
        "loot_table": {
            "Silver Pieces": 0.6, 
            "Morningstar": 0.15
        }
    },
    "Owlbear": {
        "name": "Owlbear",
        "hp": 59,
        "ac": 13,
        "strength": 20,
        "dexterity": 12,
        "constitution": 17,
        "intelligence": 3,
        "wisdom": 12,
        "charisma": 7,
        "xp": 450,
        "attacks": [
            {"name": "Claws", "verb": "rakes with its claws", "modifier": "strength", "damage": (2, 8), "damage_type": "slashing"},
            {"name": "Bite", "verb": "bites", "modifier": "strength", "damage": (1, 10), "damage_type": "piercing"}
        ],
        "description": "A fearsome creature with the head of an owl and the body of a bear. Its powerful claws and beak are capable of inflicting devastating wounds.",
        "loot_table": {
            "Owlbear Hide": 0.4,
            "Gold Pieces": 0.2,
            "Potion of Greater Healing": 0.05  # Very rare drop
        }
    },
    # ... Add more monster data here ...
}