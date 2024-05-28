import pandas as pd

# a. Import the dataset from this [address] and assign it to df variable.
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
df = pd.read_csv(url, sep=",")

# b. Select only the Team, Yellow Cards and Red Cards columns.
needed_columns = ["Team", "Yellow Cards", "Red Cards"]
needed_df = df[needed_columns]
print(needed_df)

# c. How many teams participated in the Euro2012?
unique_teams = needed_df["Team"].nunique()
print(f"In ther Euro 2012 participated {unique_teams} teams")

# d. Filter teams that scored more than 6 goals
teams_goals = ["Team", "Goals"]
filtered_df = df[teams_goals]
target_teams = filtered_df[filtered_df["Goals"] > 6]
print(f"Teams that scored more than 6 goals: \n {target_teams}")