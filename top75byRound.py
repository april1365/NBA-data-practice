import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the nba.sqlite database file
conn = sqlite3.connect('nba.sqlite')

# Load the player_info and draft_history tables into Pandas DataFrames
player_info = pd.read_sql_query("SELECT * FROM common_player_info;", conn)
draft_history = pd.read_sql_query("SELECT * FROM draft_history;", conn)

# Close the connection
conn.close()

#print unique values for round drafted
print(draft_history['round_number'].unique())

# Join the player_info and draft_history tables on person_id
drafted_players = pd.merge(draft_history, player_info, left_on='person_id', right_on='person_id', how='inner')

# Filter the DataFrame to keep only top 75 players
top_75_players = drafted_players[drafted_players['greatest_75_flag'] == 'Y']
print(top_75_players)
# Count the number of top 75 players drafted in each round
top_75_players_by_round = top_75_players.groupby('round_number').size().reset_index(name='num_players')

# Convert the 'round_number' column to int
top_75_players_by_round['round_number'] = top_75_players_by_round['round_number'].astype(int)

# Create a bar chart to visualize the number of top 75 players drafted in each round
plt.figure(figsize=(8, 6))
plt.bar(top_75_players_by_round['round_number'], top_75_players_by_round['num_players'])
plt.xlabel('Draft Round')
plt.ylabel('Number of Top 75 Players')
plt.title('Number of Top 75 Players Drafted by Round')

# Set xticks
xticks = top_75_players_by_round['round_number'].unique()
plt.xticks(xticks, xticks)

#plt.show()


# # Find the top 75 players in the draft_history table
# draft_history_top_75 = draft_history[draft_history['person_id'].isin(top_75_players['person_id'])]

# # Display the number of top 75 players in the draft_history table
# print(f"Number of top 75 players in the draft_history table: {len(draft_history_top_75)}")

# # Display the distribution of round numbers for the top 75 players in the draft_history table
# round_distribution = draft_history_top_75['round_number'].value_counts()
# print("Distribution of round numbers for top 75 players in the draft_history table:")
# print(round_distribution)









top_75_player_names = [
    "Michael Jordan",
    "LeBron James",
    "Kareem Abdul-Jabbar",
    "Magic Johnson",
    "Wilt Chamberlain",
    "Bill Russell",
    "Larry Bird",
    "Tim Duncan",
    "Oscar Robertson",
    "Kobe Bryant",
    "Shaquille O'Neal",
    "Kevin Durant",
    "Hakeem Olajuwon",
    "Julius Erving",
    "Moses Malone",
    "Stephen Curry",
    "Dirk Nowitzki",
    "Giannis Antetokounmpo",
    "Jerry West",
    "Elgin Baylor",
    "Kevin Garnett",
    "Charles Barkley",
    "Karl Malone",
    "John Stockton",
    "David Robinson",
    "John Havlicek",
    "Isiah Thomas",
    "George Mikan",
    "Chris Paul",
    "Dwyane Wade",
    "Allen Iverson",
    "Scottie Pippen",
    "Kawhi Leonard",
    "Bob Cousy",
    "Bob Pettit",
    "Dominique Wilkins",
    "Steve Nash",
    "Rick Barry",
    "Kevin McHale",
    "Patrick Ewing",
    "Walt Frazier",
    "Gary Payton",
    "Jason Kidd",
    "Bill Walton",
    "Bob McAdoo",
    "Jerry Lucas",
    "Ray Allen",
    "Wes Unseld",
    "Nate Thurmond",
    "James Harden",
    "Reggie Miller",
    "George Gervin",
    "Clyde Drexler",
    "Pete Maravich",
    "Earl Monroe",
    "James Worthy",
    "Willis Reed",
    "Elvin Hayes",
    "Nate Archibald",
    "Sam Jones",
    "Dave Cowens",
    "Paul Pierce",
    "Robert Parish",
    "Hal Greer",
    "Lenny Wilkens",
    "Paul Arizin",
    "Dennis Rodman",
    "Russell Westbrook",
    "Carmelo Anthony",
    "Dolph Schayes",
    "Anthony Davis",
    "Billy Cunningham",
    "Dave DeBusschere",
    "Dave Bing",
    "Damian Lillard"
]


player_name_to_id = dict(zip(draft_history['player_name'], draft_history['person_id']))


# Find the person_id for each player in the top 75 player names list
top_75_player_ids = [player_name_to_id.get(name, None) for name in top_75_player_names]

# Filter the draft_history DataFrame to include only the top 75 players
draft_history_top_75 = draft_history[draft_history['person_id'].isin(top_75_player_ids)]

# Display the number of top 75 players in the draft_history table
print(f"Number of top 75 players in the draft_history table: {len(draft_history_top_75)}")

# Display the distribution of round numbers for the top 75 players in the draft_history table
round_distribution = draft_history_top_75['round_number'].value_counts()
print("Distribution of round numbers for top 75 players in the draft_history table:")
print(round_distribution)
#print count of total players in round_distribution
print(round_distribution.sum())

# Extract the player names found in the draft_history DataFrame
found_player_names = draft_history_top_75['player_name'].tolist()

# Find the missing player names
missing_player_names = set(top_75_player_names) - set(found_player_names)

# Display the number of missing players and their names
print(f"Number of missing players: {len(missing_player_names)}")
print("Missing player names:")
print(missing_player_names)

