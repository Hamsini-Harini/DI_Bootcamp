class Farm:
  """
  This class represents a farm with its animals and their quantities.
  """

  def __init__(self, name):
    """
    This method initializes a new Farm object with a given name.
    It creates an empty dictionary to store animal types and their counts.
    """
    self.name = name
    self.animals = {}  # Dictionary to store animal types (keys) and counts (values)

  def add_animal(self, animal_type, count=1):
    """
    This method adds a new animal type to the farm or increments the count
    of an existing animal type.

    Args:
        animal_type: The type of animal (e.g., cow, sheep, goat).
        count (optional): The number of animals to add (defaults to 1).
    """
    if animal_type in self.animals:
      self.animals[animal_type] += count
    else:
      self.animals[animal_type] = count


  def get_info(self):
    """
    This method generates a string containing the farm's name,
    animal types and their counts, and the "E-I-E-I-0!" song snippet.

    Returns:
        A string containing the formatted farm information.
    """
    info = f"{self.name}'s farm\n\n"  # Start building the info string

    for animal, count in self.animals.items():
      info += f"{animal} : {count}\n"  # Add each animal type and count

    info += "\nE-I-E-I-0!"  # Add the song snippet

    return info
# Test our code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

farm_info = macdonald.get_info()
print(farm_info)







# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheeps.”. The method should call the get_animal_types function to get a list of the animals.
# Note : In English the plural form of the word “sheep” is sheep. But for the purpose of the exercise, let’s say that if there is more than 1 animal, an “s” should be added at the end of the word.


class Farm:
  """
  This class represents a farm with its animals and their quantities.
  """

  def __init__(self, name):
    """
    Initializes a new Farm object with a given name and an empty animals dictionary.
    """
    self.name = name
    self.animals = {}

  def add_animal(self, animal_type, count=1):
    """
    Adds a new animal type or increments the count of an existing animal type.
    """
    if animal_type in self.animals:
      self.animals[animal_type] += count
    else:
      self.animals[animal_type] = count

  def get_info(self):
    """
    Generates a string containing the farm's name, animal types and counts, and a song snippet.
    """
    info = f"{self.name}'s farm\n\n"
    for animal, count in self.animals.items():
      info += f"{animal} : {count}\n"
    info += "\nE-I-E-I-0!"
    return info

  def get_animal_types(self):
    """
    Returns a sorted list of all animal types on the farm.
    """
    return sorted(list(self.animals.keys()))

  def get_short_info(self):
    """
    Returns a short description of the farm with animal types in plural form.
    """
    animal_types = self.get_animal_types()
    animal_types_str = ", ".join([f"{animal}{'s' if self.animals[animal] > 1 else ''}"] for animal in animal_types)
    return f"{self.name}'s farm has {animal_types_str}."

