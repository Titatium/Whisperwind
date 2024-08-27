import random
import json
import os

from combat import Character
from utils import roll_dice
from items import items_data
from skills import skills_data
from quests import Quest


class Player(Character):
    def __init__(self, name, race, char_class, background, strength, dexterity, constitution,
                 intelligence, wisdom, charisma, level=1, xp=0, hp=None, armor_class=10,
                 inventory=None, skills=None, equipment=None, gold=0, location=None,
                 active_quest=None, completed_quests=None, abilities=None):
        super().__init__(name, race, char_class, background, strength, dexterity, constitution,
                         intelligence, wisdom, charisma, level, xp, hp, armor_class,
                         inventory or {}, skills or [], equipment or {}, gold, location)

        self.active_quest = active_quest
        self.completed_quests = completed_quests or []
        self.abilities = abilities or []  # Special abilities based on class or race
        self.known_spells = []  # Spells the player can cast
        self.spell_slots = {}  # Spell slots per level, e.g., {1: 2} for two 1st-level slots
        self.equipped_weapon = None
        self.equipped_armor = None

    def to_json(self):
        """Converts the player object to a JSON-serializable dictionary."""
        return {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "background": self.background,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "level": self.level,
            "xp": self.xp,
            "max_hp": self.max_hp,
            "current_hp": self.current_hp,
            "armor_class": self.armor_class,
            "inventory": {name: item.to_json() for name, item in self.inventory.items()},
            "skills": self.skills,
            "equipment": {slot: item.to_json() for slot, item in self.equipment.items()},
            "gold": self.gold,
            "location": self.location.to_json() if self.location else None,
            "active_quest": self.active_quest.to_json() if self.active_quest else None,
            "completed_quests": self.completed_quests,
            "abilities": [ability.to_json() for ability in self.abilities],
            "known_spells": self.known_spells,
            "spell_slots": self.spell_slots,
            "equipped_weapon": self.equipped_weapon.name if self.equipped_weapon else None,
            "equipped_armor": self.equipped_armor.name if self.equipped_armor else None
        }

    @classmethod
    def from_json(cls, data):
        """Creates a Player instance from a JSON-serializable dictionary."""
        # Load basic attributes
        player = cls(
            data["name"],
            data["race"],
            data["class"],
            data["background"],
            data["strength"],
            data["dexterity"],
            data["constitution"],
            data["intelligence"],
            data["wisdom"],
            data["charisma"],
            level=data["level"],
            xp=data["xp"],
            hp=data["max_hp"],  # Load max_hp, current_hp will be set to max_hp later
            armor_class=data["armor_class"],
            gold=data["gold"],
            # Location will be loaded later based on location data
            active_quest=Quest.from_json(data["active_quest"]) if data["active_quest"] else None,
            completed_quests=data["completed_quests"],
            # Abilities will be loaded later based on class and race data
            known_spells=data["known_spells"],
            spell_slots=data["spell_slots"]
        )

        # Load inventory
        from object import Object
        player.inventory = {name: Object.from_json(item_data) for name, item_data in data["inventory"].items()}

        # Load equipment (assuming equipment items are also Objects)
        player.equipment = {slot: Object.from_json(item_data) for slot, item_data in data["equipment"].items()}

        # Set current HP to max HP after loading
        player.current_hp = player.max_hp

        # Load equipped weapon and armor (assuming they are in inventory/equipment)
        if data["equipped_weapon"]:
            player.equipped_weapon = player.inventory.get(data["equipped_weapon"])
            if not player.equipped_weapon:
                player.equipped_weapon = player.equipment.get(data["equipped_weapon"])
        if data["equipped_armor"]:
            player.equipped_armor = player.inventory.get(data["equipped_armor"])
            if not player.equipped_armor:
                player.equipped_armor = player.equipment.get(data["equipped_armor"])

        # Load abilities based on class and race data (implementation depends on your data structure)
        # ...

        # Load location based on location data (implementation depends on your data structure)
        # ...

        return player

    def attack(self, monster):
        """Performs an attack against a monster."""
        # Weapon attack or unarmed strike
        if self.equipped_weapon:
            weapon_damage = roll_dice(*self.equipped_weapon.damage)
            print(f"You attack the {monster.name} with your {self.equipped_weapon.name}, hitting for {weapon_damage} damage!")
            monster.take_damage(weapon_damage)
        else:
            unarmed_damage = roll_dice(1, 4) + self.strength_modifier
            print(f"You punch the {monster.name}, hitting for {unarmed_damage} damage!")
            monster.take_damage(unarmed_damage)

    def flee(self, monster):
        """Attempts to flee from combat."""
        from world import attempt_flee
        if attempt_flee(self, monster):
            print(f"You successfully flee from the {monster.name}!")
        else:
            print(f"You failed to flee! The {monster.name} attacks!")
            monster.attack(self)

    def rest(self):
        """Rests to regain health and potentially other resources."""
        if self.current_hp < self.max_hp:
            heal_amount = roll_dice(1, 8) + self.constitution_modifier  # Example healing
            self.heal(heal_amount)
            print(f"You rest and regain {heal_amount} hit points.")
        else:
            print("You are already at full health.")

        # Potentially regain spell slots or other class-specific resources
        # ...

    def level_up(self):
        """Handles the character leveling up."""
        self.level += 1
        # Increase max HP, potentially gain new abilities or spell slots, etc.
        # ...
        print(f"You've reached level {self.level}!")

    def gain_skill_proficiency(self, skill_name):
        """Adds a skill to the player's list of proficiencies."""
        if skill_name not in self.skills:
            self.skills.append(skill_name)
            print(f"You've gained proficiency in {skill_name}!")

    def get_skill_modifier(self, skill_name):
        """Calculates the modifier for a given skill, including proficiency bonus."""
        if skill_name in self.skills:
            proficiency_bonus = (self.level - 1) // 4 + 2  # Example proficiency bonus calculation
        else:
            proficiency_bonus = 0

        ability_modifier = getattr(self, skills_data[skill_name]["ability_modifier"])
        return ability_modifier + proficiency_bonus

    def print_inventory(self):
        """Prints the player's inventory in a formatted way