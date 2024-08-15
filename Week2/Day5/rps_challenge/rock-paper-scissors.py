from game import Game 

def get_user_menu_choice() -> str:
    """
    Displays the main menu and gets the user's choice.
    """
    # Display the menu options to the user
    print("\nMenu:")
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    
    # Keep asking the user until a valid input is provided
    choice = input("Please select an option: ").lower()
    if choice in ['g', 'x']:
        return choice
    else:
        print("Invalid option, please try again.")
        return get_user_menu_choice()  # Recursively ask again if invalid choice

def print_results(results: dict) -> None:
    """
    Prints the results - scoreboard of all games played.
    Args:
        results (dict): A dictionary containing the game results for user only since we don't present this statistic to computer.
            It should have the keys 'win', 'loss', and 'draw'.
    """
    print("\nGame Results:")
    print(f"You won {results['win']} times")
    print(f"You lost {results['loss']} times")
    print(f"You drew {results['draw']} times")


if __name__ == "__main__":
    def main() -> None:
        """
        The main function that runs the rock-paper-scissors game loop.
        """
    # Initialize the results dictionary
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        # If the user chooses to play a new game
        if choice == 'g':
            game = Game()  # Create a new Game object
            result = game.play()  # Play a single game
            
            # Update the results dictionary based on the game outcome
            if result == "win":
                results["win"] += 1
            elif result == "loss":
                results["loss"] += 1
            elif result == "draw":
                results["draw"] += 1

        # If the user chooses to exit and show scores
        elif choice == 'x':
            print_results(results)  # Show the game results
            break  # Exit the game loop

