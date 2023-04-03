# I have a list of party guests below
party_guests = ['kofi', 'ama', 'kweku']


# Using List Indexing and slicing take each item and apply a an action called title() which will change their first letters to caps
'''
The title method .title()  does not change the list it only does a temporary action to it and returns the result but doesnt permanently change the content of the list.
Also the title can take a string with two names eg 'kofi nimako" and it will change the kofi to Kofi and nimako to Nimako.
'''
print(party_guests[0].title(), party_guests[1].title(), party_guests[2].title())


# I Want you to take the list and add a new guest to it called Ransben
party_guests.append("ransben")


# Now show me the content of my party guests
print(party_guests)



'''
We can also use a for loop to loop over the items and apply a function or action to them like below.
'''
# for item in party_guests:
#     print(item.title())

party_guests.append('asi')
print(party_guests)
print(party_guests[0].title(), party_guests[4].title(), party_guests[3].title())
party_guests.insert(0, 'korkor')
print(party_guests)
print(f'You are welcome to my party, {party_guests[0].title()}!')
party_guests.pop()
print(party_guests.pop(2))
party_guests.sort()
print(party_guests)
