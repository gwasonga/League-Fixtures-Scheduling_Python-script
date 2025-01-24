import os
import pandas as pd
from datetime import datetime, timedelta

# Your list of team names
teams = ["Ababu", "Abel", "Abraham", "Achar", "Achoki", "Agullo", "Akello", "Ayara", "Baraza", "Chamwada", "Chris",
         "Dancan", "Felix", "Gilbert", "Grado", "Hon Abito", "Jobroz", "Joshwa", "Junior", "Lawi", "Lenox", "Lessing",
         "Mutisya", "Ndinya", "Ochido", "Ofweneke", "Ogega", "Ogutu", "Oscar", "Osoro", "Jaosingo", "Patel", "Shaddy"]

# Number of teams
num_teams = len(teams)

# Define the league start date
league_start_date = datetime.strptime("2025-01-25", "%Y-%m-%d")

# Create an empty list to store the fixtures with dates
fixtures_with_dates = []

# Generate all fixtures with bye week handling
def generate_fixtures_with_bye(teams):
    if len(teams) % 2 != 0:
        teams.append("Bye")  # Add a dummy team for bye weeks
    
    fixtures = []
    num_rounds = len(teams) - 1
    num_matches_per_round = len(teams) // 2
    
    for round_num in range(num_rounds):
        round_fixtures = []
        for i in range(num_matches_per_round):
            home = teams[i]
            away = teams[-(i + 1)]
            if home != "Bye" and away != "Bye":
                round_fixtures.append([home, away])
        
        # Rotate teams for the next round
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]
        fixtures.extend(round_fixtures)
    
    return fixtures

# Generate fixtures with bye handling
all_fixtures = generate_fixtures_with_bye(teams)

# Schedule fixtures over weekends (rest of your script remains the same)
current_date = league_start_date
while all_fixtures:
    saturday_fixtures, sunday_fixtures_1, sunday_fixtures_2 = create_weekend_fixtures(teams, all_fixtures)
    
    # Assign fixtures to Saturday, Sunday Morning, and Sunday Afternoon
    for fixture in saturday_fixtures:
        fixtures_with_dates.append([fixture[0], fixture[1], current_date.strftime("%Y-%m-%d"), 'Saturday'])
    for fixture in sunday_fixtures_1:
        fixtures_with_dates.append([fixture[0], fixture[1], (current_date + timedelta(days=1)).strftime("%Y-%m-%d"), 'Sunday Morning'])
    for fixture in sunday_fixtures_2:
        fixtures_with_dates.append([fixture[0], fixture[1], (current_date + timedelta(days=1)).strftime("%Y-%m-%d"), 'Sunday Afternoon'])
    
    # Remove scheduled fixtures from the list
    all_fixtures = [f for f in all_fixtures if f not in saturday_fixtures and f not in sunday_fixtures_1 and f not in sunday_fixtures_2]
    
    # Move to the next weekend
    current_date += timedelta(days=7)

# Save to CSV as before
fixtures_with_dates_df = pd.DataFrame(fixtures_with_dates, columns=['HomeTeam', 'AwayTeam', 'MatchDate', 'Day'])
try:
    fixtures_with_dates_df.to_csv(output_file_path, index=False)
    print(f"Fixtures with dates have been saved to {os.path.abspath(output_file_path)}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
