import json
import random
import time

from character import Player, create_player
from classes import Class
from combat import initiate_combat
from commands import process_command
from dialogue import initiate_dialogue
from location import Location
from npcs import NPC
from quests import Quest, load_quests
from races import Race
from utils import clear_screen, roll_dice, type_text_slow, color_print
from world import generate_random_encounter, handle_encounter, display_map

# Load game data
with open("location_data.json", "r") as f:
    location_data = json.load(f)

quests = load_quests()  # Load quests from quests.py

def main_menu():
    """Displays the main menu with ASCII art and options."""
    clear_screen()
    print("""
     /\\ /\\__ _  _  _ ___  ___ 
    /~~\\/  ' \\/ \\/ \\/ \\ / _ \\
   /    \\____/\\  /\\  /\\  / (_) |
  /_/\\_\\/___/_/\\/  \\/  \\/ \\___/ 

  A Text-Based Adventure in the Feywild
    """)
    print("1. New Game")
    print("2. Load Game (Not yet implemented)")
    print("3. Tutorial")
    print("4. Quit")

def introduction():
    """Provides an immersive introduction to the game world."""
    clear_screen()
    type_text_slow("""
    The sun dips below the horizon, casting long shadows across the cobblestone streets of Whisperwind. 
    Lanterns flicker to life, painting the town in a warm, inviting glow. The air hums with the whispers 
    of the Feywood Forest, a realm of ancient magic and untold secrets that borders the town.

    You, a traveler from distant lands, find yourself drawn to this quaint haven. Perhaps it was fate, 
    the promise of adventure, or simply the allure of the unknown that led you here. But one thing is 
    certain: your destiny is intertwined with the mysteries that lie within Whisperwind and the Feywood...
    """)
    input("\nPress Enter to continue...")

def character_creation():
    """Guides the player through a detailed character creation process."""
    clear_screen()
    color_print("Welcome, traveler! Let's forge your legend...", "green")
    player_name = input("What is your name? ")

    # Race selection with descriptions
    print("\nChoose your race:")
    for race_name, race_data in Race.race_data.items():
        print(f"- {race_name}: {race_data['description']}")
    player_race = input("> ")
    while player_race.lower() not in Race.race_data:
        print("Invalid race. Please choose again.")
        player_race = input("> ")

    # Class selection with descriptions
    print("\nChoose your class:")
    for class_name, class_data in Class.class_data.items():
        print(f"- {class_name}: {class_data['description']}")
    player_class = input("> ")
    while player_class.lower() not in Class.class_data:
        print("Invalid class. Please choose again.")
        player_class = input("> ")

    # Create the player object
    player = create_player(player_name, player_race, player_class)
    print(f"\nBehold, {player.name} the {player.race} {player.class}!")
    time.sleep(2)  # Add a pause for dramatic effect

    return player

def tutorial():
    """Provides an interactive tutorial to introduce game mechanics."""
    clear_screen()
    color_print("Welcome to the tutorial! Let's get you started...", "cyan")
    type_text_slow("""
    You'll explore the world by typing commands. Try 'look' to see your surroundings. 
    To move, use 'go north', 'go south', etc. If you encounter a creature, you can 'fight' or 'flee'.
    """)

    # Simple interactive tutorial steps (expand as needed)
    while True:
        command = input("> ")
        if command.lower() == 'look':
            print("You see a quaint town square with a bustling inn and a few shops.")
            break
        else:
            print("Try typing 'look' to see your surroundings.")

    # ... Add more tutorial steps to cover combat, inventory, etc.

    color_print("\nYou're ready to embark on your adventure! Good luck!", "cyan")
    input("\nPress Enter to continue...")

def game_loop(player):
    """The main game loop, handling player actions and events."""
    current_location = Location.from_data(location_data["Town Square"])  # Start in Town Square

    while True:
        display_map(current_location)
        print(current_location.description)

        # Check for random encounters
        monster = generate_random_encounter(current_location)
        if monster:
            handle_encounter(player, monster)

        # Check for NPCs and initiate dialogue
        for npc_data in current_location.npcs:
            npc = NPC.from_data(npc_data)
            if npc.has_dialogue:
                initiate_dialogue(player, npc)

        # Check for quests and update progress
        for quest in quests:
            quest.check_progress(player, current_location)

        # Get player command and process it
        command = input("> ")
        process_command(player, command, current_location, location_data, quests)

# Main game execution
while True:
    main_menu()
    choice = input("> ")

    if choice == '1':
        introduction()
        player = character_creation()
        game_loop(player)
    elif choice == '2':
        print("Load Game - Not yet implemented")
    elif choice == '3':
        tutorial()
    elif choice == '4':
        print("Farewell, adventurer!")
        break
    else:
        print("Invalid choice.")