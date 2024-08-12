# 🌟 Exercise 1 : Pets
# Using this code:
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.
class Siamese(Cat):
    pass
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
cat1 = Bengal("Fluffy", 3)
cat2 = Chartreux("Garfield", 5)
cat3 = Siamese("Whiskers", 1)
all_cats = [cat1, cat2, cat3]   
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
sara_pets = Pets(all_cats)
# Take all the cats for a walk, use the walk method.
sara_pets.walk()    


# 🌟 Exercise 2 : Dogs
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
    # bark: returns a string which states: “<dog_name> is barking”.
    # run_speed: returns the dogs running speed (weight/age*10).
    # fight : takes a parameter which value is another Dog instance, called other_dog. 
    #   This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight/self.age *10
    
    def fight(self, other_dog):
        self_power = self.weight * self.run_speed()
        other_power = other_dog.weight * other_dog.run_speed()
        if self_power > other_power:
            return f"{self.name} wins the fight!"
        else:
            return f"{other_dog.name} wins the fight!"
# Create 3 dogs and run them through your class.
dog1 = Dog("Fluffy", 3, 50) 
dog2 = Dog("Garfield", 5, 100)
dog3 = Dog("Whiskers", 1, 10)
# Test the methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

# 🌟 Exercise 3 : Dogs Domesticated
# NOTE TO CHECKER - DANIEL TOLD US TO SKIP EXERCISE WITH MODULE SINCE WE DIDN'T COVER IT

# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.







# Exercise 4 : Family
# Create a class called Family and implement the following attributes:
# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.
class Family():
    def __init__(self, last_name:str, members:list): #MEMBERS IS A LIST OF DICTIONARIES CONTAINING NAME AGE GENDER AND IS_CHILD boolean
        self.last_name = last_name
        self.members = members
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"{self.last_name} was born!")

    def is_18(self, name):
                # Iterate over the members list to find the member with the given name
        for member in self.members:
            if member['name'] == name:
                # Check if the member's age is greater than or equal to 18
                return member['age'] >= 18
        return False  # Return False if the member is not found
    
    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        # Print details for each member of the family
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.
#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]
# create the following variable here, instead of entering this huge list in the place of parameter members
family_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

smith_family = Family(last_name="Smith", members=family_members)

smith_family.family_presentation()

# Check if a family member is over 18
smith_family.is_18("Michael")  # Expected: True

smith_family.born(name='James', age=0, gender='Male', is_child=True)

# Print the family presentation again to see the updated family
smith_family.family_presentation()








# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
# Add a method called incredible_presentation which :
# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        # Call the constructor of the parent class to initialize last_name and members
        super().__init__(last_name, members)

    def use_power(self, name):
        """
        Print the power of a member if they are over 18.
        Raises an exception if the member is not over 18.
        """
        # Find the member by name in the members list
        for member in self.members:
            if member['name'] == name:
                # Check if the member is over 18
                if member['age'] >= 18:
                    print(f"{member['name']}'s power is: {member['power']}")
                else:
                    # Raise an exception if the member is not over 18
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power!")
                return  # Exit the method once the member is found

        # Raise an exception if the member is not found
        raise Exception(f"No member named {name} found in the family.")

    def incredible_presentation(self):
        """
        Present the Incredibles family and their details.
        """
        # Print an introductory sentence
        print("*Here is our powerful family*")
        # Use the super() function to call the family_presentation method from the parent class
        super().family_presentation()

# Now, let's create an instance of TheIncredibles and test these methods.


# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]

# Call the incredible_presentation method.
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# Call the incredible_presentation method again.
# Create an instance of TheIncredibles


incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredible_family = TheIncredibles(last_name="Incredibles", members=incredibles_members)

# Call the incredible_presentation method
incredible_family.incredible_presentation()

# Use the use_power method
try:
    incredible_family.use_power("Michael")  # Should print Michael's power
    incredible_family.use_power("Sarah")    # Should print Sarah's power
except Exception as e:
    print(e)

# Add a new child to the family using the born method
incredible_family.born(name='Baby Jack', age=1, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

# Call the incredible_presentation method again to see the updated family
incredible_family.incredible_presentation()

# Test the use_power method with the new child (should raise an exception)
try:
    incredible_family.use_power("Baby Jack")
except Exception as e:
    print(e)  # Expected to print the exception message because Baby Jack is not over 18
