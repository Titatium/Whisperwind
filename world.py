import random

from combat import initiate_combat
from data import monster_data, location_data

# ASCII Art Maps (Enhanced)

town_square_map = r"""
 ___________________
|                   |
|     Town Square   |
|        *          |
|    / | \          |
|   /  |  \         |
|  /   |   \        |
| /    |    \       |
|/_____|_____\      |
|  Inn  | Shop |     |
|_______|______|     |
|                   |
|___________________|
"""

feywood_forest_edge_map = r"""
 ___________________
|                   |
| Feywood Forest    |
|      ###          |
|     #####         |
|    #######        |
|   #########       |
|  ###########      |
| #############     |
|___________________|
"""

# ... (Add more maps for other locations as needed)

def generate_random_encounter(current_location):
    """Generates a random encounter based on the current location.

    Args:
        current_location: The Location object representing the player's current location.

    Returns:
        A Monster object if an encounter occurs, otherwise None.
    """

    # Location-Specific Encounters (Enhanced)
    if current_location.name == "Town Square":
        encounter_chance = 0.1  # Low chance in town
        possible_encounters = ["Goblin", "Kobold"] 
    elif current_location.name == "Feywood Forest Edge":
        encounter_chance = 0.5  # Higher chance in the forest
        possible_encounters = ["Wolf", "Pixie", "Dryad"]  # More diverse encounters
    # ... (Add more location-specific encounter data)
    else:
        encounter_chance = 0.3  # Default chance for other locations
        possible_encounters = ["Goblin", "Kobold", "Wolf"] 

    if random.random() < encounter_chance:
        monster_name = random.choice(possible_encounters)
        monster = Monster.from_data(monster_data[monster_name])
        return monster
    else:
        return None


def handle_encounter(player, monster):
    """Handles a random encounter, initiating combat or allowing the player to flee.

    Args:
        player: The Player object.
        monster: The Monster object encountered.
    """
    print(f"\nYou've encountered a {monster.name}!")

    while True:
        print("\nWhat will you do?")
        print("1. Fight")
        print("2. Attempt to flee")

        choice = input("> ")

        if choice == '1':
            initiate_combat(player, monster)
            break 
        elif choice == '2':
            if attempt_flee(player, monster):
                print("You successfully fled the encounter!")
                break
            else:
                print("You failed to flee! The monster attacks!")
                initiate_combat(player, monster)
                break
        else:
            print("Invalid choice.")

def attempt_flee(player, monster):
    """Determines if the player successfully flees from an encounter.

    Args:
        player: The Player object.
        monster: The Monster object.

    Returns:
        True if the player successfully flees, False otherwise.
    """
    # Basic flee mechanic based on Dexterity checks (can be customized)
    player_roll = roll_dice(1, 20) + player.dexterity_modifier
    monster_roll = roll_dice(1, 20) + monster.dexterity

    if player_roll > monster_roll:
        return True
    else:
        return False


def display_map(current_location):
    """Displays an ASCII art map of the current location.

    Args:
        current_location: The Location object representing the player's current location.
    """
    # Retrieve and display the map based on location name
    map_data = {
        "Town Square": town_square_map,
        "Feywood Forest Edge": feywood_forest_edge_map,
        # ... (Add more maps for other locations)
    }

    if current_location.name in map_data:
        print(map_data[current_location.name])
    else:
        print("No map available for this location.")