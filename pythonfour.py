dictionary = {
    "wood": "wawa",
    "description": ["apotracheal","diffuse porous", "tyloses"],
    "uses":["furniture", "flooring", "moulding"]
}

# dictionary["colour"] ="white"

dictionary['colour'] = ['white','yellowish']

# print(dictionary)

print(f"{dictionary['description'][2].title()} resemble water bubbles.")
print('\n')

print(f"{dictionary['wood'].title()} is used as {dictionary['uses'][1]} material.")

for x in dictionary['uses']:
    print(x)
   
    print(f"{dictionary['wood'].title()} can be used as {x}.")

