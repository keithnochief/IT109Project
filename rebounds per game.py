def calculate_player_ppg():
    print("Enter player stats for each game. Type 'done' when finished.\n")
    
    total_points = 0
    total_rebounds = 0
    games_played = 0

    while True:
        try:
            points = input(f"Enter points for game {games_played + 1} (or 'done' to finish): ")
            if points.lower() == 'done':
                break
            rebounds = input(f"Enter rebounds for game {games_played + 1}: ")

            
            points = int(points)
            rebounds = int(rebounds)

            total_points += points
            total_rebounds += rebounds
            games_played += 1
        except ValueError:
            print("Invalid input. Please enter numeric values or 'done'.")
            continue

    if games_played == 0:
        print("\nNo games entered.")
        return

    avg_points = total_points / games_played
    avg_rebounds = total_rebounds / games_played

    print("\nPlayer Stats:")
    print(f"Games Played: {games_played}")
    print(f"Total Points: {total_points}")
    print(f"Total Rebounds: {total_rebounds}")
    print(f"Average Points per Game: {avg_points:.2f}")
    print(f"Average Rebounds per Game: {avg_rebounds}")

calculate_player_ppg()