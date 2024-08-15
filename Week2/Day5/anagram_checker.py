class AnagramChecker:
    def __init__(self, file_path: str) -> None: #file_path: The path to the text file containing list of valid words.
        with open(file_path, 'r') as file:
            self.words = [line.strip().lower() for line in file]  # We load the words and convert them to lowercase for consistency
            # processed words from inputed file
    def is_valid_word(self, word: str) -> bool: # word is a word to check
        return word.lower() in self.words    
    
    def get_anagrams(self, word: str) -> list[str]:
        """
        Finds all anagrams of a given word from the word list.
        :param word: The word for which to find anagrams.
        :return: A list of anagrams.
        """
        return [w for w in self.words if self.is_anagram(word, w)] # The list comprehension results in a list of words from 'self.words' that are anagrams of 'word'.
    
    def is_anagram(self, word1: str, word2: str) -> bool:
        """Checks if two words are anagrams of each other."""
          # We sort the letters of both words and check if they match. This works because anagrams have the same letters.
        #Sorting rearranges the letters of the words in alphabetical order, so if they are anagrams, their sorted versions will match
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

# now we create anagrams.py to control user interaction in separate file