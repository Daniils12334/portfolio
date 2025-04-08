#dictionary = a collection of {key:value} pairs

games = {   'Hoearts of Iron 5': 'Strategy',
            'FIFA 2020': 'Sports',
            'CS:GO': 'FPS',
            'Ark: Survival Evolved': 'Survival',
            'God of War': 'Adventure'}

# print(dir(games))
# print(help(games))

# print(games.get('FIFA 2020'))
# if games.get("CS:GO"):
    # print("the game exists")
# else:
    # print("the game does not exist")

# games.update({'Ark survival Ascended': 'Survival'}) # adds a new key:value pair
# games.pop('FIFA 2020') # removes a key:value pair
# games.popitem() # removes the last key:value pair
# games.clear() # removes all key:value pairs

keys = games.keys()
print(keys)

for key in games.keys():
    print(key)

values = games.values()
print(values)
for value in games.values():
    print(value)

items = games.items()
for key, value in games.items():
    print(f"{key}: {value}")
    