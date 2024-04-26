# You have 100 cats.
# One day you decide to arrange all your cats in a giant circle.
# Initially, none of your cats have any hats on.
# You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1).
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on,
# or you take its hat off if it has one on.

# In The first round, you stop at every cat, placing a hat on each one
# In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).

# Write a program that simply outputs which cats have hats at the end.

# complexity of your algorithm - O(rounds * cats)


rounds = int(input("Input rounds: "))
cats = int(input("Input number of cats: "))


def get_cats_with_hats(rounds: int, cats: int):
    cats_list = [True] * cats
    cats_with_hats = []
    while rounds > 0:
        for round in range(2, rounds + 1):
            for cat in range(round, len(cats_list)+1, round):
                if cat % round == 0:
                    cats_list[cat-1] = not cats_list[cat-1]
            else:
                rounds -= 1
        break             
    for cat_pos, status in enumerate(cats_list):
        if status == True:
            cats_with_hats.append(cat_pos + 1)
    return cats_with_hats

print(f"Cats with hats: {get_cats_with_hats(rounds, cats)}")