def create_box_score(team1, team1_points, team2, team2_points):
    print("=" * 30)
    print(f"{'Box Score':^30}")
    print("=" * 30)
    print(f"{'Team':<20}{'Points':>10}")
    print("-" * 30)
    print(f"{team1:<20}{team1_points:>10}")
    print(f"{team2:<20}{team2_points:>10}")
    print("=" * 30)
    if team1_points > team2_points:
        print(f"Winner: {team1}")
    elif team2_points > team1_points:
        print(f"Winner: {team2}")
    else:
        print("It's a tie!")
team1_name = input("Enter the name of Team 1: ")
team1_score = int(input(f"Enter points scored by {team1_name}: "))
team2_name = input("Enter the name of Team 2: ")
team2_score = int(input(f"Enter points scored by {team2_name}: "))

create_box_score(team1_name, team1_score, team2_name, team2_score)
