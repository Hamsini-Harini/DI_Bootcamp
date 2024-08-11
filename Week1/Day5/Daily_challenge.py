def sort_words():
    input_words = input("Enter a comma-separated sequence of words: ")

    # Split the input string into a list of words
    word_list = [word.strip() for word in input_words.split(',')]

    # Sort the list of words alphabetically
    sorted_words = sorted(word_list)

    # Join the sorted words into a comma-separated string
    result = ','.join(sorted_words)

    print(result)

sort_words()

#Challenge 2

def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    longest = ""

    # Iterate through each word to find the longest one
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

# Test cases
print(longest_word("Margaret's toy is a pretty doll."))  # ➞ "Margaret's"
print(longest_word("A thing of beauty is a joy forever."))  # ➞ "forever."
print(longest_word("Forgetfulness is by all means powerless!"))  # ➞ "Forgetfulness"
