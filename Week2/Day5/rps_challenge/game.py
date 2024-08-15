import random 
class Game:
    def get_user_item(self) -> str:
        """
        Asks the user to choose between rock, paper, or scissors.
        Keeps asking until a valid input is received.
        Returns:
            str: The user's chosen item.
        """
    
        while True:
            user_input = input("Select (r)ock, (p)aper, or (s)cissors: ").lower() 
            if user_input in ['r', 'p', 's']:  # Validating the input
                if user_input == 'r':
                    return "rock"
                elif user_input == 'p':
                    return "paper"
                else:
                    return "scissors"
            print("Invalid choice, please try again!")  # Informs the user if the choice is invalid

    def get_computer_item(self) -> str:
        """
        Computer randomly selects rock, paper, or scissors.
        Returns:
            str: The computer's chosen item.
        """
        return random.choice(["rock", "paper", "scissors"])  # Randomly choosing one of three options

    def get_game_result(self, user_item: str, computer_item: str) -> str:
        """
        Returns:
            str: 'win' if the user wins, 'loss' if the computer wins, or 'draw' if it's a tie.
        """
        # The logic to determine the outcome of the game
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"

    def play(self) -> str:
        """ Plays a single round of rock-paper-scissors.
        Returns:
            str: The result of the game ('win', 'draw', or 'loss').
        """
        user_item = self.get_user_item() 
        computer_item = self.get_computer_item()  
        result = self.get_game_result(user_item, computer_item) 

        print(f"You chose: {user_item}. The computer chose: {computer_item}. Result: {result}")
        return result
