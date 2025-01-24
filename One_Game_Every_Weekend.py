#ONE GAME PER WEEK EVERY WEEKEND
import os
import pandas as pd
from datetime import datetime, timedelta

# Your list of team names
teams = ["Hon Abito", "Shaddy", "Felix", "Waz Chamwada", "Joshwa", "Hon Baraza", "Abraham", "Ayara", "Chris",
         "Achoki", "Dan Okello", "Otis Jaosingo", "Achar", "Mc Aringo", "Abel", "Grado", "Lessing", "Lawi",
         "Ababu", "Ndinya", "Arnold", "Hon Agullo", "Ochido", "Jobroz", "Akello soldier", "Gilbert", "Godfrey",
         "Ofweneke", "Mutisya", "Dir Ogutu", "Oscar"]

# Number of teams
num_teams = len(teams)

# Define the league start date
league_start_date = datetime.strptime("2024-08-24", "%Y-%m-%d")

# Create an empty list to store the fixtures with dates
fixtures_with_dates = []

# Generate all fixtures where each team plays against every other team once
def generate_all_fixtures(teams):
    fixtures = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            fixtures.append([teams[i], teams[j]])
    return fixtures

# Function to create fixtures for a weekend with one match per team
def create_weekend_fixtures(teams, fixtures):
    weekend_fixtures = []
    used_teams = set()
    
    for fixture in fixtures:
        if fixture[0] not in used_teams and fixture[1] not in used_teams:
            if len(weekend_fixtures) < num_teams // 2:  # Only schedule half of the teams (one match per team)
                weekend_fixtures.append(fixture)
                used_teams.add(fixture[0])
                used_teams.add(fixture[1])
        if len(weekend_fixtures) == num_teams // 2:  # Stop when all teams have one match
            break
    
    return weekend_fixtures

# Generate all fixtures
all_fixtures = generate_all_fixtures(teams)

# Schedule fixtures over weekends
current_date = league_start_date
while all_fixtures:
    weekend_fixtures = create_weekend_fixtures(teams, all_fixtures)
    
    # Assign fixtures to the weekend (Saturday by default)
    for fixture in weekend_fixtures:
        fixtures_with_dates.append([fixture[0], fixture[1], current_date.strftime("%Y-%m-%d"), 'Saturday'])
    
    # Remove scheduled fixtures from the list
    all_fixtures = [f for f in all_fixtures if f not in weekend_fixtures]
    
    # Move to the next weekend
    current_date += timedelta(days=7)

# Convert the fixture dates list to a DataFrame
fixtures_with_dates_df = pd.DataFrame(fixtures_with_dates, columns=['HomeTeam', 'AwayTeam', 'MatchDate', 'Day'])

# Define the output file path
output_file_path = "C:/Users/Wasonga/Desktop/Pool_League/pool_league_fixtures_one_game_per_weekend.csv"

# Save the DataFrame to a CSV file
try:
    fixtures_with_dates_df.to_csv(output_file_path, index=False)
    print(f"Fixtures with dates have been saved to {os.path.abspath(output_file_path)}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
