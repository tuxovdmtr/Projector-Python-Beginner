# Write a program that will simulate user scores in a game.
# Create a list with 5 players’ names after that simulate 100 rounds for each player.
# As a result of the game create a list with the player's name and score (0-1000 range).
#And save it to a CSV file.

#The file should look like this:
#Player name, Score
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345

import random
import csv

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
player_scores = []
score = int()

for player in players:
    for round in range(1, 101):
        score = random.randint(0, 1000)
        player_scores.append([player, score])
    score = 0
print(player_scores)

with open("final_scores.csv", mode = "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Score"])
    writer.writerows(player_scores)