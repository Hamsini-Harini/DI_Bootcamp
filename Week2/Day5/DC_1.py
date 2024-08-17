# # # Answer the following questions

# # # What is a class? 
# # A blueprint for creating objects - contains attributes and functions those objects will inherit

# # # What is an instance?
# #n instance is an individual object created from a class.
# # # What is encapsulation?
# # it's one of the principles in OOP. We encapsulate methods under a class and attributes under a class.
# # by doing so, we "hide / encapsulate" the internal details of an object and only exposing the necessary parts. 
# # # What is abstraction?
# # You only need to know what a method or class can do, without worrying about how it's implemented. It hides complex reality while exposing only the necessary parts

# # # What is inheritance?
# allows one class (child) to inherit the attributes and methods of another class (parent). This helps you reuse code instead of writing everything from scratch. It's like how children inherit features from their parents.

# # # What is multiple inheritance?
#when a class can inherit from more than one parent class. This is like a child inheriting traits from both their mother and father. 
# one should be carefull when using multiple inheritence, makes code more complex and less readable
# # # What is polymorphism?
# it means "more forms"- llows methods to do different things based on the object calling them. 
# so an object dog and object cat for example can use the same method "Run"

# What is method resolution order or MRO?
# MRO stands for method resolution order. So it tells us there are cases when methods are in some kind of conflict - and Python applies MRO rules to resolve that conflict. For example If a class inherits from multiple parents, MRO decides in which order Python looks for the methods.

#----------------------------------------------------


class Card:
    def __init__(self, suit: str, value: str) -> None:
        """
        Initialize a card with a suit and a value.
        :param suit: The suit of the card (e.g., 'Hearts', 'Diamonds')
        :param value: The value of the card (e.g., 'A', '2', '3', ..., 'K')
        """
        self.suit = suit 
        self.value = value

    def __repr__(self) -> str: #remember, we can't just print objects in human readable way so we need this dunder method, btw __str__ does the same/similar
        """
        Provide a string representation of the card (object).
        :return: The value and suit of the card (e.g., 'A of Hearts')
        """
        return f"{self.value} of {self.suit}"

import random  # To shuffle the deck

class Deck:
    def __init__(self) -> None:
        """
        Initialize a deck of 52 cards (13 values for 4 suits).
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']  
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # The 13 values for each suit
        self.cards = [Card(suit, value) for suit in suits for value in values]  # Create the deck of cards with list comprehension
        # ^^ we have nested for loops, basically for each combination of suit and value, we create a Card object
        self.shuffle()  # Shuffle the deck when it's created

    def shuffle(self) -> None:
        """
        Shuffle the deck to rearrange the cards randomly.
        """
        random.shuffle(self.cards)  # Shuffle the list of cards in place

    def deal(self) -> Card:
        """
        Deal a card from the deck. Remove and return the top card.
        :return: A Card object that is dealt from the deck.
        """
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt!")  #  deck is empty
        return self.cards.pop()  # Remove and return the top card from the deck


deck = Deck()  # Create a new deck of cards
print(deck.deal())  # Deal one card
print(deck.deal())  # Deal another card
deck.shuffle()  # Shuffle the deck again
