# Initialize a list to store game blocks
game_blocks = []

# Prompt the user to enter the number of games
while True:
    try:
        num_games = int(input("Enter the number of games (2-5): "))
        if 2 <= num_games <= 5:
            break  # Exit the loop if input is valid
        else:
            print("Please enter a number between 2 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Loop to collect data for each game
for game in range(1, num_games + 1):
    while True:
        try:
            # Input for player's first and last name
            first_name = input(f"Enter the first name of the player for game {game}: ").strip()
            last_name = input(f"Enter the last name of the player for game {game}: ").strip()
            if not first_name or not last_name:
                print("First and last name cannot be empty. Please enter valid names.")
                continue
            
            # Input for assists
            blocks = int(input(f"Enter the number of blocks for game {game}: "))
            
            # Create a block (dictionary) for the game
            game_block = {
                "Game": f"Game {game}",
                "Player": f"{first_name} {last_name}",
                "Blocks": blocks
            }
            
            # Add the block to the list
            game_blocks.append(game_block)
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input for assists. Please enter a valid number.")

# Display the stored blocks
print("\nBlocks data stored as blocks:")
for block in game_blocks:
    print(block)

# Display the total number of blocks
print(f"\nTotal number of blocks (games): {len(game_blocks)}")
