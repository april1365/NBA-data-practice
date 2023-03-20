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

# Join the player_info and draft_history tables on person_id
drafted_players = pd.merge(draft_history, player_info, left_on='person_id', right_on='person_id', how='inner')

# Add a 'region' column to indicate if the player is from the US or not
drafted_players['region'] = 'Non-US'
drafted_players.loc[drafted_players['country'] == 'USA', 'region'] = 'US'

# Count the number of players drafted by region and draft year
drafted_players_by_region_year = drafted_players.groupby(['region', 'draft_year']).size().reset_index(name='num_players')

# Pivot the DataFrame to make the draft year the columns and regions the index
drafted_players_pivot = drafted_players_by_region_year.pivot_table(index='region', columns='draft_year', values='num_players', fill_value=0)

# Transpose the DataFrame and plot a line chart to visualize the growth of US and Non-US players over time
drafted_players_pivot.T.plot(kind='line', figsize=(14, 8), marker='o')
plt.xlabel('Draft Year')
plt.ylabel('Number of Players Drafted')
plt.title('Number of US and Non-US Players Drafted Over Time')
plt.legend(title='Region')
plt.show()
