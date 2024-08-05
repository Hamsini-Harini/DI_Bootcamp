#Exercise 1
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {7, 2, 44, 63, 33, 77}
my_fav_numbers.add(12)
my_fav_numbers.add(112)
my_fav_numbers.remove(112)
print(my_fav_numbers)

friend_fav_numbers = {1, 2, 3, 4, 5, 6}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Given a tuple which value is integers, is it possible to add more integers to the tuple?
#Answer - tuples are immutable but a way around would be to create a new tuple and then add them together or we can covert tuple to a list


# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana") 
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()

print(basket)



# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

#Answer: float is decimal number, integer is whole number
my_list = []
number = 1.5
while number <= 5:
  my_list.append(number)
  number += 0.5

print(my_list)
# Answer - I think we can use list comprehension to generate list of floats (preparation project)









# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for num in range(1, 21):
    print(num)

for num in range(0,21):
   if num % 2 == 0:
       print(num)






#      Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


my_name = "Alex"
user_name = input("Please enter your name: ")
while user_name != my_name:
    user_name = input("Please enter your name:")
print("Our names match")





# 🌟 Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user_fav_fruits = input("Please enter your favorite fruits separated by a space: ")
user_fav_fruits = user_fav_fruits.split()

any_fruit = input("Please enter any fruit: ")
if any_fruit in user_fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")






# Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
topping = ""
total_price = 10

while topping != "quit":
  topping = input("Enter a pizza topping (or 'quit' to finish): ")
  if topping != "quit":
    toppings.append(topping)
    print(f"I'll add {topping} to your pizza.")
    total_price += 2.5

print("\nYour pizza with the following toppings:")
for topping in toppings:
  print(f"- {topping}")
print(f"will cost ${total_price:.2f}")






# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

total_cost = 0
while True:
  person_age = input("Enter the age of each person (or 'done' to finish): ")
  if person_age == 'done':
    break
  person_age = int(person_age)
  if person_age < 3:
    ticket_price = 0
  elif person_age <= 12:
    ticket_price = 10
  else:
    ticket_price = 15
  total_cost += ticket_price

print(f"The total cost of tickets for your family is ${total_cost}.")























# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich