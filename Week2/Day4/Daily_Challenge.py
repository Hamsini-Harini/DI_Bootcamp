class Text:
    def __init__(self, text):
        self.text = text  # Stores the provided text as an instance variable (accessible by all methods)
    
    #frequency of word = split text into words and count each word (there should be module fo this also)

    def word_frequency(self, word):
        words = self.text.lower().split()  # Convert text to lowercase and split into words
        frequency = words.count(word.lower())  # Count occurrences of the word (case-insensitive)
        
        if frequency == 0:  # Check if the word is not found
            return f"'{word}' not found in the text."
        else:
            return f"The word '{word}' appears {frequency} times."
        

    def most_common_word(self):
        from collections import Counter  # Import Counter for counting word frequencies
        
        words = self.text.lower().split()  # Convert text to lowercase and split into words
        if not words:  # If it's true that list is empty, remember we need True to enter the If body
            return "The text is empty."
        
        word_counts = Counter(words)  # Count the frequency of each word in dictionary like object
        most_common = word_counts.most_common(1)[0]  # Get the most common word and its count
        
        return f"The most common word is '{most_common[0]}' with {most_common[1]} occurrences."

    def unique_words(self) -> set: 
        words = self.text.lower().split()  # Convert text to lowercase and split into words
        unique = set(words) 
        
        return list(unique)  # Return the set as a list for easier use
    
    #CODE FOR PART 1
    @classmethod
    def from_file(cls, filename):
        """Creates a Text instance from the contents of a text file."""
        try:
            with open(filename, 'r') as file:  # Open the file for reading
                text = file.read()  # Read the entire file into a string
            return cls(text)  # Create a new Text instance with the file's content
        except FileNotFoundError:
            return f"File '{filename}' not found."
    
    # TESTING THE CODE for part 1

#creating instance of a class
my_text = Text ("A good book would sometimes cost as much as a good house.")

#test freuency fx
frequency_output = my_text.word_frequency("good") 
print(frequency_output)

most_common_word_output = my_text.most_common_word()  # Should return the most frequent word
print (most_common_word_output)     

unique_words_output = my_text.unique_words()
print(unique_words_output)  


# PART 2 testing ------------------------------------------------

my_file_text = Text.from_file('the_stranger.txt')
my_file_text.word_frequency("the")
my_file_text.most_common_word()
my_file_text.unique_words()

# note to checker, not sure where the error in second part is coming from


