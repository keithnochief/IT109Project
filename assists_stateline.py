game_assists = {}

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
            assists = int(input(f"Enter the number of assists for game {game}: "))
            game_assists[f"Game {game}"] = assists
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("\nAssists data stored in the dictionary:")
print(game_assists)
