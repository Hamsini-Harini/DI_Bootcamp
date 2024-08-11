# 🌟 Exercise 1: Cats
# Using this class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Instantiate three Cat objects using the code provided above.

cat1 = Cat("Fluffy", 3)
cat2 = Cat("Garfield", 5)
cat3 = Cat("Whiskers", 1)

# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”.

def find_oldest_cat(*args):
    return max(args)

print(f"The oldest cat is {find_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")  

# 🌟 Exercise 2 : Dogs

# Create a class called Dog.
class Dog:
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        print (f"{self.name} goes woof!")
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self):
        print (f"{self.name} jumps {self.height*2} cm high!")

# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
davids_dog = Dog("Rex", 50) # once creating objects we have to pass the (initial) arguments
# davids_dog.name = "Bex" #changing the inital arguments
# davids_dog.height = 250 #changing the initial argumetns

# Print the details of his dog (ie. name and height) and call the methods bark and jump.
print(davids_dog.name, davids_dog.height)
davids_dog.bark()  
davids_dog.jump()  
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
sarahs_dog = Dog("Teacup", 20)
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)

# _________________________________________________________________________

# 🌟 Exercise 3 : Who’s the song producer?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics 

# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# Then, call the sing_me_a_song method. The output should be:

stairway.sing_me_a_song()

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


#_________________________________________________________________________________________

class Zoo:
    def __init__(self, zoo_name):
        """
        Initializes a new Zoo object with a name and an empty list of animals.

        Args:
            zoo_name (str): The name of the zoo.
        """
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        """
        Adds a new animal to the zoo's list if it's not already present.

        Args:
            new_animal (str): The name of the animal to add.
        """
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        """
        Prints a message listing all the animals in the zoo.
        """
        print(f"The zoo has {self.animals} animals.")

    def sell_animal(self, animal_sold):
        """
        Removes an animal from the zoo's list if it exists.

        Args:
            animal_sold (str): The name of the animal to sell (remove).
        """
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        """
        Sorts the animals alphabetically and groups them by their first letter.

        Returns:
            dict: A dictionary where keys are first letters and values are lists of animals starting with that letter.
        """
        sorted_animals = {}  # Create an empty dictionary to store sorted animals
        for animal in self.animals:
            first_letter = animal[0].upper()  # Get the first letter (uppercase)

            # If the first letter key doesn't exist, create it with an empty list
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []

            sorted_animals[first_letter].append(animal)  # Add the animal to its first letter group

        return sorted_animals

# Create an object called ramat_gan_safari and call all the methods.
ramat_gan_safari = Zoo("Central Park Zoo")

# Add some animals to the zoo
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Monkey")
ramat_gan_safari.add_animal("Crocodile")

ramat_gan_safari.sell_animal("Lion")

# Print the animals in the zoo
ramat_gan_safari.get_animals()

# Sort the animals and get the sorted dictionary
sorted_animals = ramat_gan_safari.sort_animals()

# Print the sorted animals (if desired)
print(sorted_animals)

# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)





