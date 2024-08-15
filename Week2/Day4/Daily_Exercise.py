import random
import os
os.getcwd()
def get_words_from_file():
    with open ("Week2/Day4/Words_Ex.txt", "r") as file:
        words = file.read().splitlines()  
        return words

def get_random_sentence(lenght):
    if lenght < 2 or lenght > 20:
        raise ValueError("lenght must be between 2 and 20")
    words = get_words_from_file()  # Get the list of words from the file
    random_words = random.sample(words, lenght)  # random.sample() returns a list of unique random elements from the list
    sentence = " ".join(random_words).lower()  # " ".join() combines the list into a string with spaces, .lower() converts it to lowercase
    return sentence


def main():
    """
    This is the main function that runs the program.
    """
    print("This program generates a random sentence of a specified length.")  # Inform the user about the program's purpose

    try:
        length = int(input("How long should the sentence be (2-20 words)? "))  # Get the sentence length from the user
        if length < 2 or length > 20:  # Validate that the length is within the acceptable range
            print("Error: The length must be between 2 and 20.")
            return  # Exit the program if the input is invalid

        sentence = get_random_sentence(length)  # Generate the random sentence
        print("Your random sentence is:", sentence)  # Print the generated sentence

    except ValueError:
        print("Error: Please enter a valid integer.") 

main()



# 2 ---------------------------------------------------------------------------
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

import json

with open("Week2/Day4/sampleJson.json", "r") as file:
    data = json.load(file)

# Now, data is a dictionary that represents the JSON structure, and we can access its elements just like any other Python dictionary.
salary = data["company"]["employee"]["payable"]["salary"]  # Access the nested "salary" key
print("Salary:", salary)  # Print the salary

#Next, we need to add a new key called "birth_date" at the same level as "name". Here's how to do that:
data["company"]["employee"]["birth_date"] = "1990-01-01"

print(json.dumps(data)) # just to make sure data is correct before writing

# Now we need to save the modified JSON back to the same file
with open("Week2/Day4/sampleJson.json", "w") as file: #opens the same  file in writing mode
    json.dump(data, file)

# NOTE TO CHECKER - I am having some basic problem with accessing the file, I never know do I need relative path or no and also what is directory ?



