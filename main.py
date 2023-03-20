import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the nba.sqlite database file
conn = sqlite3.connect('nba.sqlite')

# Load the data from the SQLite table into a Pandas DataFrame
table_name = 'game'
query = f"SELECT * FROM {table_name};"
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the first few rows of the DataFrame
print(df.head())

# Basic data transformation and analysis

# Filter rows based on a condition
# Replace 'some_value' with the value you want to filter by
some_value = 100
filtered_df = df[df['pts_home'] > some_value]

# Sort the DataFrame based on a column
sorted_df = df.sort_values(by='pts_home', ascending=False)

# Group by a column and compute the mean
grouped_df = df.groupby('team_abbreviation_home').mean()

# Compute a new column based on existing columns
df['total_pts'] = df['pts_home'] + df['pts_away']

# Basic data visualization using Matplotlib or Seaborn

# Scatter plot
plt.scatter(df['pts_home'], df['pts_away'])
plt.xlabel('Home Team Points')
plt.ylabel('Away Team Points')
plt.title('Scatter Plot of Home Team Points vs Away Team Points')
plt.show()

# Histogram
plt.hist(df['total_pts'], bins=10)
plt.xlabel('Total Points')
plt.ylabel('Frequency')
plt.title('Histogram of Total Points')
plt.show()



# Compute the correlation matrix for numeric columns
corr_matrix = df.corr(numeric_only=True)

# Set the plot style and font size
sns.set(style="white", font_scale=1.2)

# Create a custom colormap for the heatmap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Set the figure size
plt.figure(figsize=(14, 10))

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_matrix, cmap=cmap, annot=True, fmt=".2f", linewidths=.5, cbar_kws={"shrink": .5}, annot_kws={"size": 10})

# Set the title
plt.title('Correlation Matrix', fontsize=18)

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.show()
