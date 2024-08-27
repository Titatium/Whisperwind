import random
import time

from classes import Class
from items import Item
from utils import clear_screen, roll_dice, type_text_slow, color_print

def calculate_damage(attacker, defender):
    """Calculates damage based on attacker's strength and defender's armor."""
    base_damage = roll_dice(1, attacker.strength)
    damage_reduction = roll_dice(1, defender.armor_class) // 2  # Half the armor class for damage reduction
    final_damage = max(0, base_damage - damage_reduction)
    return final_damage

def apply_damage(entity, damage):
    """Applies damage to an entity, potentially killing it."""
    entity.hp -= damage
    if entity.hp <= 0:
        entity.is_alive = False

def display_combat_status(player, enemy):
    """Displays player and enemy health during combat."""
    clear_screen()
    print(f"{player.name}: {player.hp}/{player.max_hp} HP")
    print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP\n")

def player_attack(player, enemy):
    """Handles the player's attack turn."""
    damage = calculate_damage(player, enemy)
    color_print(f"You attack {enemy.name} for {damage} damage!", "green")
    apply_damage(enemy, damage)
    time.sleep(1)

def enemy_attack(player, enemy):
    """Handles the enemy's attack turn."""
    if enemy.is_alive:
        damage = calculate_damage(enemy, player)
        color_print(f"{enemy.name} attacks you for {damage} damage!", "red")
        apply_damage(player, damage)
        time.sleep(1)

def get_player_action():
    """Gets the player's action during combat."""
    while True:
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Use Item")
        print("3. Flee")
        choice = input("> ")

        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice.")

def use_item(player):
    """Allows the player to use an item from their inventory during combat."""
    if not player.inventory:
        print("Your inventory is empty.")
        return

    print("\nChoose an item to use:")
    for i, item in enumerate(player.inventory):
        print(f"{i+1}. {item.name}")
    choice = input("> ")

    try:
        index = int(choice) - 1
        if 0 <= index < len(player.inventory):
            item = player.inventory.pop(index)  # Remove item from inventory
            item.use(player)  # Apply item's effect
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")

def flee(player, enemy):
    """Attempts to flee from combat."""
    if roll_dice(1, 20) + player.dexterity_modifier >= enemy.challenge_rating:
        color_print("You successfully flee from combat!", "yellow")
        return True
    else:
        color_print("You fail to escape!", "red")
        return False

def initiate_combat(player, enemy):
    """Initiates combat between the player and an enemy."""
    clear_screen()
    color_print(f"You are ambushed by a {enemy.name}!", "red")

    while player.is_alive and enemy.is_alive:
        display_combat_status(player, enemy)

        action = get_player_action()
        if action == '1':
            player_attack(player, enemy)
        elif action == '2':
            use_item(player)
        elif action == '3':
            if flee(player, enemy):
                return  # Exit combat if flee is successful

        enemy_attack(player, enemy)

    if not player.is_alive:
        color_print("You have been defeated!", "red")
        # Handle player death (e.g., game over or respawn)
    else:
        color_print(f"You have vanquished the {enemy.name}!", "green")
        # Grant experience, loot, etc.