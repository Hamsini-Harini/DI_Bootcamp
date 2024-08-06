# 🌟 Exercise 1 : Convert lists into dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = dict(zip(keys, values))
print(dict)




# 🌟 Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_ticket_cost = 0

for name, age in family.items():
    if age < 3:
        total_ticket_cost += 0
    elif age <= 12:
        total_ticket_cost += 10
    else:
        total_ticket_cost += 15

print(f"The total cost for the movies is ${total_ticket_cost}")


# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# number_stores: 7000 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green



# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "number_stores": 7000,
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "major_color": 
    {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
        },
    }

# 3. Change the number of stores to 2.

brand["number_stores"] = 2
print(brand)

# 4. Print a sentence that explains who Zaras clients are.
clients = brand["type_of_clothes"][:3]
print(f"Zara's clients are {clients}.")

# 5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
for key, value in brand.items():
    if key == "international_competitors":
        value.append("Desigual")
        break
print(brand)

# 7. Delete the information about the date of creation.
del brand["creation_date"]
print(brand)

# 8. Print the last international competitor.
last_competitor = brand["international_competitors"][-1]
print(last_competitor)

# 9. Print the major clothes colors in the US.
print(brand["major_color"]["US"])

# 10. Print the amount of key value pairs (ie. length of the dictionary).

print(len(brand)) #but this will not give you sub-dictionaries

# 11. Print the keys of the dictionary..
print(brand.keys())


# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?

print(brand["number_stores"]) # the value is overwritten with the new value


#____________________________________________________________________________________
# Exercise 4 : Disney characters
# Instructions
# Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/ # Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# so we what has been done here - looks like enumerate.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {name: i for i, name in enumerate(users)}
print(disney_users_A)

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Characters with names containing "i"
users_with_i = {user: i for i, user in enumerate(users) if "i" in user}
print(users_with_i)

# Characters with names starting with "m" or "p"
users_starting_mp = {user: i for i, user in enumerate(users) if user.startswith(("m", "p"))}
print(users_starting_mp) #this will outout empty dictionary since Python is case sensistive, I could have used .lower funcion on initial list

# #2/
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B = {}
for i in range(len(users)):
  disney_users_B[i] = users[i]
print(disney_users_B)



# #3/ 
# print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
users.sort()
disney_users_C = {users[i]: i for i in range(len(users))}
print(disney_users_C)



