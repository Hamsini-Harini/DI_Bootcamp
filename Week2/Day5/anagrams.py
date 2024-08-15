from anagram_checker import AnagramChecker # imported the class (with all it's properties)
def main() -> None:
    """ Main function that runs the user interface for the anagram checker. """
    # Load the anagram checker with the path to the word list after creating instance of the class
    checker = AnagramChecker("Week2/Day5/sowpods.txt")



    while True: #always = while true
            # Displaying menu options
            print("\nAnagram Checker Menu:")
            print("1. Enter a word")
            print("2. Exit")

            choice = input("Choose an option, enter number only: ")

            if choice == '2':
                print("Exiting the program. Goodbye!")
                break

            elif choice == '1':
                user_word = input("Enter a single word: ").strip() #strips accidental spaces or other characters at the begining or end, space between words will stay

                # Check if input is a valid single word (letters only)
                if not user_word.isalpha():
                    print("Error: Please enter a valid word containing only letters.")
                    continue

                # Check if it's a valid word in the dictionary - word list loaded from the file sowpods.txt, which contains valid English words.
                if checker.is_valid_word(user_word):
                    print(f"\nYour word: {user_word.upper()}")
                    print("This is a valid English word.")

                    # Find anagrams
                    anagrams = checker.get_anagrams(user_word)
                    print(f"Anagrams for your word: {', '.join(anagrams)}")
                else:
                    print("This is not a valid English word. Please try again.")

            else:
                print("Invalid option, please choose 1 or 2.")

if __name__ == "__main__": #executable only from this file, important
    main()