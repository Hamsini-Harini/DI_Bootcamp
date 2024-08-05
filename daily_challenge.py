# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]


number = int(input("Please enter a number: "))
length = int(input("Please enter a length: "))

result = []
for i in range(1, length + 1):
    multiple = number * i
    result.append(multiple)

print(result)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"
# user's word : "wiiiinnnnd" ➞ "wind"
# user's word : "ttiiitllleeee" ➞ "title"
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).


user_input = input("Enter a word: ")
clear_word = ""
last_seen = {'char': "0"}

for char in user_input:
        if char != last_seen['char']:
            # Append to result if it's not a consecutive duplicate
            clear_word += char
            # Update the last seen character in the dictionary - move the pointer
            last_seen['char'] = char

print(f"The word without consecutive duplicates is: {clear_word}")
