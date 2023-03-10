"""removes repeated photos from json file"""


import json


with open("data/photos_all.json") as f:
    photo_data = json.loads(f.read())

# print (len(photo_data))

# Convert each dictionary to a tuple of key-value pairs
list_of_tuples = [tuple(d.items()) for d in photo_data]

# Eliminate duplicates by converting the list to a set and then back to a list
unique_tuples = list(set(list_of_tuples))

# Convert each tuple back to a dictionary
photos_list = [dict(t) for t in unique_tuples]


# print (photos_list)
# print (len(photos_list))

with open("data/photos_all2.json", 'w') as f:
    json.dump(photos_list, f)

