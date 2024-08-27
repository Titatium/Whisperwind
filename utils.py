import os
import random
import textwrap

from data import npc_dialogues  # Assuming npc_dialogues is in data.py

def clear_screen():
    """Clears the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def roll_dice(num_dice, sides):
    """Rolls a specified number of dice with a given number of sides.

    Args:
        num_dice: The number of dice to roll.
        sides: The number of sides on each die.

    Returns:
        The total result of the dice rolls.
    """
    return sum(random.randint(1, sides) for _ in range(num_dice))


def display_dialogue(npc_name, dialogue_lines, speaker=None):
    """Displays dialogue lines with optional speaker identification and flavorful pauses.

    Args:
        npc_name: The name of the NPC speaking.
        dialogue_lines: A list of dialogue lines to display.
        speaker: An optional string to identify the current speaker ("Player" or "NPC").
    """
    for line in dialogue_lines:
        if speaker:
            prefix = f"{speaker}: " 
        else:
            prefix = ""
        wrapped_line = textwrap.fill(prefix + line, width=70)  # Wrap long lines for better readability
        for part in wrapped_line.splitlines():  # Print each wrapped part with a slight delay
            print(part)
            # Add a pause after each line for a more natural feel (optional)
            # time.sleep(1)  # Uncomment if you want to add pauses 


def get_user_choice(options):
    """Presents a list of options to the user and gets their valid choice.

    Args:
        options: A list of strings representing the available options.

    Returns:
        The index of the chosen option (0-based).
    """
    while True:
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        try:
            choice = int(input("Enter your choice: ")) - 1
            if 0 <= choice < len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def format_output(text, width=70, indent=0):
    """Formats text into wrapped lines with an optional indent.

    Args:
        text: The text to format.
        width: The maximum line width (default: 70).
        indent: The number of spaces to indent each line (default: 0).

    Returns:
        The formatted text as a string.
    """
    return textwrap.fill(text, width=width, initial_indent=" " * indent, subsequent_indent=" " * indent)


# New Utility Function for Flavorful Descriptions
def describe_item(item):
    """Provides a flavorful description of an item, incorporating its attributes and potential uses.

    Args:
        item: An Item object.

    Returns:
        A descriptive string about the item.
    """
    description = item.description  # Start with the base description

    # Add flavor based on item type and attributes
    if item.type == "weapon":
        if item.damage_type == "slashing":
            description += " Its keen edge seems eager to slice through flesh."
        elif item.damage_type == "piercing":
            description += " Its sharp point is designed to puncture armor and find vital organs."
        elif item.damage_type == "bludgeoning":
            description += " Its weight and heft promise to crush bones and shatter shields."

    elif item.type == "armor":
        if item.armor_class > 15:
            description += " It looks sturdy enough to deflect even the mightiest blows."
        elif item.armor_class < 10:
            description += " While offering some protection, it appears rather flimsy."

    # Add more flavor based on other attributes or item-specific lore (optional)

    return description


def handle_npc_dialogue(player, npc):
    """Handles interactive dialogue with an NPC, potentially triggering quests or revealing information.

    Args:
        player: The Player object.
        npc: The NPC object.
    """
    dialogue_options = npc_dialogues.get(npc.name, {}).get("options", [])
    if dialogue_options:
        print(f"\n{npc.name}:")
        choice = get_user_choice(dialogue_options)
        response = npc_dialogues[npc.name]["responses"][choice]
        display_dialogue(npc.name, response, speaker="NPC")

        # Check for quest triggers or updates
        if "quest_trigger" in npc_dialogues[npc.name]:
            quest_name = npc_dialogues[npc.name]["quest_trigger"]
            if choice == 0:  # Assuming the first option triggers the quest
                accept_quest(player, quest_name)

    else:
        display_dialogue(npc.name, npc.dialogue)