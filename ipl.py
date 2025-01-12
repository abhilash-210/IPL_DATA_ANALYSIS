import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Expanded IPL Data with new teams
data = {
    'season': [2023, 2023, 2023, 2022, 2022, 2022, 2021, 2021, 2021, 2023, 2023, 2022, 2022, 2021],
    'team1': ['MI', 'CSK', 'RCB', 'MI', 'KKR', 'CSK', 'DC', 'RCB', 'MI', 'SRH', 'GT', 'LSG', 'PBKS', 'SRH'],
    'team2': ['CSK', 'RCB', 'MI', 'KKR', 'CSK', 'MI', 'MI', 'CSK', 'KKR', 'GT', 'LSG', 'PBKS', 'GT', 'PBKS'],
    'winner': ['MI', 'CSK', 'MI', 'MI', 'KKR', 'CSK', 'DC', 'RCB', 'MI', 'SRH', 'GT', 'LSG', 'PBKS', 'SRH'],
    'city': ['Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Lucknow', 'Mohali', 'Hyderabad'],
    'player_of_match': ['Rohit Sharma', 'MS Dhoni', 'Virat Kohli', 'Jasprit Bumrah', 'Andre Russell', 'Ravindra Jadeja', 'Rishabh Pant', 'AB de Villiers', 'Kieron Pollard',
                        'David Warner', 'Hardik Pandya', 'KL Rahul', 'Shikhar Dhawan', 'Kane Williamson'],
    'runs_scored': [160, 180, 175, 150, 200, 190, 170, 185, 165, 190, 175, 165, 180, 200],
}

# Create a DataFrame
ipl_df = pd.DataFrame(data)

# Basic Data Exploration
print(ipl_df.head())  # View the first few rows
print(ipl_df.info())  # Get information about columns and data types
print("\nDescriptive statistics:\n", ipl_df.describe())  # Summary statistics

# Team Performance
team_wins = ipl_df['winner'].value_counts()
print("\nTeam wins:\n", team_wins)

# Player of the Match Analysis
player_of_match_counts = ipl_df['player_of_match'].value_counts()
print("\nPlayer of the match counts:\n", player_of_match_counts)

# Runs Scored Analysis
average_runs_per_match = ipl_df['runs_scored'].mean()
print("\nAverage Runs scored per match:", average_runs_per_match)

# Matches Played in Each City
city_counts = ipl_df['city'].value_counts()
print("\nMatches played in each city:\n", city_counts)

# Most Successful Team by Season
season_winner = ipl_df.groupby('season')['winner'].value_counts()
print("\nMost successful teams by season:\n", season_winner)

# Visualizations
# 1. Bar chart of Team Wins
plt.figure(figsize=(10, 6))
sns.countplot(x='winner', data=ipl_df, order=team_wins.index)
plt.title('Number of Wins by Team')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.xticks(rotation=45)
plt.show()

# 2. Histogram of Runs Scored
plt.figure(figsize=(8, 5))
plt.hist(ipl_df['runs_scored'], bins=8, color='skyblue', edgecolor='black')
plt.title('Distribution of Runs Scored per Match')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.show()

# 3. Matches Played in Each City
plt.figure(figsize=(10, 6))
sns.barplot(x=city_counts.index, y=city_counts.values, color='skyblue')
plt.title('Matches Played in Each City')
plt.xlabel('City')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()

# 4. Average Runs Scored per Season
avg_runs_per_season = ipl_df.groupby('season')['runs_scored'].mean()
plt.figure(figsize=(8, 5))
sns.lineplot(x=avg_runs_per_season.index, y=avg_runs_per_season.values, marker='o', color='red')
plt.title('Average Runs Scored per Season')
plt.xlabel('Season')
plt.ylabel('Average Runs Scored')
plt.grid(True)
plt.show()

# 5. Most Player of the Match Awards
plt.figure(figsize=(12, 6))
sns.barplot(x=player_of_match_counts.index, y=player_of_match_counts.values, color='coral')
plt.title('Player of the Match Awards')
plt.xlabel('Player')
plt.ylabel('Number of Awards')
plt.xticks(rotation=45)
plt.show()

# 6. Correlation Heatmap
numeric_cols = ipl_df.select_dtypes(include=['number'])  # Select numeric columns
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
