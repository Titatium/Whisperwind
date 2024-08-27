from utils import display_dialogue, get_user_choice
from world import generate_random_encounter, handle_encounter
from combat import initiate_combat
from monster import Monster
from items import items_data

class Quest:
    # ... (Quest class definition remains the same)

# Quest 1: Whispers in the Woods
quest_1 = Quest(
    "Whispers in the Woods",
    "Investigate strange occurrences in the Feywood Forest.",
    [
        "Talk to townsfolk about Feywood disturbances",
        "Gather information from Lily Rootwhistle",
        "Locate the source of the disturbances in the Feywood"
    ],
    {"gold": 50, "experience": 100}  # Example rewards
)

def start_quest_1(player):
    """Initiates Quest 1 and sets it as the player's active quest."""
    player.active_quest = quest_1
    display_dialogue(None, ["Strange occurrences in the Feywood Forest have been causing unease among the townsfolk.",
                            "Mayor Elden Rootwhistle has tasked you with investigating these disturbances.",
                            "Perhaps the patrons at the Gilded Tankard or Lily Rootwhistle at the Apothecary might have some information."], speaker="Narrator")

def check_quest_1_completion(player, location):
    """Checks if the objectives for Quest 1 have been completed."""
    if player.active_quest == quest_1:
        if "Talk to townsfolk about Feywood disturbances" in player.active_quest.objectives:
            if location.name == "Gilded Tankard":
                # Logic to check if player has talked to enough townsfolk
                # ...
                if enough_townsfolk_talked_to:
                    player.active_quest.objectives.remove("Talk to townsfolk about Feywood disturbances")
                    display_dialogue(None, ["You've gathered enough information from the townsfolk.",
                                            "It seems the disturbances are indeed real and growing more frequent."], speaker="Narrator")

        if "Gather information from Lily Rootwhistle" in player.active_quest.objectives:
            if location.name == "Rootwhistle Apothecary":
                # Logic to check if player has talked to Lily
                # ...
                if talked_to_lily:
                    player.active_quest.objectives.remove("Gather information from Lily Rootwhistle")
                    display_dialogue("Lily Rootwhistle", ["The Feywood is a place of magic and wonder, but also of danger.",
                                                         "Be careful, and may the blessings of nature guide you."], speaker="NPC")

        if "Locate the source of the disturbances in the Feywood" in player.active_quest.objectives:
            if location.name == "Feywood Forest Edge":  # Or another relevant Feywood location
                # Logic to check if player has found the source (e.g., reached a specific area)
                # ...
                if source_located:
                    player.active_quest.objectives.remove("Locate the source of the disturbances in the Feywood")
                    display_dialogue(None, ["You've found the source of the disturbances!",
                                            "Now, you must face the challenge that awaits..."], speaker="Narrator")

        # Check if all objectives are complete
        if not player.active_quest.objectives:
            complete_quest_1(player)

def complete_quest_1(player):
    """Handles the completion of Quest 1, granting rewards and potentially starting the next quest."""
    display_dialogue(None, ["You've completed the quest: Whispers in the Woods!",
                            "You receive the following rewards:"
                            f"* Gold: {quest_1.rewards['gold']}",
                            f"* Experience: {quest_1.rewards['experience']}"], speaker="Narrator")
    player.gold += quest_1.rewards['gold']
    player.gain_xp(quest_1.rewards['experience'])
    player.active_quest = None  # Clear the active quest

    # Potentially trigger the start of the next quest
    # ...

# Side Quests for Quest 1 (Example implementation, expand as needed)
def herbalists_errand(player):
    # ... (Logic for the Herbalist's Errand side quest)

def lost_in_the_woods(player):
    # ... (Logic for the Lost in the Woods side quest)

# ... (Add more side quest functions)

# Encounter during Quest 1
def goblin_ambush(player, location):
    """Triggers a random encounter with goblins."""
    if random.random() < 0.5:  # 50% chance of encounter
        num_goblins = random.randint(2, 4)  # 2-4 goblins
        goblins = [Monster.from_data(monster_data["Goblin"]) for _ in range(num_goblins)]
        print("\nYou are ambushed by a group of goblins!")
        for goblin in goblins:
            handle_encounter(player, goblin)
            if not player.is_alive():
                # Handle player death
                break
        # Potential rewards or consequences based on encounter outcome
        # ...

