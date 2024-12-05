game_turnovers = []

while True:
    try:
        num_games = int(input("Enter the number of games (2-5): "))
        if 2 <= num_games <= 5:
            break  
        else:
            print("Please enter a number between 2 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

for game in range(1, num_games + 1):
    while True:
        try:
            first_name = input(f"Enter the first name of the player for game {game}: ").strip()
            last_name = input(f"Enter the last name of the player for game {game}: ").strip()
            if not first_name or not last_name:
                print("First and last name cannot be empty. Please enter valid names.")
                continue
            
            turnover = int(input(f"Enter the number of turnovers for game {game}: "))
            
            game_turnover = {
                "Game": f"Game {game}",
                "Player": f"{first_name} {last_name}",
                "Turnover": turnover
            }
            
            game_turnovers.append(game_turnover)
            break 
        except ValueError:
            print("Invalid input for assists. Please enter a valid number.")

print("\nTurnover data stored as blocks:")
for turnover in game_turnover:
    print(turnover)

print(f"\nTotal number of turnovers (games): {len(game_turnover)}")
