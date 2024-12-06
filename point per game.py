def calculate_player_ppg():

    game_stats = []

    # Prompt user to enter the number of games
    while True:
        try:
            num_games = int(input("How many games (2-5)? "))
            if 2 <= num_games <= 5:
                break
            else:
                print("Please enter a number between 2 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Collect stats for each game
    for game in range(1, num_games + 1):
        while True:
            try:
                print(f"\nGame {game}:")
                points = int(input("Enter points: "))

                # Add the game stats to the list
                game_stats.append({"game": game, "points": points})
                break
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    # Calculate total and average stats
    total_points = sum(game["points"] for game in game_stats)

    avg_points = total_points / num_games

    # Display results
    print("\nPlayer Stats per Game:")
    for game in game_stats:
        print(f"Game {game['game']}: Points = {game['points']}")

    print("\nSummary:")
    print(f"Games Played: {num_games}")
    print(f"Total Points: {total_points}")
    print(f"Average Points per Game: {avg_points:.2f}")

calculate_player_ppg()
