def create_standings():
   
    print("Welcome to the Team Standings Creator!")
    teams = []

    for i in range(1, 31):
        print(f"\nEnter record for Team {i}:")
        team_name = input("Team Name (or type 'done' to finish): ").strip()
        if team_name.lower() == "done":
            break

        try:
            wins = int(input(f"Enter number of wins for {team_name}: "))
            losses = int(input(f"Enter number of losses for {team_name}: "))
        except ValueError:
            print("Invalid input! Wins and losses must be integers. Try again.")
            continue

        teams.append({"name": team_name, "wins": wins, "losses": losses})

    
    def sort_teams(team):
        return (-team["wins"], team["losses"])


    teams.sort(key=sort_teams)

    print("\nNBA-Style Team Standings")
    print("=" * 40)
    print(f"{'Rank':<5}{'Team':<20}{'Wins':<8}{'Losses':<8}")
    print("-" * 40)
    for rank, team in enumerate(teams, start=1):
        print(f"{rank:<5}{team['name']:<20}{team['wins']:<8}{team['losses']:<8}")
    print("=" * 40)



create_standings()
