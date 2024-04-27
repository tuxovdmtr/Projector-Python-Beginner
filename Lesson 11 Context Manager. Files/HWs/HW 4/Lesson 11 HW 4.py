# Write a script that reads the data from the previous CSV file and creates a new file called high_scores.csv
# where each row contains the player name and their highest score.
# The final score should be sorted by descending to the highest score.

# The output CSV file should look like this:
# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345

import csv

player_scores = []
with open('Lesson 11 Context Manager. Files/HWs/HW 4/final_scores.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        player_scores.append(row)
print(player_scores)

max_score = 0
high_scores = dict()
for item in player_scores:
    player = item["Player name"]
    score = int(item["Score"])
    if score > max_score or player not in high_scores:
        max_score = score
        high_scores[player] = score
print(high_scores)

high_scores_sorted = sorted(high_scores.items(), key = lambda x: x[1], reverse=True)

with open("Lesson 11 Context Manager. Files/HWs/HW 4/final_scores_sorted.csv", mode = "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow (["Player Name", "Highest Score"])
    for player, score in high_scores_sorted:
        writer.writerow([player,score])

