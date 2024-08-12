#Colab Link Gabriel - https://colab.research.google.com/drive/1YuI4SHulFxDA7v3yTeT1yt-xqpBmNNVO?usp=sharing

# #exercise Gabriel gave us


# Exercise: *Vehicle Inheritance*
#  Objective:
# Create a simple class hierarchy to manage different types of vehicles using inheritance. The exercise will focus on sharing common behavior among different vehicle types and adding specific behavior for each type.
#  Requirements:
# 1. *Base Class: Vehicle*
#    - *Attributes*:
#      - make: The manufacturer of the vehicle.
#      - model: The model of the vehicle.
#    - *Methods*:
#      - start(): Prints a message indicating that the vehicle is starting.
#      - stop(): Prints a message indicating that the vehicle is stopping.
# 2. *Derived Class: Car*
#    - *Attributes*:
#      - Inherits all attributes from Vehicle.
#      - number_of_doors: The number of doors the car has.
#    - *Methods*:
#      - Inherits all methods from Vehicle.
#      - open_trunk(): Prints a message indicating that the trunk is being opened.
# 3. *Derived Class: Motorcycle*
#    - *Attributes*:
#      - Inherits all attributes from Vehicle.
#      - has_sidecar: A boolean indicating if the motorcycle has a sidecar.
#    - *Methods*:
#      - Inherits all methods from Vehicle.
#      - pop_wheelie(): Prints a message indicating that the motorcycle is popping a wheelie.
# Instructions:
# 1. Implement the Vehicle, Car, and Motorcycle classes according to the specifications.
# 2. Create a Car instance with the make "Toyota", model "Corolla", and 4 doors. Call the start(), open_trunk(), and stop() methods.
# 3. Create a Motorcycle instance with the make "Harley-Davidson", model "Street 750", and no sidecar. Call the start(), pop_wheelie(), and stop() methods.
# Expected Output:
# After implementing the classes and running the operations, you should see output similar to the following:
# Toyota Corolla is starting.
# Opening the trunk of the Toyota Corolla.
# Toyota Corolla is stopping.
# Harley-Davidson Street 750 is starting.
# Harley-Davidson Street 750 is popping a wheelie!
# Harley-Davidson Street 750 is stopping.