# Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
# To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains the name of the file and the number in that file:
# A.txt: 67 B.txt: 12...Z.txt: 98

import random
print(ord("A"))
print(ord("Z"))

for i in range(65, 91):
    with open(f"{chr(i)}.txt", "a") as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number))
    with open("summary.txt", "a") as summary:
        summary.write(f"{chr(i)}.txt: {random_number}\n")