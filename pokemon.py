import random
import os
import msvcrt  # For Console.ReadKey equivalent in Windows
import time  # For adding delays

# Define the game map
MAP_SIZE = 10
player_pos = [MAP_SIZE // 2, MAP_SIZE // 2]

# Define Pokémon data (moves, health, and ASCII art)
pokemon_data = {
    "Bulbasaur": {
        "moves": ["Tackle", "Vine Whip"],
        "max_health": 20,
        "art": """
          (\__/)
          (o.o )
          ( <🌱 )
        """
    },
    "Charmander": {
        "moves": ["Scratch", "Ember"],
        "max_health": 20,
        "art": """
          (\__/)
          (o.o )
          (>🔥)  
        """
    },
    "Squirtle": {
        "moves": ["Tackle", "Water Gun"],
        "max_health": 20,
        "art": """
          (\__/)
          (o.o )
          ( <💧 )
        """
    },
    "Pikachu": {
        "moves": ["Quick Attack", "Thunder Shock"],
        "max_health": 20,
        "art": """
          (\__/)
          (o^.^)
          (>⚡)
        """
    }
}
move_data = {
    "Tackle": {"power": 40, "accuracy": 100, "pp": 35},
    "Vine Whip": {"power": 45, "accuracy": 100, "pp": 25},
    "Scratch": {"power": 40, "accuracy": 100, "pp": 35},
    "Ember": {"power": 40, "accuracy": 100, "pp": 25},
    "Water Gun": {"power": 40, "accuracy": 100, "pp": 25},
    "Quick Attack": {"power": 40, "accuracy": 100, "pp": 30},
    "Thunder Shock": {"power": 40, "accuracy": 100, "pp": 30}
}

pokemon_list = list(pokemon_data.keys())  # List of available Pokémon

# ASCII Art for Title Screen
def display_title():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("""
     █████╗ ███████╗ ██████╗██╗██╗███╗   ███╗ ██████╗ ███╗   ██╗
    ██╔══██╗██╔════╝██╔════╝██║██║████╗ ████║██╔═══██╗████╗  ██║
    ███████║███████╗██║     ██║██║██╔████╔██║██║   ██║██╔██╗ ██║
    ██╔══██║╚════██║██║     ██║██║██║╚██╔╝██║██║   ██║██║╚██╗██║
    ██║  ██║███████║╚██████╗██║██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    Version 0.31
    """)
    msvcrt.getch()  # Wait for key press

# Function to render health bars
def render_health(name, health, max_health):
    bar_length = 5  # Total number of blocks
    filled_blocks = health // 4  # Each block represents 4 HP
    empty_blocks = bar_length - filled_blocks
    health_bar = "█" * filled_blocks + " " * empty_blocks
    return f"{name}\n[{health_bar}] {health}/{max_health}\n"

# Function to display Pokémon battle scene with health bars
def display_battle_scene(player_pokemon, player_health, enemy_pokemon, enemy_health, last_action_player, last_action_enemy):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    
    # Show the last two moves at the top
    print(f"{last_action_player}\n{last_action_enemy}\n")

    # Use the player's custom Pokémon nickname instead of the default name
    player_health_bar = render_health(player_nickname, player_health, pokemon_data[player_pokemon]["max_health"]).split("\n")
    enemy_health_bar = render_health(enemy_pokemon, enemy_health, pokemon_data[enemy_pokemon]["max_health"]).split("\n")

    player_art = pokemon_data[player_pokemon]["art"].split("\n")
    enemy_art = pokemon_data[enemy_pokemon]["art"].split("\n")

    # Print health bars first
    for i in range(max(len(player_health_bar), len(enemy_health_bar))):
        player_line = player_health_bar[i] if i < len(player_health_bar) else ""
        enemy_line = enemy_health_bar[i] if i < len(enemy_health_bar) else ""
        print(f"{player_line:<15}{' ' * 10}{enemy_line}")

    print()

    # Print Pokémon ASCII art
    for i in range(max(len(player_art), len(enemy_art))):
        player_line = player_art[i] if i < len(player_art) else ""
        enemy_line = enemy_art[i] if i < len(enemy_art) else ""
        print(f"{player_line:<15}{' ' * 10}{enemy_line}")

# Function for random Pokémon encounters
def encounter_pokemon():
    if random.randint(1, 5) == 1:  # 20% chance of encounter
        enemy_pokemon = random.choice(pokemon_list)
        
        # Get player's health correctly
        player_health = pokemon_data[player_pokemon]["max_health"]
        enemy_health = pokemon_data[enemy_pokemon]["max_health"]
        
        fight_pokemon(player_pokemon, player_health, enemy_pokemon, enemy_health)


# Function to choose a starter Pokémon
def choose_pokemon():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    starters = ["Bulbasaur", "Charmander", "Squirtle"]
    
    # Ask for the trainer's name
    trainer_name = input("Enter your trainer name: ").strip()
    print(f"\nWelcome, {trainer_name}! Your journey is about to begin!\n")
    time.sleep(1)

    while True:
        print("Choose your starter Pokémon: Bulbasaur, Charmander, or Squirtle")
        choice = input("Enter your choice: ").strip().capitalize()
        if choice in starters:
            print(f"\nYou chose {choice}!")
            
            # **Force naming the Pokémon**
            while True:
                nickname = input(f"Give your {choice} a nickname: ").strip()
                if nickname:  # Ensures the name isn't empty
                    break
                print("⚠ You must enter a name for your Pokémon!")
            
            print(f"\n{trainer_name}, your Pokémon {nickname} is ready for battle!")
            return trainer_name, choice, nickname
        else:
            print("Invalid choice. Please select Bulbasaur, Charmander, or Squirtle.")

# Function to display the game map
def display_map():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            if [x, y] == player_pos:
                print("P", end=" ")  # Player character
            else:
                print(".", end=" ")  # Empty space
        print()

def initialize_pp(pokemon):
    """Returns a dictionary tracking PP for each move of the Pokémon."""
    return {move: move_data[move]["pp"] for move in pokemon_data[pokemon]["moves"]}

# Function to display available moves with PP
def display_moves_with_pp(player_pokemon):
    print("\nYour available moves:")
    for i, move in enumerate(pokemon_data[player_pokemon]["moves"], 1):
        pp_left = pokemon_pp[move]
        pwr = move_data[move]["power"]
        acc = move_data[move]["accuracy"]
        print(f"{i}. {move} ⚡: {pwr}, 🎯: {acc}%, 🔋 PP: {pp_left}")

# Function to simulate a Pokémon battle
def fight_pokemon(player_pokemon, player_health, enemy_pokemon, enemy_health):
    global player_nickname, trainer_name  
    last_action_player = f"A wild {enemy_pokemon} appeared!"  
    last_action_enemy = ""

    # Initialize PP for both Pokémon
    global pokemon_pp
    pokemon_pp = initialize_pp(player_pokemon)
    enemy_pp = initialize_pp(enemy_pokemon)

    while player_health > 0 and enemy_health > 0:
        display_battle_scene(player_pokemon, player_health, enemy_pokemon, enemy_health, last_action_player, last_action_enemy)

        # Display moves with PP
        display_moves_with_pp(player_pokemon)

        action = input("Choose a move or (R)un: ").strip().lower()
        if action.isdigit() and 1 <= int(action) <= len(pokemon_data[player_pokemon]["moves"]):
            chosen_move = pokemon_data[player_pokemon]["moves"][int(action) - 1]
            move_stats = move_data[chosen_move]

            # Check if move has PP
            if pokemon_pp[chosen_move] > 0:
                pokemon_pp[chosen_move] -= 1  # Reduce PP
                last_action_player = f"\n{player_nickname} used {chosen_move}!"

                # Check accuracy
                if random.randint(1, 100) <= move_stats["accuracy"]:
                    damage = move_stats["power"] // 10  # Temporary flat damage
                    enemy_health -= damage
                    if enemy_health <= 0:
                        last_action_player = f"\n🎉 {enemy_pokemon} fainted! You win! 🎉"
                        last_action_enemy = ""
                        time.sleep(2)
                        display_battle_scene(player_pokemon, player_health, enemy_pokemon, enemy_health, last_action_player, last_action_enemy)
                        msvcrt.getch()
                        return
                else:
                    last_action_player = f"\n{player_nickname} used {chosen_move}, but it missed!"
            else:
                last_action_player = f"\n❌ {player_nickname} tried to use {chosen_move}, but it has no PP left!"
                continue  # Force the player to choose another move

            # Enemy's turn
            if enemy_health > 0:
                enemy_move = random.choice(pokemon_data[enemy_pokemon]["moves"])
                move_stats = move_data[enemy_move]
                last_action_enemy = f"\n{enemy_pokemon} used {enemy_move}!"

                if random.randint(1, 100) <= move_stats["accuracy"]:
                    damage = move_stats["power"] // 10
                    player_health -= damage
                else:
                    last_action_enemy += f"\n🙌 {player_nickname} dodged the attack! 🙌"

        elif action == "r":
            last_action_player = f"\n🏃 {trainer_name} ran away safely! 🏃"
            last_action_enemy = ""
            time.sleep(2)
            display_battle_scene(player_pokemon, player_health, enemy_pokemon, enemy_health, last_action_player, last_action_enemy)
            msvcrt.getch()
            return
        else:
            last_action_player = "\nInvalid choice. Try again."

        time.sleep(2)

# Main game loop
def main():
    global player_pokemon, player_nickname, trainer_name
    display_title()
    trainer_name, player_pokemon, player_nickname = choose_pokemon()
    print(f"\n🌟 Your journey begins with {player_pokemon}! 🌟")
    msvcrt.getch()  # Wait for key press before starting
    while True:
        display_map()
        move = input("\nMove (W/A/S/D): ").strip().lower()
        if move == "w" and player_pos[1] > 0:
            player_pos[1] -= 1
        elif move == "s" and player_pos[1] < MAP_SIZE - 1:
            player_pos[1] += 1
        elif move == "a" and player_pos[0] > 0:
            player_pos[0] -= 1
        elif move == "d" and player_pos[0] < MAP_SIZE - 1:
            player_pos[0] += 1
        else:
            print("\nInvalid move.")
        encounter_pokemon()

if __name__ == "__main__":
    main()