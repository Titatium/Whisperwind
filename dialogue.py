from utils import display_dialogue, get_user_choice
from world import generate_random_encounter, handle_encounter
from combat import initiate_combat
from monster import Monster
from items import items_data
from quests import *
from location import Location

# NPC Dialogue Data (Example, expand based on your NPCs and quests)
npc_dialogues = {
    "Lily Rootwhistle": {
        "general": [
            "The Feywood is a beautiful but dangerous place. Be careful out there.",
            "If you need any healing potions or herbs, just let me know."
        ],
        "Rootwhistle Apothecary": [
            "Welcome to my apothecary! How can I help you today?",
            "I have a wide selection of potions and herbs for all your adventuring needs."
        ],
        "Whispers in the Woods": {
            "dialogue": [
                "I've heard whispers of strange happenings in the Feywood. It's unsettling.",
                "If you're venturing into the woods, be cautious. The Fey can be unpredictable."
            ]
        },
        "Herbalist's Errand": {
            "dialogue": [
                "I desperately need some moonpetals and glowcaps for a special potion. Could you gather some for me?",
                "They can be found in the Feywood, but be careful. The Fey are protective of their plants."
            ],
            "prerequisites": [], # No prerequisites for this dialogue
            "updates": [
                {"type": "add_objective", "objective": "Gather moonpetals and glowcaps for Lily"}
            ]
        }
    },
    "Barkeep": {
        "general": [
            "Welcome to the Gilded Tankard! What can I get for you?",
            "We have the finest ales and meads in all of Whisperwind.",
            "If you're looking for adventure, you might hear some interesting rumors around here."
        ],
        "Gilded Tankard": [
            "Pull up a chair and relax. The fire's warm and the company's good.",
            "Heard any good stories lately? The Feywood's been acting up, they say."
        ],
        "Whispers in the Woods": {
            "dialogue": [
                "Aye, there's been talk of strange lights and eerie sounds coming from the Feywood.",
                "Some say the Fey are restless, others whisper of darker forces at play."
            ]
        }
    },
    "Old Silas": {
        "general": [
            "Hmm, what do you want? I'm busy.",
            "If you're looking for trinkets or treasures, you've come to the right place... maybe."
        ],
        "Silas' Sundries": [
            "Take a look around. Just don't touch anything unless you're buying.",
            "I've got all sorts of oddities here. Some might even be magical... if you believe in that sort of thing."
        ],
        "Cursed Trinket": {
            "dialogue": [
                "This blasted locket! It's been giving me nothing but trouble.",
                "If you can figure out how to lift the curse, I'll reward you handsomely."
            ],
            "prerequisites": [],  # No prerequisites for this dialogue
            "updates": [
                {"type": "add_objective", "objective": "Lift the curse on Silas' locket"}
            ]
        }
    },
    # Add more NPCs and their dialogues here
}

# Quest-related Dialogue Data (Example, expand based on your quests)
quest_data = {
    "Lily Rootwhistle": {
        "Herbalist's Errand": {
            "dialogue": [
                "Did you find those moonpetals and glowcaps? I'm eager to finish my potion.",
                "If you have them, I'll gladly reward you."
            ],
            "prerequisites": [
                {"item": "moonpetal", "quantity": 3},
                {"item": "glowcap", "quantity": 2}
            ]
        }
    },
    "Old Silas": {
        "Cursed Trinket": {
            "dialogue": [
                "Have you managed to lift the curse on my locket?",
                "If so, I'm a man of my word. Here's your reward."
            ],
            "prerequisites": [
                {"quest_flag": "cursed_locket_cleansed"}  # Example flag to track curse removal
            ]
        }
    }
    # Add more quest-related dialogues here
}

def initiate_dialogue(player, npc_name, location):
    """Initiates dialogue with an NPC based on their name and the current location."""

    # Fetch NPC dialogue data
    npc_dialogue_data = npc_dialogues.get(npc_name)
    if not npc_dialogue_data:
        display_dialogue(npc_name, ["I have nothing to say to you."], speaker="NPC")
        return

    # General conversation (with some personality)
    if "general" in npc_dialogue_data:
        # Add variations to general dialogue based on NPC personality or player's actions
        if npc_name == "Barkeep":
            if player.gold < 5:
                display_dialogue(npc_name, ["Looks like you're a bit short on coin. Maybe try your luck at the tables?"], speaker="NPC")
            else:
                display_dialogue(npc_name, npc_dialogue_data["general"], speaker="NPC")
        else:
            display_dialogue(npc_name, npc_dialogue_data["general"], speaker="NPC")

    # Location-specific dialogue
    if location.name in npc_dialogue_data:
        display_dialogue(npc_name, npc_dialogue_data[location.name], speaker="NPC")

    # Quest-related dialogue
    if player.active_quest and npc_name in quest_data:
        quest_dialogue = quest_data[npc_name].get(player.active_quest.name)
        if quest_dialogue:
            # Check prerequisites
            if "prerequisites" in quest_dialogue:
                if not all(player.check_requirement(req) for req in quest_dialogue["prerequisites"]):
                    display_dialogue(npc_name, ["I can't help you with that right now."], speaker="NPC")
                    return

            # Display dialogue and handle potential choices
            while True:  # Loop until a valid choice is made or dialogue ends
                display_dialogue(npc_name, quest_dialogue["dialogue"], speaker="NPC")
                if "choices" in quest_dialogue:
                    choice = get_user_choice(quest_dialogue["choices"])
                    if choice in quest_dialogue["choices"]:
                        handle_choice(player, npc_name, choice, quest_dialogue)
                        break  # Exit the loop after handling the choice
                else:
                    break  # No choices, exit the loop

            # Update quest objectives or trigger events
            if "updates" in quest_dialogue:
                for update in quest_dialogue["updates"]:
                    if update["type"] == "remove_objective":
                        player.active_quest.objectives.remove(update["objective"])
                    elif update["type"] == "add_objective":
                        player.active_quest.objectives.append(update["objective"])
                    # ... (Add more update types as needed)

            # Check for quest completion
            check_quest_progress(player, location)

    # Shop functionality (if applicable)
    if "shop" in npc_dialogue_data:
        display_dialogue(npc_name, ["Welcome to my shop! What would you like to buy?"], speaker="NPC")
        # Add logic for browsing and purchasing items

    # Add more dialogue options (e.g., rumors, gossip, hints)
    if npc_name == "Barkeep" and location.name == "Gilded Tankard":
        if random.random() < 0.2:  # 20% chance of hearing a rumor
            display_dialogue(npc_name, ["Psst... I heard there's a hidden treasure in the old Willowwood Cemetery. But it's guarded by restless spirits."], speaker="NPC")

# Function to handle player choices in dialogue
def handle_choice(player, npc_name, choice, quest_dialogue):
    """Handles the consequences of a player's choice in dialogue."""

    choice_data = quest_dialogue["choices"][choice]

    # Display the outcome of the choice
    display_dialogue(npc_