import csv

def read_player_stats(file_path):
    player_stats = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            player_stats[row['Player']] = {
                'Points': float(row['PPG']),
                'Assists': float(row['APG']),
                'Rebounds': float(row['RPG'])
            }
    return player_stats


# Allows users to input stats for games
def input_stats(players):
    num_games = int(input("Enter the number of games to track (2-5): "))
    
    for player in players:
        print(f"Entering stats for {player}")
        for game in range(num_games):
            points = int(input(f"Enter points for game {game + 1}: "))
            assists = int(input(f"Enter assists for game {game + 1}: "))
            rebounds = int(input(f"Enter rebounds for game {game + 1}: "))
            players[player].append({
                "points": points,
                "assists": assists,
                "rebounds": rebounds
            })

# calculate averages for the games entered
def calculate_averages(player_stats):
    averages = {}
    for player, stats in player_stats.items():
        if stats:
            total_points = sum(stat["points"] for stat in stats)
            total_assists = sum(stat["assists"] for stat in stats)
            total_rebounds = sum(stat["rebounds"] for stat in stats)
            num_games = len(stats)
            averages[player] = {
                "Average Points": total_points / num_games,
                "Average Assists": total_assists / num_games,
                "Average Rebounds": total_rebounds / num_games
            }
    return averages

# displayes the averaged stats
def display_averages(averages):
    print("\nAverage Stats for Top 20 NBA Players:")
    for player, stats in averages.items():
        print(f"{player}: {stats['Average Points']:.2f} points, {stats['Average Assists']:.2f} assists, {stats['Average Rebounds']:.2f} rebounds")

def main():
    player_stats = {
        "LeBron James": [],
        "Kevin Durant": [],
        "Stephen Curry": [],
        "Giannis Antetokounmpo": [],
        "James Harden": [],
        "Luka Dončić": [],
        "Anthony Davis": [],
        "Damian Lillard": [],
        "Kawhi Leonard": [],
        "Jayson Tatum": [],
        "Joel Embiid": [],
        "Nikola Jokić": [],
        "Jimmy Butler": [],
        "Kyrie Irving": [],
        "Bradley Beal": [],
        "Paul George": [],
        "Devin Booker": [],
        "Zion Williamson": [],
        "Trae Young": [],
        "Donovan Mitchell": []
    }

   
    
if __name__ == "__main__":
    main()

