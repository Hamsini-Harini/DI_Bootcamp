# Exercise 1 : What are you learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
  

def display_message(subject):
    display_message_result = f"I am learning {subject}."
    return display_message_result

print(display_message("Python"))

# 🌟 Exercise 2: What’s your favorite book ?
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    favorite_book_result = print(f"One of my favorite books is {title}.")
    return favorite_book_result
favorite_book("Alice in Wonderland")

# 🌟 Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(name,country="Iceland"):
    describe_city_result = print(f"{name} is in {country}.")
    return describe_city_result
describe_city("Belgrade")

# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

#NOTE TO CHECKER: WE DIDN'T LEARN RANDOM MODULE, WHY IS THERE SUCH EXERCISE?
# import random

# def number_guessing_game():
#   random_number = random.randint(1, 100)
#   guess = 0

#   while guess != random_number:
#     guess = int(input("Guess a number between 1 and 100: "))

#     if guess < random_number:
#       print("Too low!")
#     elif guess > random_number:
#       print("Too high!")
#     else:
#       print("Congratulations! You guessed it!")

# number_guessing_game()


# 🌟 Exercise 5 : Let’s create some personalized shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

def make_shirt(size, text):
   make_shirt_result= print(f"The size of the shirt is {size} and the text is {text}.")
   return make_shirt_result
make_shirt("xxl", "I love Python")



# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
def make_shirt(size="large", text="I love Python"):
   make_shirt_result= print(f"The size of the shirt is {size} and the text is {text}.")
   return make_shirt_result
make_shirt()


# Make medium shirt with the default message

def make_shirt(size, text="I love Python"):
   make_shirt_result= print(f"The size of the shirt is {size} and the text is {text}.")
   return make_shirt_result
make_shirt("medium")
# Make a shirt of any size with a different message.

def make_shirt(size, text):
   make_shirt_result= print(f"The size of the shirt is {size} and the text is: {text}.")
   return make_shirt_result
make_shirt("XXL", "This is an eco friendly shirt")


# Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(**kwargs):
#    make_shirt_result= print(f"The size of the shirt is {size} and the text is: {text}.")
#    return make_shirt_result
# make_shirt(size = "XXL", color = "Blue", text = "I love Python" )

#NOTE TO THE CHECKER - I DON"T KNOW HOW TO USE KWARGS IN F-STRING - looks like I need to know in advance what user will input


# 🌟 Exercise 6 : Magicians …
# Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
def show_magicians():
    for name in magician_names:
        print(name)
show_magicians()
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
def make_great(magician_names):
    new_magician_names = []
    for name in magician_names:
        name = "the Great " + name
        new_magician_names.append(name)
    print(new_magician_names)
make_great(magician_names)

# Call the function show_magicians() to see that the list has actually been modified.

show_magicians() # I created new list so the original list did not change!

# 🌟 Exercise 7 : Temperature Advice
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

def get_random_temp():
    import random
    random.randint(-10, 40)
    random_temp_chosen = random.randint(-10, 40)
    # I defined random_temp_chosen inside the function so I can't call it outside (not sure if global would help here)
    return random_temp_chosen
    # NOTE TO MYSELF - you can't put any code after return statement, return includes exiting the function
print(get_random_temp())


# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

def main():
    random_temp_value = get_random_temp()
    print(f"The temperature right now is {random_temp_value} degrees Celsius.")
main()


# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

def main():
    random_temp_value = get_random_temp()
    print(random_temp_value)
    if random_temp_value < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif random_temp_value < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif random_temp_value <16 and random_temp_value< 24:
        print("Cool weather today.")
    else:
        print("Perfect weather today, or is it too hot for you")

main()


# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.

# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().



import random
user_input = input("Enter a season: ")
def get_random_temp(season):
  """Generates a random temperature based on the given season."""
  if season == "winter":
    return random.randint(-10, 16)
  elif season == "spring":
    return random.randint(5, 22)
  elif season == "summer":
    return random.randint(18, 35)
  elif season == "autumn" or season == "fall":
    return random.randint(10, 25)
  else:
    print("Invalid season")
    return None

get_random_temp(user_input)

#NOTE TO CHECKER - not sure why is this producing no result?


# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


# 🌟 Exercise 8 : Star Wars Quiz - THIS WAS TOO HARD
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


# Create a function that asks the questions to the user, and check his answers. 
# Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.





# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.