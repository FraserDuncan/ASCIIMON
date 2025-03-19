import random
import os
import msvcrt  # For Console.ReadKey equivalent in Windows

# Define the game map
MAP_SIZE = 10
player_pos = [MAP_SIZE // 2, MAP_SIZE // 2]
pokemon_list = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle"]

# Define Pokémon moves
pokemon_moves = {
    "Bulbasaur": ["Tackle", "Vine Whip"],
    "Charmander": ["Scratch", "Ember"],
    "Squirtle": ["Tackle", "Water Gun"],
    "Pikachu": ["Quick Attack", "Thunder Shock"]
}

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
    Version 0.12
    """)
    msvcrt.getch()  # Wait for key press

# ASCII Art for Pokémon
pokemon_ascii = {
    "Pikachu": """
      (\__/)
      (o^.^)
      (> <)
    """,
    "Charmander": """
      (\__/)
      (o.o )
      (>🔥)
    """,
    "Bulbasaur": """
      (\__/)
      (o.o )
      ( <🌱 )
    """,
    "Squirtle": """
      (\__/)
      (o.o )
      ( <💧 )
    """
}

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

# Function for random Pokémon encounters
def encounter_pokemon():
    if random.randint(1, 5) == 1:  # 20% chance of encounter
        pokemon = random.choice(pokemon_list)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print(f"A wild {pokemon} appeared!")
        print(pokemon_ascii[pokemon])
        fight_pokemon(pokemon)

# Function for battling a Pokémon
def fight_pokemon(pokemon):
    while True:
        print("Your available moves:")
        for i, move in enumerate(pokemon_moves[player_pokemon], 1):
            print(f"{i}. {move}")
        action = input("Choose a move or (R)un: ").strip().lower()
        if action.isdigit() and 1 <= int(action) <= len(pokemon_moves[player_pokemon]):
            chosen_move = pokemon_moves[player_pokemon][int(action) - 1]
            print(f"Your {player_pokemon} used {chosen_move}!")
            if random.randint(1, 2) == 1:
                print(f"You defeated {pokemon}!")
                msvcrt.getch()  # Wait for key press
                return
            else:
                print(f"{pokemon} dodged the attack!")
                enemy_move = random.choice(pokemon_moves[pokemon])
                print(f"{pokemon} used {enemy_move}!")
        elif action == "r":
            print("You ran away safely!")
            msvcrt.getch()  # Wait for key press
            return
        else:
            print("Invalid choice.")

# Main game loop
def main():
    global player_pokemon
    display_title()
    player_pokemon = choose_pokemon()
    print(f"Your journey begins with {player_pokemon}!")
    msvcrt.getch()  # Wait for key press before starting
    while True:
        display_map()
        move = input("Move (W/A/S/D): ").strip().lower()
        if move == "w" and player_pos[1] > 0:
            player_pos[1] -= 1
        elif move == "s" and player_pos[1] < MAP_SIZE - 1:
            player_pos[1] += 1
        elif move == "a" and player_pos[0] > 0:
            player_pos[0] -= 1
        elif move == "d" and player_pos[0] < MAP_SIZE - 1:
            player_pos[0] += 1
        else:
            print("Invalid move.")
        encounter_pokemon()

if __name__ == "__main__":
    main()