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
    Version 0.19
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
def display_battle_scene(player_pokemon, player_health, enemy_pokemon, enemy_health):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print(f"🌿🔥💧⚡ A wild {enemy_pokemon} appeared! 🌿🔥💧⚡\n")

    player_art = pokemon_data[player_pokemon]["art"].split("\n")
    enemy_art = pokemon_data[enemy_pokemon]["art"].split("\n")
    
    player_health_bar = render_health(player_pokemon, player_health, pokemon_data[player_pokemon]["max_health"]).split("\n")
    enemy_health_bar = render_health(enemy_pokemon, enemy_health, pokemon_data[enemy_pokemon]["max_health"]).split("\n")

    for i in range(max(len(player_health_bar), len(enemy_health_bar))):
        player_line = player_health_bar[i] if i < len(player_health_bar) else ""
        enemy_line = enemy_health_bar[i] if i < len(enemy_health_bar) else ""
        print(f"{player_line:<15}{' ' * 10}{enemy_line}")

    print("\n")

    for i in range(max(len(player_art), len(enemy_art))):
        player_line = player_art[i] if i < len(player_art) else ""
        enemy_line = enemy_art[i] if i < len(enemy_art) else ""
        print(f"{player_line:<15}{' ' * 10}{enemy_line}")

# Function for random Pokémon encounters
def encounter_pokemon():
    if random.randint(1, 5) == 1:  # 20% chance of encounter
        enemy_pokemon = random.choice(pokemon_list)
        player_health = pokemon_data[player_pokemon]["max_health"]
        enemy_health = pokemon_data[enemy_pokemon]["max_health"]
        fight_pokemon(player_pokemon, player_health, enemy_pokemon, enemy_health)

# Function to choose a starter Pokémon
def choose_pokemon():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    starters = ["Bulbasaur", "Charmander", "Squirtle"]
    while True:
        print("Choose your starter Pokémon: Bulbasaur, Charmander, or Squirtle")
        choice = input("Enter your choice: ").strip().capitalize()
        if choice in starters:
            print(f"You chose {choice}!")
            return choice
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
        
# Function to simulate a Pokémon battle
def fight_pokemon(player_pokemon, player_health, enemy_pokemon, enemy_health):
    while player_health > 0 and enemy_health > 0:
        display_battle_scene(player_pokemon, player_health, enemy_pokemon, enemy_health)

        print("\nYour available moves:")
        for i, move in enumerate(pokemon_data[player_pokemon]["moves"], 1):
            print(f"{i}. {move}")
        
        action = input("Choose a move or (R)un: ").strip().lower()
        if action.isdigit() and 1 <= int(action) <= len(pokemon_data[player_pokemon]["moves"]):
            chosen_move = pokemon_data[player_pokemon]["moves"][int(action) - 1]
            print(f"\nYour {player_pokemon} used {chosen_move}!")
            time.sleep(2)  # Delay before result
            
            if random.randint(1, 2) == 1:
                enemy_health -= 4  # Fixed damage for now
                if enemy_health <= 0:
                    print(f"\n🎉 You defeated {enemy_pokemon}! 🎉")
                    msvcrt.getch()  # Wait for key press
                    return
            else:
                print(f"\n{enemy_pokemon} dodged the attack!")

            time.sleep(2)  # Delay before enemy move
            
            if enemy_health > 0:
                enemy_move = random.choice(pokemon_data[enemy_pokemon]["moves"])
                print(f"{enemy_pokemon} used {enemy_move}!")
                time.sleep(2)  # Delay before checking dodge
                
                # **NEW DODGE MECHANIC**
                if random.randint(1, 2) == 1:  # 50% chance to dodge
                    print(f"\n🙌 Your {player_pokemon} dodged the attack! 🙌")
                else:
                    player_health -= 4  # Fixed damage for now
                    print(f"\n💥 {player_pokemon} took damage! 💥")

        elif action == "r":
            print("\n🏃 You ran away safely! 🏃")
            msvcrt.getch()  # Wait for key press
            return
        else:
            print("\nInvalid choice. Try again.")

    if player_health <= 0:
        print("\n💀 Your Pokémon fainted! You blacked out! 💀")
        msvcrt.getch()

# Main game loop
def main():
    global player_pokemon
    display_title()
    player_pokemon = choose_pokemon()
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