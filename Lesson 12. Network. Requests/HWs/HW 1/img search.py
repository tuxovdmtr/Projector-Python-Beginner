#Create a program that allows you to search for images in gif format.
# The program should allow you to enter a search word.
# Using this word, search for GIFs using the Giphy API.
# As a result, print the links to the GIFs.

import requests

api_key = "FINmM5yMk9PykNRq7zr8sWZB7npAxagO"
q = input("Enter a word to search an image: ")

response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={q}")
dict = response.json()
data = dict["data"]
print(f"Here are {len(data)} {q} GIFs")
for i in range(len(data)):
    print(data[i]["embed_url"])