# Add this encounter to the Feywood Forest Edge location
location_data["Feywood Forest Edge"]["special_events"].append(goblin_ambush)

# Integrate quest checks into location entering logic
def location_enter_with_quests(player, location):
    """Modified enter function to include quest checks."""
    location.enter(player)
    check_quest_1_completion(player, location)  # Check for Quest 1 completion

# Replace the original enter function in the Location class
Location.enter = location_enter_with_quests

# Logic for checking quest objectives
def check_quest_1_completion(player, location):
    """Checks if the objectives for Quest 1 have been completed."""
    if player.active_quest == quest_1:
        if "Talk to townsfolk about Feywood disturbances" in player.active_quest.objectives:
            if location.name == "Gilded Tankard":
                # Logic to track conversations with townsfolk
                if not hasattr(player, "townsfolk_talked_to"):
                    player.townsfolk_talked_to = 0
                player.townsfolk_talked_to += 1
                if player.townsfolk_talked_to >= 3:  # Talk to at least 3 townsfolk
                    player.active_quest.objectives.remove("Talk to townsfolk about Feywood disturbances")
                    display_dialogue(None, ["You've gathered enough information from the townsfolk.",
                                            "It seems the disturbances are indeed real and growing more frequent."], speaker="Narrator")

        if "Gather information from Lily Rootwhistle" in player.active_quest.objectives:
            if location.name == "Rootwhistle Apothecary" and "Lily Rootwhistle" in location.characters:
                # Initiate dialogue with Lily
                display_dialogue("Lily Rootwhistle", ["The Feywood is a place of magic and wonder, but also of danger.",
                                                     "Be careful, and may the blessings of nature guide you."], speaker="NPC")
                player.active_quest.objectives.remove("Gather information from Lily Rootwhistle")

        if "Locate the source of the disturbances in the Feywood" in player.active_quest.objectives:
            if location.name == "Feywood Forest Clearing":  # Example location within Feywood
                # Logic to check if player has reached the correct area
                # ... (e.g., check player's coordinates or trigger a cutscene)
                if player.coordinates == (5, 10):  # Example coordinates
                    player.active_quest.objectives.remove("Locate the source of the disturbances in the Feywood")
                    display_dialogue(None, ["You've found the source of the disturbances! A swirling vortex of magical energy pulsates at the heart of the clearing.",
                                            "It seems to be the entrance to another realm..."], speaker="Narrator")

        # Check if all objectives are complete
        if not player.active_quest.objectives:
            complete_quest_1(player)

# Flesh out a side quest (Example: Herbalist's Errand)
def herbalists_errand(player):
    if player.active_quest == quest_1 and "Herbalist's Errand" not in player.completed_quests:
        if "moonpetal" in player.inventory and "glowcap" in player.inventory:
            # Player has the required herbs
            display_dialogue("Lily Rootwhistle", ["Ah, you've found the herbs! Thank you so much!",
                                                 "Here's the healing potion I promised, and a little extra for your troubles."], speaker="NPC")
            player.inventory.remove("moonpetal")
            player.inventory.remove("glowcap")
            player.add_item_to_inventory("healing_potion")
            player.gold += 10
            player.completed_quests.append("Herbalist's Errand")
        else:
            display_dialogue("Lily Rootwhistle", ["I still need those moonpetals and glowcaps. Please hurry!"], speaker="NPC")

# Add more encounters to Feywood Forest Edge
def mischievous_pixie_encounter(player, location):
    if random.random() < 0.3:  # 30% chance of encounter
        print("\nA mischievous pixie flits around you, giggling and casting playful spells.")
        choices = ["Try to catch the pixie", "Ignore the pixie and continue on your way"]
        choice = get_user_choice(choices)
        if choice == 1:
            # Logic for trying to catch the pixie (e.g., a skill check)
            # ...
        # Potential consequences or rewards based on the player's choice
        # ...

location_data["Feywood Forest Edge"]["special_events"].append(mischievous_pixie_encounter)