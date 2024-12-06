def calculate_player_rpg():

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
                rebounds = int(input("Enter rebounds: "))

                game_stats.append({"game": game, "rebounds": rebounds})
                break
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    # Calculate total and average stats
    total_rebounds = sum(game["rebounds"] for game in game_stats)

    avg_rebounds = total_rebounds / num_games

    # Display results
    print("\nPlayer Stats per Game:")
    for game in game_stats:
        print(f"Game {game['game']}: Rebounds = {game['rebounds']}")

    print("\nSummary:")
    print(f"Games Played: {num_games}")
    print(f"Total Rebounds: {total_rebounds}")
    print(f"Average Rebounds per Game: {avg_rebounds:.2f}")

calculate_player_rpg()
