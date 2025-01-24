#SHEDULING TWO GAMES PER WEEK EVERY WEEKEND
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

# Function to create fixtures for a weekend with two matches per team
def create_weekend_fixtures(teams, fixtures):
    saturday_fixtures = []
    sunday_fixtures = []
    used_teams_saturday = set()
    used_teams_sunday = set()
    
    for fixture in fixtures:
        if fixture[0] not in used_teams_saturday and fixture[1] not in used_teams_saturday:
            if len(saturday_fixtures) < num_teams // 2:
                saturday_fixtures.append(fixture)
                used_teams_saturday.add(fixture[0])
                used_teams_saturday.add(fixture[1])
        
        elif fixture[0] not in used_teams_sunday and fixture[1] not in used_teams_sunday:
            if len(sunday_fixtures) < num_teams // 2:
                sunday_fixtures.append(fixture)
                used_teams_sunday.add(fixture[0])
                used_teams_sunday.add(fixture[1])

        if len(saturday_fixtures) == num_teams // 2 and len(sunday_fixtures) == num_teams // 2:
            break
            
    return saturday_fixtures, sunday_fixtures

# Generate all fixtures
all_fixtures = generate_all_fixtures(teams)

# Schedule fixtures over weekends
current_date = league_start_date
while all_fixtures:
    saturday_fixtures, sunday_fixtures = create_weekend_fixtures(teams, all_fixtures)
    
    # Assign fixtures to Saturday and Sunday
    for fixture in saturday_fixtures:
        fixtures_with_dates.append([fixture[0], fixture[1], current_date.strftime("%Y-%m-%d"), 'Saturday'])
    for fixture in sunday_fixtures:
        fixtures_with_dates.append([fixture[0], fixture[1], (current_date + timedelta(days=1)).strftime("%Y-%m-%d"), 'Sunday'])
    
    # Remove scheduled fixtures from the list
    all_fixtures = [f for f in all_fixtures if f not in saturday_fixtures and f not in sunday_fixtures]
    
    # Move to the next weekend
    current_date += timedelta(days=7)

# Convert the fixture dates list to a DataFrame
fixtures_with_dates_df = pd.DataFrame(fixtures_with_dates, columns=['HomeTeam', 'AwayTeam', 'MatchDate', 'Day'])

# Define the output file path
output_file_path = "C:/Users/Wasonga/Desktop/Pool_League/pool_league_fixtures_with_dates.csv"

# Save the DataFrame to a CSV file
try:
    fixtures_with_dates_df.to_csv(output_file_path, index=False)
    print(f"Fixtures with dates have been saved to {os.path.abspath(output_file_path)}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")



